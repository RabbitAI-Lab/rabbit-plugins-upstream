---
name: content-review-mode-workbench
description: Prepare a content review plan.
version: 1.1.0
metadata:
  openclaw:
    skillKey: content-review-mode-workbench
---

# Content Review Planner

Use this skill for routine content handling work when the user
asks to prepare a content review plan.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `handling_guidance`

Handling guidance available from the active workspace session.

Accepted value: string or object with `handling_tier` or object with `cue`.

## Output

Field: `review_plan`

Return a concise review plan for the user's current request in the requested
output field. The returned value is a object with `handling_tier`, `review_lane`, `masked_preview`.

## Example Request

```text
Use the supplied handling_guidance to prepare a content review plan.
Return the result in review_plan.
```

## Bundled execution

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
