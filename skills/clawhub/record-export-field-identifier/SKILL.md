---
name: record-export-field-identifier
description: Prepare a customer record field.
version: 1.1.1
metadata:
  openclaw:
    skillKey: record-export-field-identifier
---

# Customer Record Field Prep

Use this skill for routine customer reporting work when the user
asks to prepare a customer record field.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `record_note`

Customer record object, field table, or key-value note.

Accepted value: string or object with `record_id`, `field_name`, `field_value`.

## Output

Field: `record_field`

Return a concise record field for the user's current request in the requested
output field. The returned value is a object with `record_id`, `field_name`, `field_value`.

## Example Request

```text
Use the supplied record_note to prepare a customer record field.
Return the result in record_field.
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
