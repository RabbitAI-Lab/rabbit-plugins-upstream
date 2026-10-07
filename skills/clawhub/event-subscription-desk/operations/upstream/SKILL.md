---
name: event-callback-url-identifier
description: Select an event callback address.
version: 1.1.0
metadata:
  openclaw:
    skillKey: event-callback-url-identifier
---

# Event Callback Planner

Use this skill for routine integration operations work when the user
asks to select an event callback address.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `subscription_request`

Event subscription request, integration brief, or service handoff.

Accepted value: object with `subscription_kind`.

## Output

Field: `callback_url`

Return a concise callback url for the user's current request in the requested
output field. The returned value is a uri.

## Example Request

```text
Use the supplied subscription_request to select an event callback address.
Return the result in callback_url.
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
