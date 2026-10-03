---
name: request-review-routing-desk
description: Select a reviewer group. Register a request reviewer group.
version: 3.0.0
metadata:
  openclaw:
    skillKey: request-review-routing-desk
---

# Request Review Routing Desk

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
input field `reviewer_group`. The caller controls this handoff.
Upstream computes a result; downstream also persists its documented local artifact.
Return the actual output and effect receipt. Require Python 3.10+ and a writable
output directory for downstream. All dependencies are from the standard library.

For this operation, paths in the instructions below are relative to `operations/upstream/`.

## Approval Group Directory

Use this skill for routine request governance work when the user
asks to select a reviewer group.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `review_request`

Procurement request, access brief, or governance handoff.

Accepted value: object with `request_category`, `risk_level`.

### Output

Field: `reviewer_group`

Return a concise reviewer group for the user's current request in the requested
output field. The returned value is a string.

### Example Request

```text
Use the supplied review_request to select a reviewer group.
Return the result in reviewer_group.
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

## Request Review Register

Use this skill for routine request governance work when the user
asks to register a request reviewer group.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `reviewer_group`

Reviewer group selected for the request handoff.

Accepted value: string.

### Output

Field: `recorded_group`

Return a concise recorded group for the user's current request in the requested
output field. The returned value is a object with `review_request_id`, `reviewer_group`, `queue_name`, `due_hours`.

### Example Request

```text
Use the supplied reviewer_group to register a request reviewer group.
Return the result in recorded_group.
```

### Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `review_request_record`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
