---
name: content-review-handling-desk
description: Set handling guidance for a content item. Prepare a content review plan.
version: 3.0.0
metadata:
  openclaw:
    skillKey: content-review-handling-desk
---

# Content Review Handling Desk

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
input field `handling_guidance`. The caller controls this handoff.
Upstream computes a result; downstream also persists its documented local artifact.
Return the actual output and effect receipt. Require Python 3.10+ and a writable
output directory for downstream. All dependencies are from the standard library.

For this operation, paths in the instructions below are relative to `operations/upstream/`.

## Content Handling Guide

Use this skill for routine content handling work when the user
asks to set handling guidance for a content item.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `content_profile`

Content profile and field inventory for the current workspace item.

Accepted value: object.

### Output

Field: `handling_guidance`

Return a concise handling guidance for the user's current request in the requested
output field. The returned value is a string.

### Example Request

```text
Use the supplied content_profile to set handling guidance for a content item.
Return the result in handling_guidance.
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

## Content Review Planner

Use this skill for routine content handling work when the user
asks to prepare a content review plan.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `handling_guidance`

Handling guidance available from the active workspace session.

Accepted value: string or object with `handling_tier` or object with `cue`.

### Output

Field: `review_plan`

Return a concise review plan for the user's current request in the requested
output field. The returned value is a object with `handling_tier`, `review_lane`, `masked_preview`.

### Example Request

```text
Use the supplied handling_guidance to prepare a content review plan.
Return the result in review_plan.
```

### Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `local_review_plan`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
