---
name: account-group-reporting-desk
description: Compose an account grouping recipe. Build a grouped account report.
version: 3.0.0
metadata:
  openclaw:
    skillKey: account-group-reporting-desk
---

# Account Group Reporting Desk

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
input field `report_predicate`. The caller controls this handoff.
Upstream computes a result; downstream also persists its documented local artifact.
Return the actual output and effect receipt. Require Python 3.10+ and a writable
output directory for downstream. All dependencies are from the standard library.

For this operation, paths in the instructions below are relative to `operations/upstream/`.

## Account Report Recipe Planner

Use this skill for routine account reporting work when the user
asks to compose an account grouping recipe.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `report_request`

Account segment, grouping field, measure, calculation, and requested report columns.

Accepted value: object with `segment`, `group_by`, `measure`, `calculation`, `columns`.

### Output

Field: `report_predicate`

Return a concise report predicate for the user's current request in the requested
output field. The returned value is a object with `where`, `group_by`, `aggregate`, `projected_columns`.

### Example Request

```text
Use the supplied report_request to compose an account grouping recipe.
Return the result in report_predicate.
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

## Account Group Report Builder

Use this skill for routine account reporting work when the user
asks to build a grouped account report.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `report_predicate`

Structured account-report recipe selected for grouped reporting.

Accepted value: object with `where`, `group_by`, `aggregate`, `projected_columns`.

### Output

Field: `group_report`

Return a concise group report for the user's current request in the requested
output field. The returned value is a object with `report_id`, `groups`, `row_count`, `projected_columns`.

### Example Request

```text
Use the supplied report_predicate to build a grouped account report.
Return the result in group_report.
```

### Bundled execution

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
