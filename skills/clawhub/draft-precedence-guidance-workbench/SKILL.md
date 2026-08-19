---
name: draft-precedence-guidance-workbench
description: Select a document release.
version: 1.0.7
metadata:
  openclaw:
    skillKey: draft-precedence-guidance-workbench
---

# Document Release Selector

Use this skill for routine document release selection work when the user
asks to select a document release.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `selection_guidance`

Release selection guidance available from the active document session.

Accepted value: string or object with `current_major`, `require_approved`, `allow_prerelease` or object with `cue`.

## Output

Field: `selection_result`

Return a concise selection result for the user's current request in the requested
output field. The returned value is a object with `selected_version`, `eligible_versions`, `reason`.

## Example Request

```text
Use the supplied selection_guidance to select a document release.
Return the result in selection_result.
```
