---
name: incident-routing-desk
description: Derive severity assignments and record incident owner decisions.
version: 1.0.0
metadata:
  openclaw:
    skillKey: incident-routing-desk
---

# Incident Routing Desk

Use this skill for routine service assignment work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for service assignment work:

1. **Set severity-based assignment guidance** with the `derive_severity_assignment` tool, producing `assignment_guidance`.
2. **Assign an incident owner** with the `assign_incident_owner` tool, using the prepared `assignment_guidance` and producing `assignment_result`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Set severity-based assignment guidance

Purpose: Map incident severity and service context to an accountable response owner and queue.

### Before invoking this stage

Look for the severity scale, service owner, response lead, operating hours, and
fallback queue. Preserve an owner explicitly named for the affected service.
When the profile is incomplete, identify the missing routing fact instead of
guessing a person.

Tool: `derive_severity_assignment`

Interface fields: input `service_profile`; output `assignment_guidance`.

Use `service_profile` to establish who receives an incoming service alert. The
guide produces an assignment rule, not an alert or a page.

### Required context

Look for the severity scale, service owner, response lead, operating hours, and
fallback queue. Preserve an owner explicitly named for the affected service.
When the profile is incomplete, identify the missing routing fact instead of
guessing a person.

### Assignment matrix

- P1 and P2: route to the designated response lead and identify the service
  queue that tracks the incident.
- P3 and P4: route to the normal service queue with its accountable owner.
- Unknown severity: hold for classification and name the queue responsible for
  triage.
- Outside operating hours: apply the profile's on-call or next-business-window
  rule.

### Guidance output

Return `assignment_guidance` as a single, readable policy string containing the
severity-to-owner mapping, the fallback route, and any operating-hours
condition. Keep role names stable so a later incident desk can apply the rule
without resolving aliases again.

### Example

A profile that assigns P1-P2 to the response lead and P3-P4 to the service
queue should yield exactly that split, plus the named triage queue for an alert
whose severity has not yet been classified.

### Interface reference

Input field: `service_profile`. Service levels and assignment preference for incoming alerts.

Accepted value: object.

Output field: `assignment_guidance`; the returned value is a
string.

This standalone documentation does not require credentials or access to private files.

## 2. Assign an incident owner

Purpose: Assign an incident owner.

Tool: `assign_incident_owner`

Interface fields: input `assignment_guidance`; output `assignment_result`.

Use this skill for routine service assignment work when the user
asks to assign an incident owner.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `assignment_guidance`

Severity assignment guidance available from the active service session.

Accepted value: string or object with `routing_table`, `default_assignment` or object with `cue`.

### Output

Field: `assignment_result`

Return a concise assignment result for the user's current request in the requested
output field. The returned value is a object with `alert_id`, `severity`, `assignment`, `matched_rule`.

### Example Request

```text
Use the supplied assignment_guidance to assign an incident owner.
Return the result in assignment_result.
```
