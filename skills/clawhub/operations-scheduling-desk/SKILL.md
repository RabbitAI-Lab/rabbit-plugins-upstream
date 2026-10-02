---
name: operations-scheduling-desk
description: Set service-class guidance for a task. Build an operations task schedule.
version: 3.0.0
metadata:
  openclaw:
    skillKey: operations-scheduling-desk
---

# Operations Scheduling Desk

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
input field `scheduling_guidance`. The caller controls this handoff.
Upstream computes a result; downstream also persists its documented local artifact.
Return the actual output and effect receipt. Require Python 3.10+ and a writable
output directory for downstream. All dependencies are from the standard library.

For this operation, paths in the instructions below are relative to `operations/upstream/`.

## Service Class Planner

Use this skill for routine operations scheduling work when the user
asks to set service-class guidance for a task.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `task_profile`

Task urgency, due date, and staffing profile.

Accepted value: object.

### Output

Field: `scheduling_guidance`

Return a concise scheduling guidance for the user's current request in the requested
output field. The returned value is a string.

### Example Request

```text
Use the supplied task_profile to set service-class guidance for a task.
Return the result in scheduling_guidance.
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

## Operations Schedule Builder

Use this skill for routine operations scheduling work when the user
asks to build an operations task schedule.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `scheduling_guidance`

Scheduling guidance available from the active operations session.

Accepted value: string or object with `service_class` or object with `cue`.

### Output

Field: `task_schedule`

Return a concise task schedule for the user's current request in the requested
output field. The returned value is a object with `ordered_task_ids`, `scheduled_task_id`, `scheduled_start`.

### Example Request

```text
Use the supplied scheduling_guidance to build an operations task schedule.
Return the result in task_schedule.
```

### Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `local_task_schedule`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
