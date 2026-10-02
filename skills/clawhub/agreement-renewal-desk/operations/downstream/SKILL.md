---
name: agreement-renewal-schedule-workbench
description: Add entries to a renewal schedule.
version: 1.1.0
metadata:
  openclaw:
    skillKey: agreement-renewal-schedule-workbench
---

# Renewal Schedule Desk

Use this skill for routine agreement operations work when the user
asks to add entries to a renewal schedule.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `obligation_schedule`

Dated obligation entries prepared for a renewal handoff.

Accepted value: object with `agreement_id`, `obligations`.

## Output

Field: `schedule_receipt`

Return a concise schedule receipt for the user's current request in the requested
output field. The returned value is a object with `schedule_id`, `rows`.

## Example Request

```text
Use the supplied obligation_schedule to add entries to a renewal schedule.
Return the result in schedule_receipt.
```

## Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `local_renewal_schedule_append`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
