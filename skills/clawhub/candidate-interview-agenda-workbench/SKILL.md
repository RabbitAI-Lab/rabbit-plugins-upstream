---
name: candidate-interview-agenda-workbench
description: Build an interview agenda.
version: 1.1.0
metadata:
  openclaw:
    skillKey: candidate-interview-agenda-workbench
---

# Interview Agenda Builder

Use this skill for routine recruiting operations work when the user
asks to build an interview agenda.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `interview_plan`

Role-focused topic plan prepared for an interview handoff.

Accepted value: object with `candidate_id`, `matched_required`, `missing_required`, `topics`.

## Output

Field: `agenda_artifact`

Return a concise agenda artifact for the user's current request in the requested
output field. The returned value is a object with `agenda_id`, `candidate_id`, `markdown`.

## Example Request

```text
Use the supplied interview_plan to build an interview agenda.
Return the result in agenda_artifact.
```

## Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `local_interview_agenda_render`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
