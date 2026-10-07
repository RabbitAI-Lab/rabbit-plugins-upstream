---
name: referral-handoff-packet-identifier
description: Prepare a referral handoff digest.
version: 1.1.1
metadata:
  openclaw:
    skillKey: referral-handoff-packet-identifier
---

# Referral Handoff Reader

Use this skill for routine care coordination work when the user
asks to prepare a referral handoff digest.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `referral_form_json`

Referral form supplied for a care coordination handoff.

Accepted value: object with `referral_id`, `specialty`, `urgency`, `requested_window`.

## Output

Field: `referral_digest`

Return a concise referral digest for the user's current request in the requested
output field. The returned value is a object with `referral_id`, `specialty`, `urgency_band`, `requested_window`.

## Example Request

```text
Use the supplied referral_form_json to prepare a referral handoff digest.
Return the result in referral_digest.
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
