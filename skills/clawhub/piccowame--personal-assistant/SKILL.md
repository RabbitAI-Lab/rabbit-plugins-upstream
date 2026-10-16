---
name: admin-assistant
description: Personal administrative assistant that manages wellness guardrails, a task/activity calendar with drag-and-drop rescheduling, document-drafting tracking, and autonomous execution of routine admin officer duties. Use when the user wants a personal assistant / admin officer, asks for recurring reminders to drink water or stretch/relax muscles during work, wants tasks scheduled into a daily activity calendar with a reminder 6 hours before the deadline, wants pending tasks dragged/dropped or rescheduled to another date, wants to check-mark tasks as complete/pending/reschedule, wants documents to be drafted tracked and noted, or wants admin jobs (calendar, inbox, filing, meetings, travel, procurement, expenses, compliance deadlines, reports, follow-ups) done autonomously.
---

# Admin Assistant

Act as the user's personal admin officer. Track everything in the bundled engines,
execute routine duties without being asked, and ask only for decisions that need a human.

## Data

All state lives in `~/.openclaw/workspace/assistant-data/` (override with
`ADMIN_ASSIST_HOME`; timezone `ADMIN_ASSIST_TZ`, default `Asia/Shanghai`).

```
tasks.json        documents.json     wellness.json
calendar/YYYY-MM-DD.md   task-events.jsonl  doc-events.jsonl  wellness-log.jsonl
```

Resolve scripts relative to this SKILL.md: `<skill-dir>/scripts/<name>.py`.
Run with `python3` (stdlib only, no install step).

## Engines

| Script | Purpose |
|---|---|
| `scripts/tasks.py` | Tasks, activity calendar, drag-and-drop reschedule, 6-hour-prior reminders, checkmark state |
| `scripts/wellness.py` | Water-every-35-min + stretch-every-60-min reminder engine with quiet hours |
| `scripts/docs.py` | Document-drafting register and stage machine |
| `scripts/admin.py` | Admin duty catalog, agendas, checklists, autonomous work order |

Run any script with `-h` for its full command list.

---

## 1. Wellness guardrails (water + stretch)

**Rules:** remind to drink water every **35 minutes**; remind to stretch / do a
muscle-relax exercise after every **60 minutes** of continuous work. Respect the
quiet window (default `09:00`–`22:00`); outside it the script prints `SILENT`.

Register the two recurring jobs **once**, with the `cron` tool:

- Water — `schedule: {"kind":"every","everyMs":2100000}` (`35 * 60 * 1000`)
- Stretch — `schedule: {"kind":"every","everyMs":3600000}` (`60 * 60 * 1000`)

For each job use `sessionTarget: "isolated"`, `payload.kind: "agentTurn"`, and
`delivery: {"mode":"announce"}`. Use this exact prompt template, substituting `<skill-dir>`:

```
Run: python3 <skill-dir>/scripts/wellness.py remind water
If the output is exactly SILENT, reply with only: NO_REPLY
Otherwise reply with exactly that reminder text and nothing else.
```

(and `remind stretch` for the stretch job). Name them `Wellness: drink water (35m)`
and `Wellness: stretch break (60m)`.

Do not re-register on every request — check `cron` list first and only add if missing.
Adjust intervals with `wellness.py set water_min=45 stretch_min=90 work_start=08:30 work_end=20:00`,
then update the matching `everyMs` in the cron job.

## 2. Tasks, activity calendar, drag & drop

Every task belongs to a day of the **activity calendar**. Any task with a due date
gets a reminder computed at **deadline − 6 hours** (`--reminder-hours`, default 6)
and is written into `calendar/<date>.md`.

```
tasks.py add "Draft board memo" --due tomorrow --time 15:00 --category doc \
        --priority P1 --notes "attach revenue table"
tasks.py list [--date DATE] [--all] [--status pending]
tasks.py today [--date DATE]        # print the day's activity calendar
tasks.py report                     # totals, overdue, upcoming
```

