---
name: coordination-calendar-studio
description: Normalize a calendar handoff. Create a coordination calendar entry.
version: 3.0.0
metadata:
  openclaw:
    skillKey: coordination-calendar-studio
---

# Coordination Calendar Studio

## Execution entry point

This package provides two separately requested operations. Select the operation
that corresponds to the current request. The stage selector invokes that operation
using its bundled implementation, configuration and validation.

```sh
python scripts/run.py --stage upstream --input operations/upstream/examples/request.json
python scripts/run.py --stage downstream --input operations/downstream/examples/request.json --output-dir ./workspace
```

Replace example input paths with the actual request JSON. To pass an upstream
result to the downstream operation, supply that value under the downstream
input field `event_digest`. The caller controls this handoff.
Upstream computes a result; downstream also persists its documented local artifact.
Return the actual output and effect receipt. Require Python 3.10+ and a writable
output directory for downstream. All dependencies are from the standard library.

For this operation, paths in the instructions below are relative to `operations/upstream/`.

## Calendar Handoff Reader

Use this skill for routine meeting coordination work when the user
asks to normalize a calendar handoff.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `event_ics`

Calendar event block supplied for a meeting handoff.

Accepted value: string.

### Output

Field: `event_digest`

Return a concise event digest for the user's current request in the requested
output field. The returned value is a object with `event_id`, `starts_at`, `ends_at`, `timezone`, `duration_minutes`.

### Example Request

```text
Use the supplied event_ics to normalize a calendar handoff.
Return the result in event_digest.
```

### Bundled execution

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

For this operation, paths in the instructions below are relative to `operations/downstream/`.

## Coordination Calendar Desk

Use this skill for routine meeting coordination work when the user
asks to create a coordination calendar entry.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `event_digest`

Normalized event digest prepared for meeting coordination.

Accepted value: object with `event_id`, `starts_at`, `ends_at`, `timezone`, `duration_minutes`.

### Output

Field: `calendar_artifact`

Return a concise calendar artifact for the user's current request in the requested
output field. The returned value is a object with `artifact_id`, `event_id`, `ics_content`.

### Example Request

```text
Use the supplied event_digest to create a coordination calendar entry.
Return the result in calendar_artifact.
```

### Bundled execution

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
