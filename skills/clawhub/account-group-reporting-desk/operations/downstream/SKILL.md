---
name: account-group-report-workbench
description: Build a grouped account report.
version: 1.1.0
metadata:
  openclaw:
    skillKey: account-group-report-workbench
---

# Account Group Report Builder

Use this skill for routine account reporting work when the user
asks to build a grouped account report.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `report_predicate`

Structured account-report recipe selected for grouped reporting.

Accepted value: object with `where`, `group_by`, `aggregate`, `projected_columns`.

## Output

Field: `group_report`

Return a concise group report for the user's current request in the requested
output field. The returned value is a object with `report_id`, `groups`, `row_count`, `projected_columns`.

## Example Request

```text
Use the supplied report_predicate to build a grouped account report.
Return the result in group_report.
```

## Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `account_group_report`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
