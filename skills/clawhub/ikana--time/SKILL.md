---
name: time
slug: time
description: LLM time reasoning scaffold with a bundled Node.js CLI.
when_to_use: Use when a task involves dates, deadlines, scheduling, or relative time reasoning.
---

# time

Use the bundled CLI to anchor work at NOW and place events as spatial distances (ahead/behind) for reliable time reasoning.

## Ego-Moving Metaphor (Required)

Use one frame only: you move forward through time.
- Future is ahead of you.
- Past is behind you.
- Correct: "We are approaching the deadline."
- Incorrect: "The deadline is approaching."

## Bundled CLI

- Requires Node.js 18+.
- Source code is bundled inside this skill at `scripts/time.mjs`.
- Do not install or download any external binary.
- Set `SKILL_DIR` to the absolute path of this installed skill directory, then run:
  `node "$SKILL_DIR/scripts/time.mjs" <command> [options]`

## Quick Start

```bash
SKILL_DIR="<absolute path to this time skill directory>"
TIME_CLI="$SKILL_DIR/scripts/time.mjs"
node "$TIME_CLI" init
node "$TIME_CLI" add "Sprint review" --on "2026-02-21" --type ceremony
node "$TIME_CLI" add "v0.3.0 deadline" --in "13 days" --type milestone --notes "new auth flow"
node "$TIME_CLI" show
```

## Commands

Run these command names after `node "$SKILL_DIR/scripts/time.mjs"`.

### `init [--timezone <iana_tz>] [--force]`

Create `time.md` with NOW as the anchor. Use `--force` to overwrite an existing file.

### `now [--timezone <iana_tz>]`

Update only the NOW section timestamp metadata. Does not recalculate event distances.

### `add <event> (--in <duration> | --on <date> | --at <datetime>) [--type <type>] [--notes <text>]`

Add one event with exactly one time selector:
- `--in`: relative duration (`"3 days"`, `"in 4 hours"`, `"2 days ago"`)
- `--on`: date input (`"2026-03-01"`, `"tomorrow"`, `"next Monday"`)
- `--at`: ISO datetime (`"2026-02-20T14:00:00Z"`)

### `show`

Print full `time.md` to stdout.

### `past`

Print NOW + the Behind (Past) timeline section.

### `ahead`

Print NOW + the Ahead (Future) timeline section.

### `refresh`

Move NOW to current time and recalculate all event distances/order.

### `remove <event>`

Remove an event from timeline and sequences.

### `seq <name> <event1> <event2> [event3...]`

Create/update a named sequence chain.

### `span <name> --from <when> --to <when>`

Create/update a named duration span. `--from` must be before `--to`.

## Annotated `time.md` Format

```markdown
# Time Context

## Now
- **timestamp**: 2026-02-19T09:00:00.000Z   <!-- anchor -->
- **weekday**: Thursday
- **week**: 8 of 52
- **quarter**: Q1 2026
- **timezone**: Europe/Amsterdam

## Timeline

### Behind (Past)
| distance | event | type | notes | iso |
|----------|-------|------|-------|-----|
| 1 day behind | bug #42 reported | issue | auth timeout | 2026-02-18T10:00:00.000Z |

### Ahead (Future)
| distance | event | type | notes | iso |
|----------|-------|------|-------|-----|
| 2 days ahead | sprint review | ceremony | demo v0.2.1 | 2026-02-21T14:00:00.000Z |

## Sequences
### release-cycle
v0.2.0 released → bug #42 reported → [NOW] → sprint review → v0.3.0 deadline

## Durations
| span | from | to | length |
|------|------|----|--------|
| current sprint | 5 days behind | 2 days ahead | 7 days |
```

## Scratch Pad Pattern (`/tmp`)

Use this for one-shot reasoning so project files stay clean:

```bash
cd /tmp
SKILL_DIR="<absolute path to this time skill directory>"
TIME_CLI="$SKILL_DIR/scripts/time.mjs"
node "$TIME_CLI" init --force
node "$TIME_CLI" add "Draft due" --on "2026-02-25"
node "$TIME_CLI" add "Client review" --in "3 days"
node "$TIME_CLI" show
# draft your output using the timeline
rm -f time.md
```

## Sequences

Use sequences to express ordered chains for planning:

```bash
node "$TIME_CLI" seq "release-cycle" "RFC drafted" "Implementation starts" "Testing" "Launch"
```

`show` places `[NOW]` at the correct position relative to sequence events.

## Spans

Use spans for time windows:

```bash
node "$TIME_CLI" span "Sprint 12" --from "2026-02-17" --to "2026-02-28"
```

The Durations table shows from/to distances and total length.

## Key Rules

- Run `node "$TIME_CLI" refresh` before reading `time.md` when it may be stale.
- Event names must be unique; remove before re-adding the same name.
- Markdown timeline output is written to stdout.
- Errors/warnings are written to stderr.
- The bundled CLI is fully non-interactive (no prompts).
