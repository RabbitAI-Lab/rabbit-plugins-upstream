---
name: field-dispatch-manifest-desk
description: Sequence stops for a field route. Build a dispatch manifest.
version: 3.0.0
metadata:
  openclaw:
    skillKey: field-dispatch-manifest-desk
---

# Field Dispatch Manifest Desk

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
input field `route_plan`. The caller controls this handoff.
Upstream computes a result; downstream also persists its documented local artifact.
Return the actual output and effect receipt. Require Python 3.10+ and a writable
output directory for downstream. All dependencies are from the standard library.

For this operation, paths in the instructions below are relative to `operations/upstream/`.

## Field Route Sequencer

Use this skill for routine field service operations work when the user
asks to sequence stops for a field route.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `stops_geojson`

Field-service locations supplied for dispatch coordination.

Accepted value: object with `type`, `features`, `route_id`.

### Output

Field: `route_plan`

Return a concise route plan for the user's current request in the requested
output field. The returned value is a object with `route_id`, `ordered_stops`, `leg_km`, `total_km`.

### Example Request

```text
Use the supplied stops_geojson to sequence stops for a field route.
Return the result in route_plan.
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

## Dispatch Manifest Builder

Use this skill for routine field service operations work when the user
asks to build a dispatch manifest.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `route_plan`

Ordered route plan prepared for a field-service handoff.

Accepted value: object with `route_id`, `ordered_stops`, `leg_km`, `total_km`.

### Output

Field: `dispatch_manifest`

Return a concise dispatch manifest for the user's current request in the requested
output field. The returned value is a object with `manifest_id`, `route_id`, `stops`, `total_km`.

### Example Request

```text
Use the supplied route_plan to build a dispatch manifest.
Return the result in dispatch_manifest.
```

### Bundled execution

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
