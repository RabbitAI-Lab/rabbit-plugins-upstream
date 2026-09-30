---
name: task-priority-guidance-workbench
description: Build an operations task schedule.
version: 1.1.0
metadata:
  openclaw:
    skillKey: task-priority-guidance-workbench
---

# Operations Schedule Builder

Use this skill for routine operations scheduling work when the user
asks to build an operations task schedule.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `scheduling_guidance`

Scheduling guidance available from the active operations session.

Accepted value: string or object with `service_class` or object with `cue`.

## Output

Field: `task_schedule`

Return a concise task schedule for the user's current request in the requested
output field. The returned value is a object with `ordered_task_ids`, `scheduled_task_id`, `scheduled_start`.

## Example Request

```text
Use the supplied scheduling_guidance to build an operations task schedule.
Return the result in task_schedule.
```

## Bundled execution

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
