---
name: workspace-access-checklist-identifier
description: Compare workspace access lists.
version: 1.1.0
metadata:
  openclaw:
    skillKey: workspace-access-checklist-identifier
---

# Workspace Access Comparator

Use this skill for routine collaboration operations work when the user
asks to compare workspace access lists.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `sharing_acl_json`

Current and approved workspace membership lists.

Accepted value: object with `workspace_id`, `current_members`, `approved_members`.

## Output

Field: `access_delta`

Return a concise access delta for the user's current request in the requested
output field. The returned value is a object with `workspace_id`, `added`, `removed`, `role_changed`, `external_entries`.

## Example Request

```text
Use the supplied sharing_acl_json to compare workspace access lists.
Return the result in access_delta.
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
