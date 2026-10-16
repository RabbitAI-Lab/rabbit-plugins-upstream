---
name: do
description: Install and drive `do`, the agent-drivable CLI for the do personal todo / life-tracking app. `do` is a thin client over the app's public REST API (`/api/v1`) with per-tenant API-key auth — capture tasks, see what's actionable today, complete/snooze tasks, log habits, and read entities (tasks, habits, notes, contacts, recipes, …). There are no destructive verbs, so it's safe to hand to an autonomous agent. Use when the user wants to manage their todos / life-tracking from a terminal or agent, mentions the `do` CLI, or asks to capture or review tasks and habits.
homepage: https://github.com/robbeverhelst/do
metadata:
  openclaw:
    category: productivity
    tags: [todo, life-tracker, gtd, habits, cli]
    package: "@robbeverhelst/do"
    bins:
      - do
---

# do → drive your todos / life-tracking from a terminal or agent

`do` is a thin client over the **do** app's public REST API (`/api/v1`). It
inherits the same per-tenant auth, validation, and row-level-security wall as the
web app — there is no direct DB access. The v1 surface is the **daily loop**:
capture, today, complete/snooze a task, log a habit, and read entities. There are
**no destructive verbs** (no create/update/delete), so it is safe to hand to an
autonomous agent.

> The live, authoritative surface is always `do help --json`. This skill is the
> orientation; when in doubt, introspect the binary — the manifest is generated
> from the same registry the commands dispatch from, so they can't drift.

## Install (pick one)

