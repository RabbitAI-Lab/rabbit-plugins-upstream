---
name: profile-setting-key-identifier
description: Choose a profile setting key.
version: 1.1.1
metadata:
  openclaw:
    skillKey: profile-setting-key-identifier
---

# Profile Setting Directory

Use this skill for routine workspace governance work when the user
asks to choose a profile setting key.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `profile_request`

Workspace request category used to locate the relevant profile setting.

Accepted value: object with `request_kind`.

## Output

Field: `setting_key`

Return a concise setting key for the user's current request in the requested
output field. The returned value is a string.

## Example Request

```text
Use the supplied profile_request to choose a profile setting key.
Return the result in setting_key.
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
