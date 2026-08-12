---
name: "ticktick"
description: "Include Inbox tasks and habits in complete TickTick Today queries."
metadata:
  {
    "openclaw":
      {
        "emoji": "✅",
        "homepage": "https://ticktick.com",
        "requires": { "bins": ["ticktick"] },
        "os": ["linux"],
        "install":
          [
            {
              "id": "npm",
              "kind": "node",
              "package": "@ticktick/ticktick-cli",
              "bins": ["ticktick"],
              "label": "Install TickTick CLI (npm)",
            },
          ],
      },
  }
---

# TickTick

Drive TickTick from the shell with the `exec` tool, using `ticktick` — the official CLI wrapping TickTick Open API v1.

This runs on a **headless Debian server**: no browser, no display. Local time is **America/Guayaquil (UTC-5, no DST)**.

## Before anything else

Run `ticktick auth status`.

- **Logged in** → proceed.
- **Not logged in** → read `{baseDir}/references/setup.md`. Never run `ticktick auth login`; it waits on a browser that does not exist here and hangs the turn until it times out.

Never run `ticktick auth logout` unless explicitly asked — the token can only be replaced through manual browser steps.

## Quoting matters

Task titles come from user messages and get interpolated into shell commands. A title containing backticks, `$(...)`, `;`, or `&&` becomes executable if passed unquoted. Always wrap user-supplied text in **single quotes**, escaping any embedded single quote as `'\''`:

```bash
ticktick task create --title 'Pagar la luz' --project <projectId>
```

Never paste a raw message straight into a command string. This is a server with shell access; a task titled `foo; rm -rf ~` should create a task with a silly name, not delete a home directory.

## Everything needs a project ID

Users speak in names ("agrégalo a Trabajo"); every command wants a hex ID. So the first action in a session is nearly always:

```bash
ticktick project list --json
```

Reuse that result for the rest of the session — projects rarely change, and re-listing every turn adds a round-trip the user waits through on Telegram. Re-run only if a project seems missing or was just created.

Match names case-insensitively, tolerating accents and partial matches. One plausible match → use it. Several → show them and ask. None → say so and list what exists, rather than inventing an ID; a fabricated hex string produces a cryptic API error instead of a useful "that project doesn't exist".

Tasks with no project live in **Inbox**. In the current CLI, Inbox is **not reliably returned by** `project list`. Never assume a list of project IDs covers Inbox; for account-wide task reads, prefer commands without a `--projects` restriction when supported.

## Dates: always write the offset

The CLI passes datetimes straight to the API. A bare `2026-08-09T09:00:00` or one ending in `+0000` lands **five hours off** for this user. Always write `-0500` and set the timezone:

```bash
--due-date '2026-08-09T09:00:00-0500' --time-zone 'America/Guayaquil'
```

Use `--all-day` with a midnight-local time for all-day tasks. Resolve "mañana", "el viernes", "en dos semanas" against today's date before building the command — the CLI does no natural-language date parsing.

Priority is numeric and skips values: **0 none, 1 low, 3 medium, 5 high**. There is no 2 or 4.

Status: **0 open, 2 completed, -1 abandoned**.

## Core commands

```bash
# Read
ticktick project list --json                       # all projects
ticktick project data <projectId> --json           # project + its OPEN tasks + columns
ticktick task get <projectId> <taskId> --json

# Create
ticktick task create --title 'Buy milk' --project <projectId>
ticktick task create --title 'Team sync' --project <projectId> \
  --priority 3 --due-date '2026-08-11T15:00:00-0500' \
  --time-zone 'America/Guayaquil' --tags work,meetings

# Update — taskId appears twice, positional AND --id
ticktick task update <taskId> --id <taskId> --project <projectId> --title 'New title'

# Finish / remove
ticktick task complete <projectId> <taskId>
ticktick task delete <projectId> <taskId>          # destructive, see below

# Move between projects
ticktick task move --from <srcProjectId> --to <dstProjectId> --task <taskId>

# Query
ticktick task filter --projects <id1>,<id2> --status 0 \
  --start-date '2026-08-08T00:00:00-0500' --end-date '2026-08-08T23:59:59-0500'
ticktick task completed --projects <projectId> --start-date '...' --end-date '...'

# Tags
ticktick tag list
ticktick tag create --name urgent --label urgent
```

