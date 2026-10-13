"""Submit a job, wait for it to finish, and check its receipt.

Usage:
    export GCON_URL="<your GCON service URL>"
    export GCON_KEY="gcon_..."
    python examples/01_submit_and_check_receipt.py
"""
import os
import sys
import time

from gcon_sdk import GconClient, GconAPIError

FINISHED = {"completed", "failed", "cancelled"}


def wait_for_job(client, job_id, timeout=300):
    """Poll until the job reaches a final status."""
    deadline = time.time() + timeout
    job = client.get_job(job_id)
    while job["status"] not in FINISHED:
        if time.time() > deadline:
            sys.exit("Timed out waiting for the job to finish.")
        time.sleep(2)
        job = client.get_job(job_id)
    return job


def main():
    client = GconClient(api_key=os.environ["GCON_KEY"], base_url=os.environ["GCON_URL"])

    try:
        # "hello-1" is only your own label. GCON returns the real job id.
        submitted = client.submit_job("hello-1", "echo hello from GCON")
        job = wait_for_job(client, submitted["job_id"])
    except GconAPIError as e:
        sys.exit(f"GCON API error {e.status_code}: {e.detail}")

    print("job id:  ", job["job_id"])
    print("status:  ", job["status"])
    print("output:  ", job.get("output"))

    if job["status"] != "completed":
        sys.exit(f"Job {job['status']}: {job.get('error')}")

    receipt_id = job.get("receipt_id")
    if not receipt_id:
        sys.exit("The job has no receipt yet. Try again shortly.")

    receipt = client.get_receipt(receipt_id)
    assurance = receipt["assurance"]
    print("receipt: ", receipt["receipt_id"])
    print("verdict: ", assurance["level"])
    print("reasons: ", assurance["reasons"])

    # Act on a result only when the verdict is "verified".
    if assurance["level"] != "verified":
        sys.exit("Do not rely on this result: it is not verified.")
    print("Result verified.")


if __name__ == "__main__":
    main()
