---
name: deadline-locale-guidance-identifier
description: Choose a timezone interpretation for unlabeled milestones while preserving explicitly labeled timestamps.
version: 1.0.7
metadata:
  openclaw:
    skillKey: deadline-locale-guidance-identifier
---

# Deadline Locale Guide

Create a timezone rule for milestone notes that mix labeled and unlabeled
deadlines. The input is the user's `deadline_request`; the result is a policy a
schedule register can apply consistently.

## Precedence rules

1. Preserve an explicit numeric offset or named timezone attached to a
   timestamp.
2. For an unlabeled deadline, use the timezone named for the project or
   milestone owner.
3. If neither is supplied, use UTC and state that fallback in the result.
4. Resolve daylight-saving offsets for the deadline date, not the date on which
   the request is processed.
5. Do not reinterpret a date-only milestone as a precise instant unless the
   request supplies a local cutoff time.

## Return value

Return `timezone_mode` as a concise string that states the default timezone,
the preservation rule for labeled timestamps, and the handling of date-only
deadlines. This output defines interpretation only and leaves calendar changes
to the schedule register.

## Example interpretation

If a project brief names `Asia/Shanghai`, retain a milestone already labeled
`2026-09-02T09:00-04:00` as written, interpret an unlabeled `2026-09-03 17:00`
in Asia/Shanghai, and keep a plain `2026-09-04` as a date milestone.

## Interface reference

Input field: `deadline_request`. Milestone brief, deadline note, or schedule coordination request.

Accepted value: object.

Output field: `timezone_mode`; the returned value is a
string.

This standalone documentation does not require credentials or access to private files.
