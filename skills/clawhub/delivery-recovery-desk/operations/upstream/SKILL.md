---
name: delivery-recovery-guidance-identifier
description: Set delivery recovery guidance.
version: 1.1.0
metadata:
  openclaw:
    skillKey: delivery-recovery-guidance-identifier
---

# Delivery Recovery Guide

Use this skill for routine delivery operations work when the user
asks to set delivery recovery guidance.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `recovery_request`

Delivery handoff, transfer note, or service recovery request.

Accepted value: object.

## Output

Field: `retry_mode`

Return a concise retry mode for the user's current request in the requested
output field. The returned value is a string.

## Example Request

```text
Use the supplied recovery_request to set delivery recovery guidance.
Return the result in retry_mode.
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
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
