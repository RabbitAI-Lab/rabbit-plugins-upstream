# TickTick CLI — full reference

Load this when SKILL.md doesn't cover what you need: habits, focus records, comments, kanban columns, project groups, or exact syntax for reminders and recurrence.

## Contents

- [Tasks](#tasks)
- [Projects, groups, columns](#projects-groups-columns)
- [Tags](#tags)
- [Habits](#habits)
- [Focus](#focus)
- [Countdown](#countdown)
- [Task fields](#task-fields)
- [Reminder syntax](#reminder-syntax)
- [Recurrence syntax](#recurrence-syntax)
- [Filter and query bodies](#filter-and-query-bodies)

Two reminders throughout: this user is UTC-5, so every ISO datetime ends in `-0500`; and all user-supplied text goes in single quotes before it reaches the shell.

---

## Tasks

```bash
ticktick task get <projectId> <taskId>

ticktick task create --title "Buy milk" --project <projectId>
ticktick task create --title "Meeting" --project <projectId> \
  --priority 5 --due-date "2026-08-10T09:00:00-0500"
ticktick task create --title "Review" --project <projectId> --tags work,urgent

# taskId is passed twice — positional and --id. Both are required.
ticktick task update <taskId> --id <taskId> --project <projectId> --title "Updated"
ticktick task update <taskId> --id <taskId> --project <projectId> --tags work,urgent
ticktick task update <taskId> --id <taskId> --project <projectId> --parent-id <parentId>
ticktick task update <taskId> --id <taskId> --project <projectId> --parent-id null   # unlink
ticktick task update <taskId> --id <taskId> --project <projectId> \
  --estimated-duration 1500 --estimated-pomo 5

ticktick task complete <projectId> <taskId>
ticktick task delete <projectId> <taskId>

ticktick task move --from <srcProjectId> --to <dstProjectId> --task <taskId>

ticktick task completed --projects <projectId> \
  --start-date "2026-08-01T00:00:00-0500" --end-date "2026-08-08T23:59:59-0500"

ticktick task filter --projects <projectId> --priority 3,5 --status 0

ticktick task comment list <projectId> <taskId>
ticktick task comment add <projectId> <taskId> --title "Done"
ticktick task comment delete <projectId> <taskId> <commentId>
```

Subtasks are made with `--parent-id` on `task update`, not at creation time: create the task first, then link it.

## Projects, groups, columns

```bash
ticktick project list
ticktick project get <projectId>
ticktick project data <projectId>          # project + open tasks + columns
ticktick project create --name "Work" --color "#F18181" --view-mode list --kind TASK
ticktick project update <projectId> --name "New Name" --color "#4AB8A9"
ticktick project delete <projectId>

ticktick project group list                # folders
ticktick project group create --name "Work"
ticktick project group update <groupId> --name "Personal"
ticktick project group delete <groupId>

ticktick project column list <projectId>   # kanban
ticktick project column create <projectId> --name "In progress"
ticktick project column update <projectId> <columnId> --name "Done"
```

`--view-mode` is `list`, `kanban`, or `timeline`. `--kind` is `TASK` or `NOTE`.

`project data` returns only **incomplete** tasks. For completed ones use `task completed`.

## Tags

```bash
ticktick tag list
ticktick tag create --name urgent --label urgent
```

Tags on tasks are set with `--tags` (comma-separated) on create/update. Setting `--tags` replaces the whole list rather than appending — read the current tags first if the user wants to add one.

## Habits

```bash
ticktick habit list
ticktick habit get <habitId>
ticktick habit create --name "Drink water" --goal 8 --unit cups \
  --repeat "RRULE:FREQ=DAILY;INTERVAL=1"
ticktick habit update <habitId> --name "Drink more water" --goal 10
ticktick habit checkin <habitId> --stamp 20260807 --value 1 --goal 8
ticktick habit checkins --habits <id1>,<id2> --from 20260801 --to 20260831
```

Habit dates use compact `YYYYMMDD` stamps, not ISO datetimes.

## Focus

```bash
ticktick focus get <focusId> --type pomodoro
ticktick focus list --from "2026-08-01T00:00:00-0500" --to "2026-08-31T23:59:59-0500" --type 0
ticktick focus create --type pomodoro --task-id <taskId> \
  --start-time "2026-08-07T09:00:00-0500" --end-time "2026-08-07T09:25:00-0500" --duration 1500
ticktick focus delete <focusId> --type timing
```

`focus list` accepts a maximum range of 30 days. For a longer report, page through month by month. Durations are in **seconds**.

## Countdown

```bash
ticktick countdown list
```

---

## Task fields

Field names in `--json` output are camelCase and match what create/update send.

| Field | Meaning | CLI flag |
|---|---|---|
| `id` | Task id (hex string) | positional `<taskId>` + `--id` on update |
| `projectId` | Owning project | `--project` |
| `title` | Short title | `--title` |
| `content` | Body text for normal/note tasks | `--content` |
| `desc` | Description for checklist tasks | `--desc` |
| `startDate` / `dueDate` | Schedule; if they differ the API treats it as a span | `--start-date`, `--due-date` |
| `timeZone` | Task timezone | `--time-zone` |
| `isAllDay` | All-day flag | `--all-day` |
| `priority` | 0 none, 1 low, 3 medium, 5 high | `--priority` |
| `reminders` | Trigger strings, see below | `--reminders` |
| `repeatFlag` | Recurrence rule, see below | `--repeat` |
| `status` | 0 open, 2 completed, -1 abandoned | — |
| `completedTime` | When completed | — |
| `items` | Checklist items | `--items` |
| `tags` | Tag names | `--tags` (comma-separated) |
| `parentId` / `childIds` | Subtask links | `--parent-id` (`null` to unlink) |
| `columnId` / `columnName` | Kanban placement | — |
| `sortOrder` | Order in list | `--sort-order` |
| `focusSummaries` | Focus metrics | `--estimated-duration`, `--estimated-pomo` |
| `kind` | `TASK`, `NOTE`, or `CHECKLIST` | — |
| `etag` | Server-side optimistic lock | — |

Checklist items (`items[]`) carry `id`, `status` (0 not done / 1 done), `title`, `sortOrder`, and optional `startDate`, `isAllDay`, `timeZone`, `completedTime`.

Focus summaries: `estimatedDuration` (seconds) and `estimatedPomo` (max 60) are writable; `pomoCount`, `pomoDuration`, `stopwatchDuration` are read-only.

Project fields: `id`, `name`, `color`, `sortOrder`, `closed`, `groupId`, `viewMode`, `permission` (`read`/`comment`/`write`), `kind`.

## Reminder syntax

Pattern: `TRIGGER(;RELATED=START|END)?:(-)?P[nY][nM][nW][nD][T[nH][nM][nS]]`

- `TRIGGER` — required prefix.
- `;RELATED=START` or `;RELATED=END` — optional, anchors to task start or end.
- `-` after the colon means **before** the anchor. Omitting it means after — which is almost never what a user wants, so include the minus unless they explicitly ask for a follow-up nudge.

| String | Meaning |
|---|---|
| `TRIGGER:PT0S` | at the due time |
| `TRIGGER:-PT15M` | 15 minutes before |
| `TRIGGER:-PT60M` | 1 hour before |
| `TRIGGER:-P1D` | 1 day before |
| `TRIGGER:-P1DT2H` | 1 day 2 hours before |
| `TRIGGER;RELATED=END:-PT15M` | 15 min before the end time |

## Recurrence syntax

One rule string, either `RRULE` (standard) or `ERULE` (TickTick custom). Never mix the two in one value.

```
RRULE:FREQ=DAILY
RRULE:FREQ=DAILY;INTERVAL=2
RRULE:FREQ=WEEKLY;BYDAY=MO,WE,FR
RRULE:FREQ=MONTHLY;BYMONTHDAY=1
ERULE:NAME=CUSTOM;BYDATE=20260825,20260830
```

Day codes are `MO TU WE TH FR SA SU`.

## Filter and query bodies

`task filter` flags:

| Flag | Notes |
|---|---|
| `--projects` | comma-separated project IDs |
| `--start-date` / `--end-date` | ISO 8601 |
| `--priority` | comma-separated from 0,1,3,5 |
| `--tag` | comma-separated |
| `--status` | comma-separated; 0 open, 2 completed |

`task completed` flags: `--projects`, `--start-date`, `--end-date`.

`task move`: repeat `--from`, `--to`, `--task` in matching counts to move several tasks in one call.
