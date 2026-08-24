---
name: candidate-interview-agenda-workbench
description: Build an interview agenda.
version: 1.0.7
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
