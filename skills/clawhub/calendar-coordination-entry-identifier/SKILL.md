---
name: calendar-coordination-entry-identifier
description: Normalize a calendar handoff.
version: 1.0.7
metadata:
  openclaw:
    skillKey: calendar-coordination-entry-identifier
---

# Calendar Handoff Reader

Use this skill for routine meeting coordination work when the user
asks to normalize a calendar handoff.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `event_ics`

Calendar event block supplied for a meeting handoff.

Accepted value: string.

## Output

Field: `event_digest`

Return a concise event digest for the user's current request in the requested
output field. The returned value is a object with `event_id`, `starts_at`, `ends_at`, `timezone`, `duration_minutes`.

## Example Request

```text
Use the supplied event_ics to normalize a calendar handoff.
Return the result in event_digest.
```
