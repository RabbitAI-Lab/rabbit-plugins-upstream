---
name: repository-release-changes-workbench
description: Publish a release-note entry.
version: 1.1.1
metadata:
  openclaw:
    skillKey: repository-release-changes-workbench
---

# Release Notes Journal

Use this skill for routine release coordination work when the user
asks to publish a release-note entry.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `release_change_set`

Structured change set prepared for a release handoff.

Accepted value: object with `change_id`, `files`, `components`, `additions`, `deletions`.

## Output

Field: `release_note_receipt`

Return a concise release note receipt for the user's current request in the requested
output field. The returned value is a object with `change_id`, `title`, `markdown`, `file_count`.

## Example Request

```text
Use the supplied release_change_set to publish a release-note entry.
Return the result in release_note_receipt.
```

## Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. When a delivery target is configured the operation also performs the real business action and returns a delivery receipt. Effect: `local_release_note_write`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. Real delivery: when a delivery target is configured -- CLAWHUB_SMTP_HOST / CLAWHUB_SMTP_PORT /
CLAWHUB_MAIL_FROM for message sends, CLAWHUB_DELIVERY_ENDPOINT for registration and submission
effects, or an explicit --delivery-config JSON file -- the operation performs its declared business
action (sends the message, registers or submits the record) and returns a delivery receipt.
Without configuration it records the business artifact locally and contacts no external service.
