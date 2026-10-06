---
name: metric-stakeholder-digest-identifier
description: Calculate a metric trend summary.
version: 1.1.1
metadata:
  openclaw:
    skillKey: metric-stakeholder-digest-identifier
---

# Metric Trend Calculator

Use this skill for routine analytics reporting work when the user
asks to calculate a metric trend summary.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `metric_series_csv`

Metric series supplied for an operating review.

Accepted value: string.

## Output

Field: `metric_digest`

Return a concise metric digest for the user's current request in the requested
output field. The returned value is a object with `metric_id`, `first`, `latest`, `delta`, `mean`, `direction`.

## Example Request

```text
Use the supplied metric_series_csv to calculate a metric trend summary.
Return the result in metric_digest.
```

## Bundled execution

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
local records are included for reproducibility. This package computes its declared output without external communication or persistence.
