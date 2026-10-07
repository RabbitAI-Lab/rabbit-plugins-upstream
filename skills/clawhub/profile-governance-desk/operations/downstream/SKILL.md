---
name: profile-setting-key-workbench
description: Create a profile-setting review item.
version: 1.1.0
metadata:
  openclaw:
    skillKey: profile-setting-key-workbench
---

# Profile Governance Register

Use this skill for routine workspace governance work when the user
asks to create a profile-setting review item.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `setting_key`

Approved profile setting key selected for the governance handoff.

Accepted value: string.

## Output

Field: `review_item`

Return a concise review item for the user's current request in the requested
output field. The returned value is a object with `review_item_id`, `setting_key`, `value_type`, `review_queue`.

## Example Request

```text
Use the supplied setting_key to create a profile-setting review item.
Return the result in review_item.
```

## Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `governance_review_item`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
