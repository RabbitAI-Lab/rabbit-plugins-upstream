---
name: customer-report-export-desk
description: Prepare a customer record field. Assemble a reporting export row.
version: 3.0.0
metadata:
  openclaw:
    skillKey: customer-report-export-desk
---

# Customer Report Export Desk

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
input field `record_field`. The caller controls this handoff.
Upstream computes a result; downstream also persists its documented local artifact.
Return the actual output and effect receipt. Require Python 3.10+ and a writable
output directory for downstream. All dependencies are from the standard library.

For this operation, paths in the instructions below are relative to `operations/upstream/`.

## Customer Record Field Prep

Use this skill for routine customer reporting work when the user
asks to prepare a customer record field.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `record_note`

Customer record object, field table, or key-value note.

Accepted value: string or object with `record_id`, `field_name`, `field_value`.

### Output

Field: `record_field`

Return a concise record field for the user's current request in the requested
output field. The returned value is a object with `record_id`, `field_name`, `field_value`.

### Example Request

```text
Use the supplied record_note to prepare a customer record field.
Return the result in record_field.
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

## Reporting Export Assembler

Use this skill for routine customer reporting work when the user
asks to assemble a reporting export row.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `record_field`

Named customer field prepared for a reporting export.

Accepted value: object with `record_id`, `field_name`, `field_value`.

### Output

Field: `export_row`

Return a concise export row for the user's current request in the requested
output field. The returned value is a object with `columns`, `row_values`, `row_digest`.

### Example Request

```text
Use the supplied record_field to assemble a reporting export row.
Return the result in export_row.
```

### Bundled execution

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
