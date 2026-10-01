---
name: calendar-coordination-entry-workbench
description: Create a coordination calendar entry.
version: 1.1.0
metadata:
  openclaw:
    skillKey: calendar-coordination-entry-workbench
---

# Coordination Calendar Desk

Use this skill for routine meeting coordination work when the user
asks to create a coordination calendar entry.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `event_digest`

Normalized event digest prepared for meeting coordination.

Accepted value: object with `event_id`, `starts_at`, `ends_at`, `timezone`, `duration_minutes`.

## Output

Field: `calendar_artifact`

Return a concise calendar artifact for the user's current request in the requested
output field. The returned value is a object with `artifact_id`, `event_id`, `ics_content`.

## Example Request

```text
Use the supplied event_digest to create a coordination calendar entry.
Return the result in calendar_artifact.
```

## Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `local_calendar_artifact_create`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
