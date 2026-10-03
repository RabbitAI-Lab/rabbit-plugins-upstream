---
name: export-confirmation-style-workbench
description: Create a delivery acknowledgement.
version: 1.1.0
metadata:
  openclaw:
    skillKey: export-confirmation-style-workbench
---

# Delivery Receipt Desk

Use this skill for routine delivery acknowledgement work when the user
asks to create a delivery acknowledgement.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `acknowledgement_guidance`

Acknowledgement guidance available from the active delivery session.

Accepted value: string or object with `acknowledge_after` or object with `cue`.

## Output

Field: `confirmation_result`

Return a concise confirmation result for the user's current request in the requested
output field. The returned value is a object with `operation_id`, `confirmation_status`, `receipt_created`.

## Example Request

```text
Use the supplied acknowledgement_guidance to create a delivery acknowledgement.
Return the result in confirmation_result.
```

## Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `local_confirmation_receipt`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
