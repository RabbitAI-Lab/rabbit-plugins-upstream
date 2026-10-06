---
name: candidate-interview-agenda-identifier
description: Map candidate skills to an interview plan.
version: 1.1.1
metadata:
  openclaw:
    skillKey: candidate-interview-agenda-identifier
---

# Candidate Skills Mapper

Use this skill for routine recruiting operations work when the user
asks to map candidate skills to an interview plan.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `candidate_profile_yaml`

Candidate and role profile supplied for interview planning.

Accepted value: string or object with `candidate_id`, `profile`, `role`.

## Output

Field: `interview_plan`

Return a concise interview plan for the user's current request in the requested
output field. The returned value is a object with `candidate_id`, `matched_required`, `missing_required`, `topics`.

## Example Request

```text
Use the supplied candidate_profile_yaml to map candidate skills to an interview plan.
Return the result in interview_plan.
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
local records are included for reproducibility. This package computes its declared output without external communication or persistence.
