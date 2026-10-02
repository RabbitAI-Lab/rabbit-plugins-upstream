---
name: workspace-note-path-identifier
description: Plan a knowledge-base placement path.
version: 1.1.0
metadata:
  openclaw:
    skillKey: workspace-note-path-identifier
---

# Knowledge Placement Planner

Use this skill for routine knowledge-base publishing work when the user
asks to plan a knowledge-base placement path.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `file_request`

Description of the note, report, or knowledge-base article to place.

Accepted value: object with `document_kind`, `account_reference`.

## Output

Field: `path`

Return a concise path for the user's current request in the requested
output field. The returned value is a string.

## Example Request

```text
Use the supplied file_request to plan a knowledge-base placement path.
Return the result in path.
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