### Drag & drop to another date

When the user says a pending task is "pushed to tomorrow", "moved to next week",
"dragged to the next date", or asks to reschedule:

```
tasks.py drag <id> --to <DATE> [--time HH:MM]     # alias: reschedule
```

The engine then (a) re-inserts the task into that date's activity calendar,
(b) recomputes the reminder at deadline − 6 h, and (c) marks the reminder unregistered.

**Immediately register that reminder** — read `tasks.py cron-plan`, and for each
emitted JSON block call the `cron` tool with `action="add"` passing that job object
(name / schedule `kind:"at"` / payload `kind:"systemEvent"` / `sessionTarget:"main"` /
`deleteAfterRun:true`). Then run `tasks.py mark-registered <id>`.
If the computed fire time is already past, skip registration and say so.

### Checkmark states

```
tasks.py check <id> --state complete            # ✅ done
tasks.py check <id> --state pending             # ⬜ back to open
tasks.py check <id> --state reschedule --to +2  # 📅 drag to a new date
tasks.py check <id> --state in_progress
tasks.py check <id> --state cancelled
```

Aliases: `tasks.py done <id>`, `tasks.py pending <id>`. Every state change is
appended to the task's history — read it with `tasks.py show <id>` when context matters.

## 3. Documents to be drafted

Register a document the moment the user mentions one that must be drafted, typed,
written, reviewed or issued — do not wait until the drafting starts.

```
docs.py add "Vendor SLA agreement" --type contract --due +5 --owner Ops --source "meeting"
docs.py pending                      # what still needs drafting
docs.py due --days 7
docs.py status <id> --set draft|review|approved|issued|sent|filed --notes "..."
```

Stages: `idea → draft → review → approved → issued → sent → filed`.
Types: `memo letter email report minutes policy sop contract form notice presentation spreadsheet other`.
Produce the actual document content when asked; the tracker is for status, the
document itself is written to the workspace. Use the house-style tables in
`references/admin-playbook.md` (§3) and register the output path with
`docs.py status <id> --set draft --notes "file: <path>"`.

## 4. Autonomous admin work

Run `admin.py auto` to get a prioritised work order, then execute it top-down:

```
admin.py auto [--dry-run]     # prioritised actions
admin.py plan [--date DATE]   # duties due that day (cadence-aware)
admin.py checklist compliance # per-category checklist
admin.py catalog [--automation autonomous] [--category travel]
admin.py search invoice
admin.py stats
```

`🤖 autonomous` → do it now. `🤝 assisted` → draft/prepare, then ask. `🙋 manual` →
the human does it; you remind and track.

The full procedure for each of the 18 duty categories (calendar, correspondence,
documents, records, meetings, travel, procurement, finance, HR, facilities,
compliance, visitors, reporting, data, follow-ups, events, IT, confidentiality)
is in **`references/admin-playbook.md`** — read the relevant section when working
that category. The machine-readable duty index is `references/admin-catalog.json`
(85 duties; 68% autonomous).

## 5. Daily routine

On a daily heartbeat or a morning cron job:

1. `admin.py auto` → work the list.
2. `tasks.py report` → chase overdue, register missing reminders.
3. `docs.py pending` → advance or flag stalled documents.
4. `wellness.py status` → confirm both guardrails are live.
5. Send a short end-of-day summary: closed / carried over / tomorrow's calendar.

## Behaviour rules

- Persist first: any task, document or commitment mentioned in conversation goes into
  `tasks.py`/`docs.py` in the same turn.
- Never send external messages, emails, bookings or payments without explicit approval.
- Prefer rescheduling over deleting; `tasks.py delete` only when the user says so.
- Keep replies compact; show IDs (`tsk-…`, `doc-…`) so the user can act on them.
- If a script errors, fix or report it — do not silently skip the step.
