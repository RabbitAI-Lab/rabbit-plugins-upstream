---
name: workspace-access-review-desk
description: Compare workspace access lists. Create an access review checklist.
version: 3.0.0
metadata:
  openclaw:
    skillKey: workspace-access-review-desk
---

# Workspace Access Review Desk

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
input field `access_delta`. The caller controls this handoff.
Upstream computes a result; downstream also persists its documented local artifact.
Return the actual output and effect receipt. Require Python 3.10+ and a writable
output directory for downstream. All dependencies are from the standard library.

For this operation, paths in the instructions below are relative to `operations/upstream/`.

## Workspace Access Comparator

Use this skill for routine collaboration operations work when the user
asks to compare workspace access lists.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `sharing_acl_json`

Current and approved workspace membership lists.

Accepted value: object with `workspace_id`, `current_members`, `approved_members`.

### Output

Field: `access_delta`

Return a concise access delta for the user's current request in the requested
output field. The returned value is a object with `workspace_id`, `added`, `removed`, `role_changed`, `external_entries`.

### Example Request

```text
Use the supplied sharing_acl_json to compare workspace access lists.
Return the result in access_delta.
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

## Access Review Checklist

Use this skill for routine collaboration operations work when the user
asks to create an access review checklist.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `access_delta`

Workspace membership differences prepared for collaboration follow-up.

Accepted value: object with `workspace_id`, `added`, `removed`, `role_changed`, `external_entries`.

### Output

Field: `checklist_artifact`

Return a concise checklist artifact for the user's current request in the requested
output field. The returned value is a object with `checklist_id`, `workspace_id`, `items`.

### Example Request

```text
Use the supplied access_delta to create an access review checklist.
Return the result in checklist_artifact.
```

### Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `local_access_checklist_write`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
