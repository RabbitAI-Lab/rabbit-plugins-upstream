---
name: service-capacity-window-identifier
description: Select a service capacity window.
version: 1.1.0
metadata:
  openclaw:
    skillKey: service-capacity-window-identifier
---

# Service Capacity Window Planner

Use this skill for routine service capacity planning work when the user
asks to select a service capacity window.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `capacity_request`

Date, time, and timezone requested for a service capacity reservation.

Accepted value: object with `date`, `time`, `timezone`.

## Output

Field: `capacity_window`

Return a concise capacity window for the user's current request in the requested
output field. The returned value is a date-time.

## Example Request

```text
Use the supplied capacity_request to select a service capacity window.
Return the result in capacity_window.
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
