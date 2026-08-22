---
name: source-assurance-guidance-identifier
description: Set source-agreement guidance.
version: 1.0.7
metadata:
  openclaw:
    skillKey: source-assurance-guidance-identifier
---

# Source Agreement Guide

Use this skill for routine source reconciliation work when the user
asks to set source-agreement guidance.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `source_profile`

Source count, field importance, and disagreement preference.

Accepted value: object.

## Output

Field: `source_guidance`

Return a concise source guidance for the user's current request in the requested
output field. The returned value is a string.

## Example Request

```text
Use the supplied source_profile to set source-agreement guidance.
Return the result in source_guidance.
```