`--json` works on every command. Use it whenever parsing; use plain output only when showing it verbatim, which is rare.

Habits, focus/pomodoro records, comments, project groups and kanban columns are supported too. Full flag tables, field meanings, reminder syntax (`TRIGGER:-PT60M`) and recurrence syntax (`RRULE:FREQ=WEEKLY;BYDAY=MO,WE`) live in `{baseDir}/references/cli-reference.md` — read it when the request goes beyond the commands above.

## Recipes

### "¿Qué tengo hoy?"

There is no `today` command. Reconstruct the complete Today view, including scheduled tasks, all-day tasks, untimed Inbox tasks due today, project tasks due today, and habits:

1. Query open tasks for the local day **without** `--projects`:
   ```bash
   ticktick task filter --status 0 \
     --start-date '<today>T00:00:00-0500' \
     --end-date '<today>T23:59:59-0500' --json
   ```
2. Do not build a `--projects` restriction from `project list`; that silently excludes Inbox in the current CLI.
3. Run `ticktick habit list --json`. For active habits scheduled today, use `ticktick habit checkins --habits <id1>,<id2> --from <YYYYMMDD> --to <YYYYMMDD> --json` to report today's checked/unchecked state.
4. Sort tasks by priority descending, then due time. Keep untimed/all-day items visible and report habits separately so the total is not confused with the task count.

For "overdue", query tasks without `--projects`, set `--start-date` a year back, and set `--end-date` to now.

### Finding a task from a title

The CLI has no title search. Resolve it:

1. Project named → `ticktick project data <projectId> --json`, match on `title`.
2. No project → `task filter --status 0` across all projects, match there.
3. Match generously; people paraphrase their own tasks ("lo del dentista" for "Llamar al dentista"). But when two or more plausibly match, list them with due dates and ask — completing the wrong task is tedious to undo.

Capture both `taskId` and `projectId` when found; every mutation needs both.

### Rescheduling

`task update` with a new `--due-date`. Keep the existing time-of-day unless a new one was given — "pásalo al viernes" means the same hour on Friday, not midnight.

## Confirm before destroying

`task delete` is irreversible and there is no recovery command here. Ask first, always, even when the instruction seems unambiguous.

Completing is reversible, so just do it when asked.

For anything touching multiple tasks — "limpia lo viejo", "borra todo en Archivo" — show the list first (numbered, title + due date), get confirmation, then execute. Vague bulk instructions are where an agent quietly destroys a week of someone's planning.

## Reporting back

Replies land on **Telegram**, in a narrow phone window:

- Short plain-text lines, no tables. Tables wrap into unreadable mush.
- Lead with the outcome: `Listo — 'Llamar al dentista' creada en Personal, vence mañana 10:00.`
- Lists: one task per line, priority and due time only. Ten maximum, then say how many more.
- Omit raw IDs unless asked — noise on a phone. Keep them internally for follow-ups.
- Never paste raw JSON at the user.
- Answer in the language the user wrote in.

## When something fails

- **401 / auth error** → token expired. Walk through regenerating it (`{baseDir}/references/setup.md`); do not attempt `auth login`.
- **404 / not found** → usually a stale project ID. Re-run `project list --json` once, then retry. Still failing → tell the user instead of probing further.
- **Network error** → report and stop. One retry at most; the API is rate-limited and hammering it makes the next hour worse.

Say what actually happened. "No pude crear la tarea, el token expiró" is useful; "algo salió mal" sends the user to SSH into the server themselves.