- **One-off / agents (no install):** `bunx @robbeverhelst/do <command>`.
- **Global:** `npm i -g @robbeverhelst/do` (or `bun add -g @robbeverhelst/do`), then run `do <command>`.
- **Binary:** download the `do-<os>-<arch>` asset from a GitHub Release
  (https://github.com/robbeverhelst/do/releases) and put it on your `PATH`.

Requires **Bun ≥ 1.3** for the `bunx`/binary paths (`bun --version`; install with
`curl -fsSL https://bun.sh/install | bash`).

## Auth (do this first)

Every call needs a **per-tenant API key**, sent as `Authorization: Bearer <key>`.
Keys are minted by the app (the JWT-guarded `POST /api-keys` endpoint, e.g. from
the web app's settings); the CLI only *consumes* a key — it never creates one. A
key only reaches routes whose scope it holds, so grant the scopes for the verbs
you need (`tasks:read`/`tasks:write`, `habits:write`, …).

Config resolves in precedence order (first wins):

1. `--api-key` / `--url` flags
2. `DO_API_KEY` / `DO_API_URL` environment variables  ← the agent / CI path
3. `~/.config/do/config.json`  ← written by `do login` / `do config set`, for humans

The hosted instance is **`https://do.robbe.work/api`** — so you only need a key:

```sh
# Agent / CI: just export the env vars.
export DO_API_KEY=do_xxx
export DO_API_URL=https://do.robbe.work/api   # hosted instance (see note below)

# Human: verify a key and save it (file is written 0600).
do login --api-key do_xxx --url https://do.robbe.work/api
do whoami                 # prove the key resolves to a tenant + scopes
do config show            # resolved config, key redacted, with sources
```

The URL ends in `/api` because the API sits behind the web app's same-origin
`/api` proxy (the CLI appends `/api/v1` itself). For a self-hosted instance, use
`https://<your-host>/api`; for local dev, `http://localhost:3001`. **Only the
API key is per-user — ask the user for a scoped key.**

## Output contract (agent ergonomics)

- `--json` forces JSON; output is **automatically JSON when stdout is piped**
  (non-TTY), so an agent always gets parseable output. A TTY gets pretty,
  colored text (honoring `NO_COLOR`, `--quiet`, `--verbose`).
- **Failures** print a JSON error envelope to stdout in JSON mode
  (`{ "error": { "code", "message" } }`) and a non-zero **exit code**:

  | exit | meaning                                   |
  |------|-------------------------------------------|
  | 0    | success                                   |
  | 1    | runtime / network / unexpected HTTP       |
  | 2    | usage (unknown command, missing argument) |
  | 3    | config / auth (no key, 401, 403)          |
  | 4    | not found (404)                           |
  | 5    | validation (400)                          |

## The capture grammar

`do capture` quick-adds a task to the inbox from free text with two inline tokens:

- `#tag` — adds a tag (repeatable): `#home #urgent`
- `!priority` — `!high` `!medium` `!low` `!none` (aliases `!h` `!m` `!l` `!n`); last one wins

Both are stripped from the title; standalone only (so `C#` or `10!` in prose is
left alone):

```sh
do capture "Email the landlord about the leak #home !high"
# → task "Email the landlord about the leak", tag home, priority high
```

## Recipes (the daily loop)

```sh
# Capture an idea into the inbox
do capture "Draft Q3 plan #work !medium"

# See what's actionable today (overdue, scheduled, due, in-progress), then the
# habits and routines due today under `.habits`
do today

# From earlier (#888): planned tasks of the last 14 days that weren't done —
# never "late". Answer each with today, later (the quiet day later this week),
# someday (no date, kept in its Area/Project) or let-go (cancelled, not Landed).
do today earlier
do today answer later 01J9Z2K7Q8ABCDEF0123456789 01J9Z2K7Q8ABCDEF0123456790

# Complete a task (idempotent — a no-op success if already done)
do task done 01J9Z2K7Q8ABCDEF0123456789

# Snooze a task forward (default +1 day, or an explicit target)
do task snooze 01J9Z2K7Q8ABCDEF0123456789 --days 3
do task snooze 01J9Z2K7Q8ABCDEF0123456789 --until 2026-07-01

# Log a habit check-in (value defaults to 1; --at for a past time)
do habit log 01J9Z2K7Q8ABCDEF0123456789
do habit log 01J9Z2K7Q8ABCDEF0123456789 --value 30 --at 2026-06-18T21:00:00Z
# Place a habit in the day: morning|midday|evening or "HH:MM" (null = any time)
do habits update 01J9Z2K7Q8ABCDEF0123456789 --data '{"timeOfDay":"morning"}'

# Check in by title or alias, the way a chat message says it ("wake", "12 pages")
do habit check-in wake
do habit check-in pages --value 12                 # adds 12 to today
do habit check-in pages --value 40 --set           # makes today's total 40
do habit check-in drill --at 2026-10-15            # back-date to a day (your time zone)
do habit check-in drill --note "felt heavy"        # "drill done, felt heavy": the rest is a note
# Add or change a note afterwards (the check-in id is lastCheckIn.id in the reply,
# or from `do habit check-ins <id>`); --clear drops it
do habit note 01J9Z2K7Q8ABCDEF0123456789 01J9Z2K7Q8ABCDEF0123456790 "Dune, chapter 9"
# A 409 lists the candidates (error.details.candidates): ask which, then `do habit log <id>`.
do habit alias add 01J9Z2K7Q8ABCDEF0123456789 wake

# What's left today, by part of day (morning, midday, evening, anytime), + routines
do habits today

# Skip and pause, without guilt: a skip or a pause is never a miss
do habit skip 01J9Z2K7Q8ABCDEF0123456789                      # "skip gym today"
do habit skip 01J9Z2K7Q8ABCDEF0123456789 --note "Dentist"     # "skip gym, dentist": the why shows in the log
do habit pause 01J9Z2K7Q8ABCDEF0123456789 --until 2026-10-26  # "pause gym till the 26th"
do habit resume 01J9Z2K7Q8ABCDEF0123456789                    # "gym's back on"
do habit remind 01J9Z2K7Q8ABCDEF0123456789 on                 # "remind me about my drill" (off by default)
do away --until 2026-10-19                                    # "away till Monday"
do away off                                                   # "I'm back"

# A batch (the Apple Medications model): a routine whose steps are habits, e.g.
# "AM Supplements: magnesium, D3, creatine". One call checks in every open step.
do routine done 01J9Z2K7Q8ABCDEF0123456789                    # "took my supplements"
do routine undo <run.id> <taken stepRunIds…>                  # takes the batch back

# Retire a habit to the Grown shelf (history kept), or bring it back
do habit retire 01J9Z2K7Q8ABCDEF0123456789                    # only after they say yes
do habit unretire 01J9Z2K7Q8ABCDEF0123456789                  # "bring back flossing", or Undo
do habits list --retired                                      # the Grown shelf

# Read entities: `do <entity> list` / `do <entity> get <id>`
do tasks list --filter unsorted     # the Inbox: no day, Deadline, Area or Project; never a proposal
do tasks list --proposed            # Proposed by Echo: waiting for the member's Accept
do tasks list --area <areaId> --status todo,in_progress --tag errand --due-before 2026-10-12
do tasks list --updated-since 2026-10-11T08:00:00Z   # what changed since a sync
do areas list --active             # the live Areas to file into (archived ones are put away)
do habits list                      # each carries today { due, done, week? } (on today's schedule?)
do habits list | jq '.[] | select(.today.due) .title'   # what's on today
# "How are my habits going?" — this week's grid, a strength word per habit, patterns
# from the insights worker (each with its confidence) and when you usually check in
do progress habits
do notes get 01J9Z2K7Q8ABCDEF0123456789

# Pipe JSON into jq (auto-JSON because stdout is piped)
do today | jq '.items[] | select(.bucket == "overdue") .title'

# Sync: what changed since your last cursor (store .nextCursor, rerun while .hasMore)
do changes --since now                 # a fresh cursor, no history
do changes --since 812345-12 --entity task,project
```

Readable entities: `tasks`, `habits`, `occurrences`, `shopping-lists`,
`inventory-items`, `recipes`, `meal-plans`, `notes`, `contacts`, `webhooks`.

## Discoverability

Run `do help` for the human overview, or **`do help --json`** for the complete
machine-readable manifest — every command, argument, flag, required scope, return
type, the read entities, auth resolution, and exit codes. Introspect that instead
of trusting this skill when the surface may have grown:

```sh
do help --json | jq '.commands[] | {command, scopes, returns}'
do help --json | jq '.entities[].name'
```

Source + full docs: https://github.com/robbeverhelst/do

## A note on a check-in

When a check-in message carries more than the habit, keep the rest as the
check-in's note (at most 280 characters): "drill done, felt heavy" →
`do habit check-in drill --note "felt heavy"`; "read 12 pages of Dune, chapter 9" →
`do habit check-in pages --value 12 --note "Dune, chapter 9"`. The note shows in the
habit's log beside "Echo, 07:12" and on its day in the year view. To add one later
("add a note: legs were sore"), use `do habit note <habit id> <check-in id> "…"`
with the reply's `lastCheckIn.id`; `--clear` removes it. Don't invent a note when
the message has none.

## Skip, pause and away: what the words mean

When someone says they'll rest from a habit, use these verbs. Never call a skip or
a pause a miss, and never nag about one.

| They say | Run |
|---|---|
| "skip gym today", "rest day for reading" | `do habit skip <id>` (find the id with `do habits list`) |
| "skipped the run yesterday" | `do habit skip <id> --date <yesterday, YYYY-MM-DD>` |
| "pause gym till the 26th", "no gym for two weeks" | `do habit pause <id> --until <the day it's back>` |
| "gym's back on", "resume reading" | `do habit resume <id>` |
| "remind me to do my drill", "stop reminding me about water" | `do habit remind <id> on` / `off`: one push a day at its time, never a follow-up |
| "away till Monday", "on holiday until the 3rd" | `do away --until <the day they're back>` |
| "I'm back", "come back early" | `do away off` |

- `--until` is **the day it's back** (the first day it counts again), and must be
  after today. Resolve "Monday" or "two weeks" to a date first; "till Monday" means
  back on Monday.
- Away rests **every** habit in the Space (off Now, no reminders, plants wait);
  tasks and events carry on. Ask once before going away if it's ambiguous whether
  they mean one habit or all of them.
- A skip shows in `do habit check-ins <id>` with `kind: "skip"`; undo it by
  deleting that entry. A why ("dentist") goes in `--note`. Resting habits carry `pause: { until, by }`.

## Batches: "took my supplements"

A batch is a routine whose steps are habits ("AM Supplements: magnesium, D3,
creatine"). When someone says they took or did the whole thing, check it in with
one call, not one habit at a time.

| They say | Run |
|---|---|
| "took my supplements", "supps done", "took my AM supplements" | `do routine done <routine id>` |
| "took everything except the creatine" | `do habit skip <creatine id>`, then `do routine done <routine id>` |
| "skip the creatine today" | `do habit skip <creatine id>` (the batch leaves it alone) |
| "undo that", "I didn't take them yet" | `do routine undo <run.id> <stepRunIds…>` from the answer |

- Find the routine in `do habits today` (`routines`, with their ids). With an AM
  and a PM batch and no word for which, take the one due now: AM before noon, PM
  after. Ask only if both are still open and it's unclear.
- If there's no routine for it but a single habit ("AM supplements" as one habit),
  check that habit in with `do habit check-in "am supplements"` instead.
- `do routine done` answers with `taken` (what it checked in). A habit already done
  today isn't counted twice, a skipped one stays skipped, and saying it again
  changes nothing. Reply in words ("Magnesium, D3 and creatine are in."), with no
  counts or streaks.

## Retire: when a habit has done its job

Retiring is not deleting. A habit that just happens now (or that no longer fits)
moves to the **Grown** shelf with its plant in bloom and keeps all its history. It
leaves Now and Today, sends no reminders and is never due; Progress keeps its past.

| They say | Do |
|---|---|
| "I'm done with the cold showers habit", "stop tracking flossing" | Offer first: "Retire Cold shower? It moves to Grown with its history." On a yes, `do habit retire <id>` |
| "bring back flossing", "track journaling again" | `do habit unretire <id>` |
| "what have I grown?", "which habits did I retire?" | `do habits list --retired` |

- **Ask before retiring**, and only retire on a clear yes. Then answer with a short
  receipt and an Undo: "Cold shower moved to Grown, history kept. Undo?" Undo is
  `do habit unretire <id>`.
- Never call it quitting or failing, and never delete a habit when they mean retire.
- A retired habit takes no check-in by title (404). If they check one in, offer to
  bring it back first.

### "Still right for you?" (only in a review they asked for)

During a review the person asked for (the Weekly Review, "let's review my week"),
read `do progress habits --json`: each habit has `quietWeeks`, the finished weeks
in a row it was done on less than half of what was due. For a habit at **4 or
more**, you may ask once, gently: "Reading has been quiet for a month. Still right
for you? You could keep it, pause it, or retire it to Grown." Then do what they
choose (`do habit pause`, `do habit retire`, or nothing). Never raise this outside
a review they started, never as a nudge, and never with numbers as pressure.

## An Area's standards: suggest, then apply on a yes

An Area can say what it's for (`purpose`, one line) and what "fine" looks like there
(`standards`, up to five plain sentences). A standard held by a habit, a recurring
task or a Metric says **holding** or **worth a look** with the reason in words; one
with no link is checked by hand in review. Never a score, never a percentage.

- You can **suggest** standards from what's already in the Area: "You have Gym 3× a
  week and Dentist twice a year. Make these Health's standards?" Read the Area first
  (`do areas get <id>`: its habits, routines and recurring tasks) and offer a short
  list with what would hold each.
- **Apply them only on the member's yes**, and only the ones they picked, through
  `do areas standards add` (the v1 endpoint). Each add shows in their change list
  with Undo. Never write standards, or a purpose, into an Area unasked, and never
  reword or remove theirs without being told to.
- "How's Health going?" → `do areas standards list <id>` and answer in its words
  ("Move three times a week is worth a look: one so far this week"). Don't turn it
  into a grade.

```sh
do areas get 01J9Z2K7Q8ABCDEF0123456789
do areas standards add 01J9Z2K7Q8ABCDEF0123456789 "Move three times a week" --habit 01J9Z2K7Q8ABCDEF0123456790
do areas standards list 01J9Z2K7Q8ABCDEF0123456789
```

## Tasks you make for someone arrive as proposals

When you work with an **Agent's key** (you are Echo, or a desk of Echo's) and make a
task with a **member as Owner** (`"owner":"member:robbe@example.com"`), it is
**Proposed by Echo**: it waits at the top of their Inbox with Accept / Not now / Let
go, and stays off their Today, Now and lists until they accept. Your own work
(`"owner":"me/finance"`) is never a proposal.

- Give the reason in `source.label` ("From the KBC statement email") and the Desk you
  write from in `fromDesk` (`finance`). The Inbox shows the reason as the why.
- Suggest the day and Area as usual (`scheduledAt`, `dueAt`, `areaId`); Accept keeps
  them.
- A Desk the member **trusts** (Settings → Agents) skips the proposal and plans
  straight into their week, shown as "Planned by Echo". You can't skip it yourself:
  `proposed:false` from an untrusted Desk is refused (403).
- When they answer in chat: "yes, plan it" → `do tasks accept <id>`; "not now" →
  `do tasks dismiss <id>` (back in their Inbox in a week); "drop it" → `do task cancel
  <id>` (Let go; asks them to confirm first). Your accept shows in their change list
  with Undo.
- Check what still waits with `do tasks list --proposed`.

```sh
do tasks create --data '{"title":"Pay the dentist invoice","owner":"member:robbe@example.com","fromDesk":"finance","dueAt":"2026-10-21","source":{"kind":"email","label":"From the Tandarts Peeters email, 112 euro"}}'
do tasks list --proposed
do tasks accept 01J9Z2K7Q8ABCDEF0123456789
```

## When your work is ready, say so: Ready for you

Your own tasks (`"owner":"me/finance"`) live in the member's **Tasks › With Echo**,
never in their Today. Each reads as one word: **Working on it** (open), **Waiting on
you** / **Waiting on someone** (Waiting on set), **Ready for you**, **Done today**.

- When you finish something the member should look at (a draft invoice, a recap, a
  PR or worktree), mark it **Ready for you** with what's ready in one line and the
  link: `do tasks ready <id> --note "Draft ready: 38 hours, 3,420 euro — <link>"`.
  Put the link in the note (or in `source.url` / a worktree link); the member's
  **Review** opens it. It reaches their Now under Needs you.
- They answer with **Looks good** (the task is done; carry on with what you said
  you'd do next, e.g. send it Monday) or **Send back**, which clears Ready for you and
  writes to you in the chat with what to change. Pick it up from there and mark it
  ready again when it's fixed.
- Don't mark a task ready that needs nothing from them, and never mark one done for
  them: Looks good is theirs. Need an answer instead of a look? Set `waitingOn` to
  them (Waiting on you).
- Check what still waits on their look with `do tasks list --ready`, or one desk's
  work with `do tasks list --owner agent:Echo/finance`.

```sh
do tasks ready 01J9Z2K7Q8ABCDEF0123456789 --note "Recap drafted — https://docs.google.com/document/d/…"
do tasks list --ready --owner agent:Echo/clients
```
