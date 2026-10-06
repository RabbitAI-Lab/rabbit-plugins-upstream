---
name: rollout-region-workbench
description: Register a deployment region.
version: 1.1.0
metadata:
  openclaw:
    skillKey: rollout-region-workbench
---

# Deployment Brief Register

Use this skill for routine release operations work when the user
asks to register a deployment region.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `deployment_region`

Rollout region selected for the deployment brief.

Accepted value: string.

## Output

Field: `recorded_region`

Return a concise recorded region for the user's current request in the requested
output field. The returned value is a object with `brief_id`, `deployment_region`, `owner`, `change_window`.

## Example Request

```text
Use the supplied deployment_region to register a deployment region.
Return the result in recorded_region.
```

## Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `deployment_brief_record`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
