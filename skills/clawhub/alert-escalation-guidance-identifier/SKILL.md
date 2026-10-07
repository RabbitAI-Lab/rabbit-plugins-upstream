---
name: alert-escalation-guidance-identifier
description: Map incident severity and service context to an accountable response owner and queue.
version: 1.1.1
metadata:
  openclaw:
    skillKey: alert-escalation-guidance-identifier
---

# Service Assignment Guide

Use `service_profile` to establish who receives an incoming service alert. The
guide produces an assignment rule, not an alert or a page.

## Required context

Look for the severity scale, service owner, response lead, operating hours, and
fallback queue. Preserve an owner explicitly named for the affected service.
When the profile is incomplete, identify the missing routing fact instead of
guessing a person.

## Assignment matrix

- P1 and P2: route to the designated response lead and identify the service
  queue that tracks the incident.
- P3 and P4: route to the normal service queue with its accountable owner.
- Unknown severity: hold for classification and name the queue responsible for
  triage.
- Outside operating hours: apply the profile's on-call or next-business-window
  rule.

## Guidance output

Return `assignment_guidance` as a single, readable policy string containing the
severity-to-owner mapping, the fallback route, and any operating-hours
condition. Keep role names stable so a later incident desk can apply the rule
without resolving aliases again.

## Example

A profile that assigns P1-P2 to the response lead and P3-P4 to the service
queue should yield exactly that split, plus the named triage queue for an alert
whose severity has not yet been classified.

## Interface reference

Input field: `service_profile`. Service levels and assignment preference for incoming alerts.

Accepted value: object.

Output field: `assignment_guidance`; the returned value is a
string.

This standalone documentation does not require credentials or access to private files.

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
