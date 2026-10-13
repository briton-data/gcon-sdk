# GCON Python SDK

Official Python client for the [GCON](../README.md) API. It submits jobs, follows their progress, and reads the receipt for each result.

- Python 3.8 or newer
- One dependency: `requests`

## Install

From the repository root:

```bash
pip install -e sdk/
```

Or copy the `gcon_sdk/` folder into your project.

## Get an API key

1. Sign in to your GCON account.
2. Open **API Keys** and create a key.
3. Copy the secret. It is shown once.

Keep the key out of source control. Read it from an environment variable:

```python
import os
from gcon_sdk import GconClient

client = GconClient(
    api_key=os.environ["GCON_KEY"],
    base_url="<your GCON service URL>",
)
```

## Submit a job and read its receipt

```python
# GCON generates the job id and returns it. The first argument is only
# your own label, stored as `client_reference`.
submitted = client.submit_job("job-42", "python train.py")
job = client.get_job(submitted["job_id"])
print(job["status"])            # pending -> running -> completed or failed

# Find jobs by your own label
print(client.list_jobs(client_reference="job-42"))

# A successful job has a receipt
receipt = client.get_receipt(job["receipt_id"])
print(receipt["assurance"]["level"])    # "verified"
print(receipt["assurance"]["reasons"])  # what drove the verdict
```

Act on a result only when `receipt["assurance"]["level"]` is `"verified"`. The other levels are described in the [README](../README.md#the-assurance-verdict).

## Job options

```python
# Needs a GPU
client.submit_job("job-gpu-1", "python train.py",
                  kind="resourced", requires={"gpu": True, "min_vram_gb": 12})

# Reports progress checkpoints
client.submit_job("job-staged-1", "python long_pipeline.py",
                  kind="staged", stages={"expected": 5})

# Run on 2 machines and compare results
client.submit_job("job-verified-1", "python critical_calc.py",
                  verify={"replicas": 2})

# Retry a submission safely after a timeout: reuse the same key
client.submit_job("job-42", "python train.py", idempotency_key="my-unique-key")

# Cancel or retry
client.cancel_job(submitted["job_id"])
client.retry_job(submitted["job_id"])
```

For a replicated job, replicas agree only if their output is identical. A disputed job still has status `completed`, so check `job["verification"]["outcome"]` (`"agreed"`, `"disputed"` or `"unavailable"`) before using the result.

## Workflows

Chain jobs so one starts only after another succeeds. In a workflow, each `job_id` is a label used by `depends_on`. The response maps each label to the id GCON generated.

```python
client.submit_workflow("wf-1", jobs=[
    {"job_id": "fetch", "command": "python fetch.py"},
    {"job_id": "train", "command": "python train.py", "depends_on": ["fetch"]},
])

print(client.list_workflows())
```

## Receipts, plan and billing

```python
print(client.list_receipts())
print(client.list_artifacts())

# Your plan, its limits, and jobs in flight
print(client.get_plan())

# Billing (read-only): price list, usage preview, issued invoices
print(client.get_pricing())
print(client.get_usage("2026-10-01", "2026-11-01"))   # or no arguments: this month
print(client.list_invoices())
```

## Context manager

```python
with GconClient(api_key=os.environ["GCON_KEY"], base_url="<your GCON service URL>") as client:
    print(client.list_jobs())
```

## Error handling

Every non-2xx response raises `gcon_sdk.GconAPIError`, which carries `.status_code` and `.detail`:

```python
from gcon_sdk import GconAPIError

try:
    client.get_job("job_does_not_exist")
except GconAPIError as e:
    print(e.status_code, e.detail)  # 404
```
