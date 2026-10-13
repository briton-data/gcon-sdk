"""Run one job on two independent nodes and compare their results.

Use this for work where a wrong answer is costly. The replicas agree only if
their output is identical, so the command must be deterministic: no
timestamps, random numbers or other values that change between runs.

Usage:
    export GCON_URL="<your GCON service URL>"
    export GCON_KEY="gcon_..."
    python examples/02_replicated_job.py
"""
import os
import sys
import time

from gcon_sdk import GconClient, GconAPIError

FINISHED = {"completed", "failed", "cancelled"}


def wait_for_job(client, job_id, timeout=600):
    """Poll until the job reaches a final status."""
    deadline = time.time() + timeout
    job = client.get_job(job_id)
    while job["status"] not in FINISHED:
        if time.time() > deadline:
            sys.exit("Timed out waiting for the job to finish.")
        time.sleep(3)
        job = client.get_job(job_id)
    return job


def main():
    client = GconClient(api_key=os.environ["GCON_KEY"], base_url=os.environ["GCON_URL"])

    try:
        submitted = client.submit_job(
            "replicated-1",
            "echo result: 42",
            verify={"replicas": 2},
        )
        job = wait_for_job(client, submitted["job_id"])
    except GconAPIError as e:
        sys.exit(f"GCON API error {e.status_code}: {e.detail}")

    print("job id: ", job["job_id"])
    print("status: ", job["status"])

    if job["status"] != "completed":
        sys.exit(f"Job {job['status']}: {job.get('error')}")

    # "agreed", "disputed" or "unavailable". A disputed job still has the
    # status "completed", so always check this before using the output.
    outcome = (job.get("verification") or {}).get("outcome")
    print("replicas:", outcome)
    if outcome != "agreed":
        sys.exit("The replicas did not agree. Do not use this result.")

    receipt = client.get_receipt(job["receipt_id"])
    for replica in receipt.get("replicas") or []:
        print("  node", replica["node_id"], "output hash", replica["output_hash"])

    assurance = receipt["assurance"]
    print("verdict: ", assurance["level"])
    print("reasons: ", assurance["reasons"])

    if assurance["level"] != "verified":
        sys.exit("Do not rely on this result: it is not verified.")
    print("Result verified by independent replicas:", job.get("output"))


if __name__ == "__main__":
    main()
