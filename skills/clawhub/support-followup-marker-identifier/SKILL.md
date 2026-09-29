---
name: support-followup-marker-identifier
description: Prepare a support intake digest.
version: 1.1.0
metadata:
  openclaw:
    skillKey: support-followup-marker-identifier
---

# Support Intake Digest

Use this skill for routine support operations work when the user
asks to prepare a support intake digest.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `snippet`

Support intake message with case, priority, and subject fields.

Accepted value: string.

## Output

Field: `support_digest`

Return a concise support digest for the user's current request in the requested
output field. The returned value is a object with `case_id`, `priority`, `subject`, `follow_up_category`.

## Example Request

```text
Use the supplied snippet to prepare a support intake digest.
Return the result in support_digest.
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
