---
name: calendar-coordination-entry
description: Combines normalize a calendar handoff with create a coordination calendar entry.
version: 1.0.7
metadata:
  openclaw:
    skillKey: calendar-coordination-entry
---

# Calendar Handoff Reader and Coordination Calendar Desk

Use this skill for routine meeting coordination work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Calendar Handoff Reader

Tool: `normalize_calendar_event`

Reads calendar event blocks and normalizes timing and location details for meeting coordination.

Input field: `event_ics`. Calendar event block supplied for a meeting handoff.

Output field: `event_digest`.

## Operation 2: Coordination Calendar Desk

Tool: `create_coordination_entry`

Creates calendar entries from normalized event handoffs for attendee and agenda follow-up.

Input field: `event_digest`. Normalized event digest prepared for meeting coordination.

Output field: `calendar_artifact`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
