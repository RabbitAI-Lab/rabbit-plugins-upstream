---
name: candidate-interview-agenda-identifier
description: Map candidate skills to an interview plan.
version: 1.0.7
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
