---
name: milestone-schedule-desk
description: Advise deadline timezone policy and record UTC milestone conversions.
version: 1.0.0
metadata:
  openclaw:
    skillKey: milestone-schedule-desk
---

# Milestone Schedule Desk

Use this skill for routine milestone scheduling work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for milestone scheduling work:

1. **Set timezone guidance for project deadlines** with the `advise_deadline_timezone` tool, producing `timezone_mode`.
2. **Register a milestone time interpretation** with the `record_timezone_mode` tool, using the prepared `timezone_mode` and producing `recorded_timezone`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Set timezone guidance for project deadlines

Purpose: Choose a timezone interpretation for unlabeled milestones while preserving explicitly labeled timestamps.

Tool: `advise_deadline_timezone`

Interface fields: input `deadline_request`; output `timezone_mode`.

Create a timezone rule for milestone notes that mix labeled and unlabeled
deadlines. The input is the user's `deadline_request`; the result is a policy a
schedule register can apply consistently.

### Precedence rules

1. Preserve an explicit numeric offset or named timezone attached to a
   timestamp.
2. For an unlabeled deadline, use the timezone named for the project or
   milestone owner.
3. If neither is supplied, use UTC and state that fallback in the result.
4. Resolve daylight-saving offsets for the deadline date, not the date on which
   the request is processed.
5. Do not reinterpret a date-only milestone as a precise instant unless the
   request supplies a local cutoff time.

### Return value

Return `timezone_mode` as a concise string that states the default timezone,
the preservation rule for labeled timestamps, and the handling of date-only
deadlines. This output defines interpretation only and leaves calendar changes
to the schedule register.

### Example interpretation

If a project brief names `Asia/Shanghai`, retain a milestone already labeled
`2026-09-02T09:00-04:00` as written, interpret an unlabeled `2026-09-03 17:00`
in Asia/Shanghai, and keep a plain `2026-09-04` as a date milestone.

### Interface reference

Input field: `deadline_request`. Milestone brief, deadline note, or schedule coordination request.

Accepted value: object.

Output field: `timezone_mode`; the returned value is a
string.

This standalone documentation does not require credentials or access to private files.

## 2. Register a milestone time interpretation

Purpose: Normalize milestone deadlines to UTC and retain the source timezone used for each conversion.

Tool: `record_timezone_mode`

Interface fields: input `timezone_mode`; output `recorded_timezone`.

Apply the supplied `timezone_mode` to one milestone deadline and create a
traceable schedule record.

#### 1. Read the source value

Keep the deadline text exactly as received. Detect whether it carries an
offset, a named timezone, a local time without a label, or only a calendar
date.

#### 2. Select the interpretation

Honor explicit labels first. Otherwise apply the default in the active
timezone guidance. Use the offset that applies on the milestone date. A
date-only value remains date-only unless a cutoff was provided.

#### 3. Record the conversion

Return `recorded_timezone` with `input_deadline`, `utc_deadline`, and
`source_timezone`. For date-only values, `utc_deadline` may remain empty while
`source_timezone` explains the date convention. Reject impossible local times
instead of silently shifting them.

#### Example

With a default of `Europe/Berlin`, an unlabeled local deadline of
`2026-10-20 16:30` is converted using Berlin's offset for that date. The record
retains the original text, the resulting UTC timestamp, and
`Europe/Berlin` as its source.

The output is a registration record; it does not send invitations or alter an
external calendar.

### Interface reference

Input field: `timezone_mode`. Timezone mode selected from the active scheduling guidance.

Accepted value: string or object with `default_timezone`, `preserve_labeled` or object with `cue`.

Output field: `recorded_timezone`; the returned value is a
object with `input_deadline`, `utc_deadline`, `source_timezone`.

This standalone documentation does not require credentials or access to private files.
