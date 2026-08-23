---
name: repository-release-changes-workbench
description: Publish a release-note entry.
version: 1.0.7
metadata:
  openclaw:
    skillKey: repository-release-changes-workbench
---

# Release Notes Journal

Use this skill for routine release coordination work when the user
asks to publish a release-note entry.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `release_change_set`

Structured change set prepared for a release handoff.

Accepted value: object with `change_id`, `files`, `components`, `additions`, `deletions`.

## Output

Field: `release_note_receipt`

Return a concise release note receipt for the user's current request in the requested
output field. The returned value is a object with `change_id`, `title`, `markdown`, `file_count`.

## Example Request

```text
Use the supplied release_change_set to publish a release-note entry.
Return the result in release_note_receipt.
```
