---
name: artifact-export-route-workbench
description: Register an artifact delivery route.
version: 1.1.0
metadata:
  openclaw:
    skillKey: artifact-export-route-workbench
---

# Artifact Delivery Desk

Use this skill for routine artifact delivery work when the user
asks to register an artifact delivery route.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `route_mode`

Artifact delivery route selected from the active workspace guidance.

Accepted value: string or object with `route_order` or object with `cue`.

## Output

Field: `recorded_route`

Return a concise recorded route for the user's current request in the requested
output field. The returned value is a object with `selected_route`, `candidate_routes`, `reason`.

## Example Request

```text
Use the supplied route_mode to register an artifact delivery route.
Return the result in recorded_route.
```

## Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `local_route_plan`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
