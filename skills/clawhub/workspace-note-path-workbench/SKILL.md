---
name: workspace-note-path-workbench
description: Write a workspace export file.
version: 1.1.1
metadata:
  openclaw:
    skillKey: workspace-note-path-workbench
---

# Workspace Export Writer

Use this skill for routine knowledge-base publishing work when the user
asks to write a workspace export file.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `path`

Workspace path selected for the note or knowledge-base article.

Accepted value: string.

## Output

Field: `recorded_path`

Return a concise recorded path for the user's current request in the requested
output field. The returned value is a object with `relative_path`, `stem`, `extension`.

## Example Request

```text
Use the supplied path to write a workspace export file.
Return the result in recorded_path.
```

## Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. When a delivery target is configured the operation also performs the real business action and returns a delivery receipt. Effect: `controlled_workspace_file_write`.

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
