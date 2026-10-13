# Security Policy

## Reporting a vulnerability

If you find a security vulnerability in the GCON SDK or the GCON service, please **do not open a public GitHub issue**. Report it privately instead.

Email **contact@gcon.network** with the subject "Security", and include:

- A description of the vulnerability
- Steps to reproduce it
- The potential impact
- A suggested fix, if you have one

We will acknowledge your report within 48 hours and send updates every 5 days. We will work with you on a fix and a responsible disclosure timeline.

Please do not include real API keys or customer data in your report.

## Using the SDK safely

**API keys**

- Store keys in environment variables or a secrets manager.
- Use a different key for each environment and application.
- Rotate keys periodically, and revoke any key you suspect has leaked.
- Never commit keys to version control, and never share them over email or chat.
- Do not print or log keys, including in error reports.

**Connections**

- Point `base_url` at an `https://` address.

**Results**

- Act on a result only when its receipt has `assurance["level"] == "verified"`.
- For jobs where a wrong answer is costly, ask for replicated execution with `verify={"replicas": 2}`.
