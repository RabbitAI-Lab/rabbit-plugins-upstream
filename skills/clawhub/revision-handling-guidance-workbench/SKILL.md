---
name: revision-handling-guidance-workbench
description: Merge an account revision.
version: 1.0.7
metadata:
  openclaw:
    skillKey: revision-handling-guidance-workbench
---

# Account Merge Workbench

Use this skill for routine account maintenance work when the user
asks to merge an account revision.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `merge_guidance`

Field merge guidance available from the active account session.

Accepted value: string or object with `strategy`, `preserve_absent`, `accept_blank` or object with `cue`.

## Output

Field: `merge_result`

Return a concise merge result for the user's current request in the requested
output field. The returned value is a object with `merged_record`, `changed_fields`, `preserved_fields`.

## Example Request

```text
Use the supplied merge_guidance to merge an account revision.
Return the result in merge_result.
```
