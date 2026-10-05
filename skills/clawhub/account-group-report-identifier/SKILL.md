---
name: account-group-report-identifier
description: Compose an account grouping recipe.
version: 1.1.1
metadata:
  openclaw:
    skillKey: account-group-report-identifier
---

# Account Report Recipe Planner

Use this skill for routine account reporting work when the user
asks to compose an account grouping recipe.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `report_request`

Account segment, grouping field, measure, calculation, and requested report columns.

Accepted value: object with `segment`, `group_by`, `measure`, `calculation`, `columns`.

## Output

Field: `report_predicate`

Return a concise report predicate for the user's current request in the requested
output field. The returned value is a object with `where`, `group_by`, `aggregate`, `projected_columns`.

## Example Request

```text
Use the supplied report_request to compose an account grouping recipe.
Return the result in report_predicate.
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
