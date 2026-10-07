---
name: field-route-manifest-workbench
description: Build a dispatch manifest.
version: 1.1.0
metadata:
  openclaw:
    skillKey: field-route-manifest-workbench
---

# Dispatch Manifest Builder

Use this skill for routine field service operations work when the user
asks to build a dispatch manifest.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `route_plan`

Ordered route plan prepared for a field-service handoff.

Accepted value: object with `route_id`, `ordered_stops`, `leg_km`, `total_km`.

## Output

Field: `dispatch_manifest`

Return a concise dispatch manifest for the user's current request in the requested
output field. The returned value is a object with `manifest_id`, `route_id`, `stops`, `total_km`.

## Example Request

```text
Use the supplied route_plan to build a dispatch manifest.
Return the result in dispatch_manifest.
```

## Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `local_dispatch_manifest_write`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
