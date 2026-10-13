# Contributing to the GCON SDK

Thank you for helping improve the GCON Python SDK. This repository contains the SDK (`sdk/`), its documentation and the project README.

## Before you start

Open an issue before starting any large change, so we can agree on the approach first. Small fixes such as typos, docstrings and clear bugs can go straight to a pull request.

Do not report security problems in a public issue. See [SECURITY.md](SECURITY.md).

## Set up

You need Python 3.8 or newer and Git.

```bash
git clone <this repository>
cd <this repository>
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e sdk/
```

## Making a change

1. Fork the repository and create a branch with a descriptive name, such as `fix/retry-error-message`.
2. Keep the change small and focused. One pull request should do one thing.
3. Keep `requests` as the only dependency, and keep the code working on Python 3.8.
4. Follow the existing style: type hints on public methods, a short docstring on each public method, and lines of at most 100 characters.
5. Update `sdk/README.md` if you change how the SDK is used.
6. Check your change against a real GCON account and say how you tested it in the pull request.

### Commit messages

Use the form `type(scope): short summary`, for example:

```
fix(client): raise GconAPIError for empty error responses
docs(readme): clarify idempotency keys
```

Common types are `feat`, `fix`, `docs`, `refactor` and `chore`.

## Pull requests

Describe the problem, what you changed, and how you tested it. A maintainer will review it and may ask for changes.

## Reporting bugs

Include:

- The SDK version and your Python version
- What you did, what you expected, and what happened
- The `GconAPIError` status code and message, if there was one

Remove API keys and any private data before you post.

## Suggesting features

Open an issue that describes the problem you want to solve and how you would like it to work. The API is in alpha, so some features may be declined or delayed.

## Code of conduct

Be respectful, inclusive and constructive. Harassment, discrimination, hate speech and deliberate disruption are not accepted. To report a violation, email contact@gcon.network.
