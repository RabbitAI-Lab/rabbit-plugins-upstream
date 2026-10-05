---
name: invoice-match-threshold-identifier
description: Derive an invoice-match threshold.
version: 1.1.1
metadata:
  openclaw:
    skillKey: invoice-match-threshold-identifier
---

# Reconciliation Threshold Planner

Use this skill for routine invoice reconciliation work when the user
asks to derive an invoice-match threshold.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `reconciliation_rule`

Permitted variance for an invoice reconciliation workflow.

Accepted value: object with `allowed_variance`.

## Output

Field: `match_threshold`

Return a concise match threshold for the user's current request in the requested
output field. The returned value is a number.

## Example Request

```text
Use the supplied reconciliation_rule to derive an invoice-match threshold.
Return the result in match_threshold.
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
