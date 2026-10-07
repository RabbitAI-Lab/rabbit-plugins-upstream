---
name: stakeholder-metrics-studio
description: Calculate a metric trend summary. Build a stakeholder metric digest.
version: 3.0.0
metadata:
  openclaw:
    skillKey: stakeholder-metrics-studio
---

# Stakeholder Metrics Studio

## Execution entry point

This package provides two separately requested operations. Select the operation
that corresponds to the current request. The stage selector invokes that operation
using its bundled implementation, configuration and validation.

```sh
python scripts/run.py --stage upstream --input operations/upstream/examples/request.json
python scripts/run.py --stage downstream --input operations/downstream/examples/request.json --output-dir ./workspace
```

Replace example input paths with the actual request JSON. To pass an upstream
result to the downstream operation, supply that value under the downstream
input field `metric_digest`. The caller controls this handoff.
Upstream computes a result; downstream also persists its documented local artifact.
Return the actual output and effect receipt. Require Python 3.10+ and a writable
output directory for downstream. All dependencies are from the standard library.

For this operation, paths in the instructions below are relative to `operations/upstream/`.

## Metric Trend Calculator

Use this skill for routine analytics reporting work when the user
asks to calculate a metric trend summary.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `metric_series_csv`

Metric series supplied for an operating review.

Accepted value: string.

### Output

Field: `metric_digest`

Return a concise metric digest for the user's current request in the requested
output field. The returned value is a object with `metric_id`, `first`, `latest`, `delta`, `mean`, `direction`.

### Example Request

```text
Use the supplied metric_series_csv to calculate a metric trend summary.
Return the result in metric_digest.
```

### Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json
```

This operation only computes and returns its output; it does not persist a business artifact.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.

For this operation, paths in the instructions below are relative to `operations/downstream/`.

## Stakeholder Metric Digest

Use this skill for routine analytics reporting work when the user
asks to build a stakeholder metric digest.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `metric_digest`

Structured metric summary prepared for stakeholder reporting.

Accepted value: object with `metric_id`, `first`, `latest`, `delta`, `mean`, `direction`.

### Output

Field: `digest_artifact`

Return a concise digest artifact for the user's current request in the requested
output field. The returned value is a object with `digest_id`, `metric_id`, `html`.

### Example Request

```text
Use the supplied metric_digest to build a stakeholder metric digest.
Return the result in digest_artifact.
```

### Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `local_metric_digest_render`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
