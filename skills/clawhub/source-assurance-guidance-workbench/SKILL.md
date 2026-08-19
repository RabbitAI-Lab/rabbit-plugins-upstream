---
name: source-assurance-guidance-workbench
description: Resolve imported field values.
version: 1.0.7
metadata:
  openclaw:
    skillKey: source-assurance-guidance-workbench
---

# Source Resolution Desk

Use this skill for routine source reconciliation work when the user
asks to resolve imported field values.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `source_guidance`

Source-agreement guidance available from the active intake session.

Accepted value: string or object with `required_agreement`, `conflict_action` or object with `cue`.

## Output

Field: `source_resolution`

Return a concise source resolution for the user's current request in the requested
output field. The returned value is a object with `field`, `disposition`, `selected_value`, `agreement_count`.

## Example Request

```text
Use the supplied source_guidance to resolve imported field values.
Return the result in source_resolution.
```
