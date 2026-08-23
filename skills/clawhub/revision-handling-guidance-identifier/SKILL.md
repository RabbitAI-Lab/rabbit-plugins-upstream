---
name: revision-handling-guidance-identifier
description: Set account merge guidance.
version: 1.0.7
metadata:
  openclaw:
    skillKey: revision-handling-guidance-identifier
---

# Account Merge Guide

Use this skill for routine account maintenance work when the user
asks to set account merge guidance.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `revision_profile`

Account revision profile and field-preservation preference.

Accepted value: object.

## Output

Field: `merge_guidance`

Return a concise merge guidance for the user's current request in the requested
output field. The returned value is a string.

## Example Request

```text
Use the supplied revision_profile to set account merge guidance.
Return the result in merge_guidance.
```
