---
name: interview-planning-studio
description: Map candidate skills to an interview plan. Build an interview agenda.
version: 3.0.0
metadata:
  openclaw:
    skillKey: interview-planning-studio
---

# Interview Planning Studio

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
input field `interview_plan`. The caller controls this handoff.
Upstream computes a result; downstream also persists its documented local artifact.
Return the actual output and effect receipt. Require Python 3.10+ and a writable
output directory for downstream. All dependencies are from the standard library.

For this operation, paths in the instructions below are relative to `operations/upstream/`.

## Candidate Skills Mapper

Use this skill for routine recruiting operations work when the user
asks to map candidate skills to an interview plan.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `candidate_profile_yaml`

Candidate and role profile supplied for interview planning.

Accepted value: string or object with `candidate_id`, `profile`, `role`.

### Output

Field: `interview_plan`

Return a concise interview plan for the user's current request in the requested
output field. The returned value is a object with `candidate_id`, `matched_required`, `missing_required`, `topics`.

### Example Request

```text
Use the supplied candidate_profile_yaml to map candidate skills to an interview plan.
Return the result in interview_plan.
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

## Interview Agenda Builder

Use this skill for routine recruiting operations work when the user
asks to build an interview agenda.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `interview_plan`

Role-focused topic plan prepared for an interview handoff.

Accepted value: object with `candidate_id`, `matched_required`, `missing_required`, `topics`.

### Output

Field: `agenda_artifact`

Return a concise agenda artifact for the user's current request in the requested
output field. The returned value is a object with `agenda_id`, `candidate_id`, `markdown`.

### Example Request

```text
Use the supplied interview_plan to build an interview agenda.
Return the result in agenda_artifact.
```

### Bundled execution

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
