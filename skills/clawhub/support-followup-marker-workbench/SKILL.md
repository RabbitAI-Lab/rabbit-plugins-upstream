---
name: support-followup-marker-workbench
description: Build a support case comment.
version: 1.0.7
metadata:
  openclaw:
    skillKey: support-followup-marker-workbench
---

# Support Case Workbench

Use this skill for routine support operations work when the user
asks to build a support case comment.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `support_digest`

Support digest prepared for a case handoff.

Accepted value: object with `case_id`, `priority`, `subject`, `follow_up_category`.

## Output

Field: `case_comment`

Return a concise case comment for the user's current request in the requested
output field. The returned value is a object with `comment_id`, `case_id`, `comment`, `tags`.

## Example Request

```text
Use the supplied support_digest to build a support case comment.
Return the result in case_comment.
```
