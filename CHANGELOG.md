# Changelog

All notable changes to the GCON Python SDK are recorded here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/). The GCON API is in alpha, so interfaces may change.

## [Unreleased]

### Added

- `py.typed` marker, so type checkers use the SDK's type hints.
- Project metadata: authors, URLs, keywords and classifiers.
- `examples/` with a submit-and-check-receipt script and a replicated-job script.

## [1.0.0] - 2026-10-13

First release of the SDK in its own public repository.

### Added

- `GconClient`, a synchronous client for the GCON API, usable as a context manager.
- Jobs: `submit_job`, `get_job`, `list_jobs`, `get_job_attempts`, `cancel_job`, `retry_job` and `clear_jobs`.
- Job options: `resourced` jobs with `requires`, `staged` jobs with `stages`, replicated execution with `verify`, `dataset_artifacts`, `callback_url`, `client_reference` and `idempotency_key`.
- Workflows: `submit_workflow` and `list_workflows`.
- Receipts: `list_receipts` and `get_receipt`, including the assurance verdict.
- Artifacts and telemetry: `list_artifacts` and `get_telemetry_events`.
- Account and billing (read-only): `whoami`, `get_plan`, `get_pricing`, `get_usage`, `list_invoices` and `get_invoice`.
- Status methods: `get_cluster`, `get_health`, `get_metrics`, `list_nodes`, `get_node` and `get_node_enrollment_history`.
- `GconAPIError`, raised for any non-2xx response, with `status_code` and `detail`.

[Unreleased]: https://github.com/briton-data/gcon-sdk/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/briton-data/gcon-sdk/releases/tag/v1.0.0
