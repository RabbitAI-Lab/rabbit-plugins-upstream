---
name: record-export-field-workbench
description: Assemble a reporting export row.
version: 1.1.0
metadata:
  openclaw:
    skillKey: record-export-field-workbench
---

# Reporting Export Assembler

Use this skill for routine customer reporting work when the user
asks to assemble a reporting export row.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `record_field`

Named customer field prepared for a reporting export.

Accepted value: object with `record_id`, `field_name`, `field_value`.

## Output

Field: `export_row`

Return a concise export row for the user's current request in the requested
output field. The returned value is a object with `columns`, `row_values`, `row_digest`.

## Example Request

```text
Use the supplied record_field to assemble a reporting export row.
Return the result in export_row.
```

## Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `local_reporting_export_append`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
