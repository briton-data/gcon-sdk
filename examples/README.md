# Examples

Short scripts that show the SDK end to end. Each one submits a real job, so they need a GCON account and an API key.

| Script | What it shows |
|---|---|
| [`01_submit_and_check_receipt.py`](01_submit_and_check_receipt.py) | Submit a job, wait for it to finish, read its receipt and act only on a `verified` verdict. |
| [`02_replicated_job.py`](02_replicated_job.py) | Run a job on two independent nodes, check that the replicas agree, then check the receipt verdict. |

## Before you run them

1. Create an account and an API key. See [Get an API key](../sdk/README.md#get-an-api-key).
2. Install the SDK from the repository root:

   ```bash
   pip install -e sdk/
   ```

3. Set your service URL and API key. Keep the key out of source control.

   ```bash
   export GCON_URL="<your GCON service URL>"
   export GCON_KEY="gcon_..."
   ```

   On Windows PowerShell:

   ```powershell
   $env:GCON_URL = "<your GCON service URL>"
   $env:GCON_KEY = "gcon_..."
   ```

## Run

```bash
python examples/01_submit_and_check_receipt.py
python examples/02_replicated_job.py
```

Each script exits with an error unless the result is `verified`. Jobs may be billed according to your plan.
