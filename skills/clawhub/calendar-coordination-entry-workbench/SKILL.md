---
name: calendar-coordination-entry-workbench
description: Create a coordination calendar entry.
version: 1.0.7
metadata:
  openclaw:
    skillKey: calendar-coordination-entry-workbench
---

# Coordination Calendar Desk

Use this skill for routine meeting coordination work when the user
asks to create a coordination calendar entry.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `event_digest`

Normalized event digest prepared for meeting coordination.

Accepted value: object with `event_id`, `starts_at`, `ends_at`, `timezone`, `duration_minutes`.

## Output

Field: `calendar_artifact`

Return a concise calendar artifact for the user's current request in the requested
output field. The returned value is a object with `artifact_id`, `event_id`, `ics_content`.

## Example Request

```text
Use the supplied event_digest to create a coordination calendar entry.
Return the result in calendar_artifact.
```
