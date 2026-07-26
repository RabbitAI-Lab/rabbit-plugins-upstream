---
name: content-review-mode-identifier
description: Triage a workspace content item.
version: 1.0.5
metadata:
  openclaw:
    skillKey: content-review-mode-identifier
---

# Content Intake Triage

Use this skill for routine content operations work when the user
asks to triage a workspace content item.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `content_note`

Workspace content note, planning draft, or internal checklist to triage.

## Output

Field: `review_mode`

Return a concise review mode for the user's current request in the requested
output field.

## Example Request

```text
Use the supplied content_note to triage a workspace content item.
Return the result in review_mode.
```
