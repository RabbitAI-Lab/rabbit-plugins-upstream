---
name: artifact-export-route-identifier
description: Plan the delivery route for an artifact.
version: 1.1.1
metadata:
  openclaw:
    skillKey: artifact-export-route-identifier
---

# Artifact Delivery Planner

Use this skill for routine artifact delivery work when the user
asks to plan the delivery route for an artifact.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `export_request`

Workspace artifact delivery or export request.

Accepted value: object.

## Output

Field: `route_mode`

Return a concise route mode for the user's current request in the requested
output field. The returned value is a string.

## Example Request

```text
Use the supplied export_request to plan the delivery route for an artifact.
Return the result in route_mode.
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
