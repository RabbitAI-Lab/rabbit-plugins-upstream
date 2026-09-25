---
name: interview-planning-studio
description: Map candidate skills and render interview agenda artifacts.
version: 1.0.0
metadata:
  openclaw:
    skillKey: interview-planning-studio
---

# Interview Planning Studio

Use this skill for routine recruiting operations work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for recruiting operations work:

1. **Map candidate skills to an interview plan** with the `map_candidate_skills` tool, producing `interview_plan`.
2. **Build an interview agenda** with the `render_interview_agenda` tool, using the prepared `interview_plan` and producing `agenda_artifact`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Map candidate skills to an interview plan

Purpose: Map candidate skills to an interview plan.

Tool: `map_candidate_skills`

Interface fields: input `candidate_profile_yaml`; output `interview_plan`.

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

## 2. Build an interview agenda

Purpose: Build an interview agenda.

Tool: `render_interview_agenda`

Interface fields: input `interview_plan`; output `agenda_artifact`.

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
