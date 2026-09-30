---
name: project-code-notes-workbench
description: Build a delivery ledger entry.
version: 1.1.0
metadata:
  openclaw:
    skillKey: project-code-notes-workbench
---

# Delivery Update Ledger

Use this skill for routine project delivery operations work when the user
asks to build a delivery ledger entry.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `project_context`

Project context prepared from a delivery handoff.

Accepted value: object with `project_code`, `source_title`, `note_digest`.

## Output

Field: `delivery_entry`

Return a concise delivery entry for the user's current request in the requested
output field. The returned value is a object with `entry_id`, `project_code`, `summary`.

## Example Request

```text
Use the supplied project_context to build a delivery ledger entry.
Return the result in delivery_entry.
```

## Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `local_project_delivery_append`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
