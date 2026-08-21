---
name: support-followup-marker-identifier
description: Prepare a support intake digest.
version: 1.0.7
metadata:
  openclaw:
    skillKey: support-followup-marker-identifier
---

# Support Intake Digest

Use this skill for routine support operations work when the user
asks to prepare a support intake digest.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `snippet`

Support intake message with case, priority, and subject fields.

Accepted value: string.

## Output

Field: `support_digest`

Return a concise support digest for the user's current request in the requested
output field. The returned value is a object with `case_id`, `priority`, `subject`, `follow_up_category`.

## Example Request

```text
Use the supplied snippet to prepare a support intake digest.
Return the result in support_digest.
```
