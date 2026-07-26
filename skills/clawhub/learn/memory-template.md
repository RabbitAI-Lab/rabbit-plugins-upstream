# Working File Templates — Learn

Read this file only when WRITING. `config.yaml` is what the learner **declared**; `memory.md` and everything it indexes is what you **observed** or produced. An observation never overwrites a declaration.

## Where each thing goes

| Data | Home | How it grows |
|---|---|---|
| Declared preferences — table keys and preference areas alike | `~/Clawic/data/learn/config.yaml` | Key by key, read-modify-write |
| Status, box index, cadences, topic table, how they learn | `~/Clawic/data/learn/memory.md` | Rewritten in place; stays small |
| The curriculum for one topic — exit test, sequence, cuts, resources, revisions | `~/Clawic/data/learn/plans/<topic>.md` | Born as its own file, from the first topic |
| Review queue: items, intervals, ease, next due | `## Review Queue` in `memory.md` while ≤15 items; `~/Clawic/data/learn/reviews/<topic>.md` past that | One row per item, split per topic |
| Mistakes and the misconception behind each | `## Error Log` in `memory.md` while ≤15 entries; `~/Clawic/data/learn/errors/<topic>.md` past that | One row per mistake, split per topic |
| Topics and their mastery level | `## Topics` in `memory.md` while ≤15; `~/Clawic/data/learn/topics.md` past that | One row per topic |
| Resources judged — finished, abandoned, kept for lookup | `## Resources` in `memory.md` while ≤15; `~/Clawic/data/learn/resources.md` past that | One row per resource |
| Practice sessions: date, topic, minutes, success rate, what was produced | `~/Clawic/data/learn/sessions/<year>.md` | Append-only, cut by year |
| Things produced that get re-read — cheat sheets, explanations written from memory, assessments and their results, a decision about how to learn this | `~/Clawic/data/learn/artifacts/<kebab-name>.md` | Born as its own file, from the first one |
| A build-to-learn project | `~/Clawic/data/projects/<project>.md` (**shared**) | One file per project; named here as a pointer only |
| A mentor, tutor, language partner, reviewer or study group contact | `~/Clawic/data/contacts/contacts.md` (**shared**) | One row per person; named here as a pointer only |
| A paid recurring course, tutor or platform subscription | `~/Clawic/data/finances/subscriptions.md` (**shared**) | One row per subscription, with currency |
| **Anything durable this table does not name** | `~/Clawic/data/learn/<plural-noun>.md`, or `artifacts/<kebab-name>.md` if it is a long text read whole | Name the file after what it holds, never after when it was made; add its `## Boxes` line in the same turn |
| Credentials of any kind | Nowhere under `~/Clawic/data/` | Pointer only — see Secrets |

## When to write

No permission needed, no announcement beyond one line.

| It happened | Write |
|---|---|
| A plan was written, revised, or its exit test changed | `plans/<topic>.md`, and the revision line inside it |
| A topic was started, promoted a mastery level, paused or retired | Its row in `## Topics` |
| Items were added to the queue, or graded in a review | The queue rows (interval, ease, next due, lapses) |
| A mistake was made and its cause identified | `## Error Log` — the misconception, not just the wrong answer |
| A practice session ran | A row in `sessions/<year>.md` with minutes and success rate |
| A resource was finished, abandoned, or demoted to lookup | `## Resources`, with the verdict in one clause |
| A cheat sheet, a from-memory explanation, an assessment, or a how-to-learn-this decision came out of the session | `artifacts/` |
| The learner started building something to learn with | `~/Clawic/data/projects/<project>.md`, referenced by name in the plan |
| A mentor, reviewer or partner entered the loop — or left it | `~/Clawic/data/contacts/contacts.md`: the row, added or deleted, with the date of a departure noted in `memory.md` |
| A paid course or platform was subscribed to or cancelled | `~/Clawic/data/finances/subscriptions.md` |
| A cadence was agreed or run (review day, plan review, maintenance touch) | `## Due` |
| The learner declared a preference | Its key in `config.yaml` |

## Start flat, split only when it hurts

Plans, artifacts, session logs and the shared boxes are the exceptions: they are born as their own file. Everything else begins inside `memory.md`. Splitting is a procedure, not a suggestion:

1. **Who**: the agent about to append. **When**: count the section's entries *before* adding the one that would cross the line.
2. If the append would take it past **~15 entries or ~40 lines of real content** — scaffolding, headings and comments do not count, and in tables the entry count decides — then, in the same turn: create the new file under `~/Clawic/data/learn/`, move the whole section into it, **delete the section from `memory.md`**, add its line to `## Boxes`, and append the new entry to the new file.
3. Keep the headings identical on both sides of the move, so the split is a copy-paste and never a rewrite. `## Review Queue` and `## Error Log` split **per topic** (the queue for one topic is what a session actually opens); `## Topics` and `## Resources` split whole, into one file each.
4. **Precedence**: never leave a copy behind. If the same data ever appears in both places, the extracted file wins and the `memory.md` copy is deleted in that turn.

## Secrets

Nothing under `~/Clawic/data/` ever holds a secret value — not the files named here, not files you create, not text the learner pastes in and asks you to keep. Store the pointer in its place, in this shape: `<kind>:<locator>`.

`env:OPENAI_API_KEY` · `keychain:duolingo` · `1password:Personal/Coursera` · `bitwarden:Learning/italki` · `file:~/.ssh/id_ed25519` · `profile:school`

When the learner pastes something to save — a course login, an API key inside a practice snippet, an exported `.env` from a tutorial project — replace each secret value before writing and leave the pointer visible: `api_key: <env:OPENAI_API_KEY>`. Say in one line that you did it.

In this domain — **not secrets, keep them**: course and platform names, usernames and handles, deck and topic names, mentor names, book and paper titles, ISBNs, class times, prices with currency, the last four digits of a card on a subscription row. **Secrets, strip them**: passwords and passphrases, API keys inside practice code, session cookies and tokens, licence keys, exam-portal credentials, anything in a pasted `.env`, private keys.

**Contents:** [config.yaml](#configyaml) · [memory.md](#memorymd) · [plans/](#plans) · [reviews/](#reviews) · [errors/](#errors) · [sessions/](#sessions) · [artifacts/](#artifacts) · [shared projects box](#shared-projects-box) · [shared contacts box](#shared-contacts-box) · [shared subscriptions box](#shared-subscriptions-box) · [split-out files](#split-out-files)

## config.yaml

Keys come from the Configuration table in `SKILL.md`, plus free-form keys nested under a preference area. Write a key only when the learner states the preference.

**Writing is read-modify-write**: load the existing file, set or replace only the key just declared, keep every other key byte for byte. Never emit a `config.yaml` from this template — the template shows shape, not content. Create `~/Clawic/data/learn/` if it does not exist.

```yaml
weekly_hours: 6
session_minutes: 50
daily_review_limit: 30
retention_target: 0.9
hint_policy: after-attempt
sr_tool: anki
practice_bias: projects
plan_review_weeks: 4

# Preference areas — free-form keys added as the learner reveals them.
# A preference the learner states is a declaration and belongs here, never in memory.md.
tooling:
  notes: obsidian
  drills: repl
conventions:
  item_form: cloze
accountability:
  streaks: false
  report_missed: true
cadence:
  review_day: sunday
```

If you find a preference recorded in `memory.md`, move it here and note the move.

## memory.md

Write only the sections you have content for — a heading with nothing under it is noise, and it inflates the line count that decides a split. Never copy these hints into the learner's file. `## Boxes` is the one section that is never dropped when `memory.md` is rewritten: deleting a line there orphans a file forever. This is what a populated file looks like:

```markdown
# Learn Memory

## Status
status: ongoing
last: 2026-07-26

## Boxes
- Rust plan (exit test + 6 stages) → `plans/rust.md`; read before any Rust session or scope change
- Rust review queue (140 items) → `reviews/rust.md`; read at the start of every Rust session
- Rust error log (31 entries) → `errors/rust.md`; read before designing a drill or a test
- Borrow-checker cheat sheet (1 page, 12 rules) → `artifacts/cheatsheet-borrow-checker.md`; read when ownership errors come up
- Transfer test, Rust stage 4 (task + 2 attempts) → `artifacts/assessment-rust-stage4.md`; read before re-testing or promoting
- Practice sessions (2026) → `sessions/2026.md`; read for the weekly retro and the plan review

## Due
| What | Every | Last run | Next due |
|------|-------|----------|----------|
| Review queue | day | 2026-07-25 | 2026-07-26 |
| Weekly retro | week, sunday | 2026-07-19 | 2026-07-26 |
| Plan review | 4 weeks | 2026-07-05 | 2026-08-02 |
| Maintenance: SQL windows | 60 days | 2026-06-20 | 2026-08-19 |

## Topics
| Topic | Goal / exit test | Level | Started | Last practised | Verified | Plan |
|-------|------------------|-------|---------|----------------|----------|------|
| Rust | Ship a CLI with tests from a blank repo in a weekend | Application | 2026-04-02 | 2026-07-25 | — | `plans/rust.md` |
| SQL windows | Rewrite 5 reporting queries with window functions, unaided | Retention | 2025-11-10 | 2026-06-20 | 2026-06-20 (transfer, cold) | `plans/sql-windows.md` |
| Piano — sight reading | Play an unseen grade-3 piece at tempo, first attempt | paused 2026-05-01 (weekly_hours cut) | 2026-01-15 | 2026-04-28 | — | `plans/piano-sight-reading.md` |

## Review Queue
| Item | Topic | Added | Interval (d) | Ease | Last | Next | Lapses | Conf |
|------|-------|-------|--------------|------|------|------|--------|------|
| When does a move happen vs a borrow | Rust | 2026-07-02 | 6 | 2.3 | 2026-07-20 | 2026-07-26 | 1 | 4 |

## Error Log
| Date | Topic | What went wrong | Misconception behind it | Fixed by |
|------|-------|-----------------|-------------------------|----------|
| 2026-07-20 | Rust | Cloned to silence the borrow checker | Thought lifetimes were a compiler quirk, not the model | Drill: rewrite 5 clones as borrows |

## Resources
| Resource | Type | Topic | Verdict | Date |
|----------|------|-------|---------|------|
| The Rust Book | book | Rust | primary, ch. 1-10 done | 2026-05-30 |
| Rustlings | exercises | Rust | finished — best difficulty match so far | 2026-06-14 |
| A 40-hour video course | video | Rust | abandoned at 3h — recognition only, no production | 2026-04-20 |

## How They Learn
Retains procedures, forgets vocabulary. Interleaving works; streaks backfire (two abandoned runs).
Needs the production step early or the session becomes reading.

---
*Updated: 2026-07-26*
```

Rules that keep this readable next month:

- **`## Boxes`**: one line per file that exists — `<what> (<volume>) → <file>; read when <condition>`. Written in the same turn the file is created. Never delete a line without deleting the file it points to. A box with no index line does not exist.
- **`## Due`**: check it against today's date at the start of a session and state any overdue item in one line — a statement, not a question. Every recurring thing this skill schedules (review day, weekly retro, `plan_review_weeks`, each verified topic's maintenance touch) belongs here.
- **`## Topics`**: one row per topic, and `Level` uses the Mastery Ladder names from `SKILL.md`. A promotion carries the date and the test that produced it in `Verified` — never a self-report. Retirement is part of the record: set `Level` to `paused <date> (<reason>)` or `retired <date> (<reason>)` rather than deleting the row, because "I stopped on purpose" is the fact that stops the topic resurfacing as guilt. Delete the row only when its plan and queue are deleted too.
- **`## Review Queue`**: `Interval` in days, `Ease` starting at 2.5 with a 1.3 floor, `Conf` the learner's 1-5 confidence rating recorded **before** the answer was revealed — the pair (`Conf` high, graded wrong) is the calibration signal and the reason the column exists. An item at 5+ `Lapses` is a leech: reformulate or drop it, and note which in `## Error Log`.
- **`## Error Log`**: the `Misconception` column is the point of the table. A row that only records the wrong answer produces the same mistake next month.
- **`## Resources`**: `Verdict` is one clause and always includes why — an abandoned resource with no reason gets picked up again in six months.
- With `sr_tool` set to anything but `this-skill`, do not mirror the external deck here: keep `## Due` (review cadence), leeches, and the daily workload number only, and say where the queue actually lives.
- These headings are exactly the ones the split-out files get, so the split stays a copy-paste.

| Status | Meaning |
|-------|---------|
| `ongoing` | Topics in flight, plan still moving |
| `maintenance` | Nothing new being learned; only `## Due` touches remain |
| `complete` | Every topic verified or retired |

## plans/

One file per topic at `~/Clawic/data/learn/plans/<topic>.md`, created with the topic — a plan is read whole, at the start of a topic's session and whenever scope moves.

```markdown
# Plan — Rust
*Read before any Rust session or scope change. Started 2026-04-02.*

Exit test: ship a CLI with subcommands, tests and error handling from a blank repo in one weekend, no tutorial open.
Budget: 6 h/week → 40-80 h → 7-14 weeks (range, not a date).

| Stage | Capability it adds | Its own test | Status |
|-------|--------------------|--------------|--------|
| 1 | Ownership and borrowing | Explain 5 compiler errors without the book | done 2026-04-28 |
| 2 | Error handling with Result | Rewrite a panic-heavy script | done 2026-05-19 |

Cut, on purpose: async, macros, unsafe — not in the exit test. Revisit only if the test changes.
Primary resource: The Rust Book. Everything else is lookup.
Project: `~/Clawic/data/projects/rust-cli.md`.

## Revisions
- 2026-06-01: 8 h/week was fiction, re-sized to 6; range moved to 7-14 weeks.
```

Every revision gets a dated line rather than a silent edit: a plan whose history is invisible cannot be checked against reality at `plan_review_weeks`.

## reviews/

Created by the split, one file per topic, with the exact `## Review Queue` headings from `memory.md`. Sorted by `Next`, oldest first, so the due set is the top of the file.

```markdown
# Review Queue — Rust

| Item | Topic | Added | Interval (d) | Ease | Last | Next | Lapses | Conf |
|------|-------|-------|--------------|------|------|------|--------|------|
| When does a move happen vs a borrow | Rust | 2026-07-02 | 6 | 2.3 | 2026-07-20 | 2026-07-26 | 1 | 4 |

## Suspended
| Item | Why | Date |
|------|-----|------|
| Lifetime elision rules | Leech at 5 lapses; reformulated into 3 atomic items | 2026-07-11 |
```

## errors/

Created by the split, one file per topic, same headings as `## Error Log`, newest last. This is the highest-value file in the folder: it is the only place that says what this learner specifically gets wrong, and it is what a drill or a transfer test should be built from.

## sessions/

Append-only, cut by year. Never inside `memory.md`: a log that grows every session would push the whole file past its split threshold within a month.

```markdown
# Practice Sessions — 2026

| Date | Topic | Minutes | Hard block | Success rate | Produced | Note |
|------|-------|---------|------------|--------------|----------|------|
| 2026-07-25 | Rust | 50 | traits + generics | 12/15 | subcommand parser, no tutorial | difficulty on target |
| 2026-07-23 | Rust | 20 | short session | 7/8 | — | retrieval + production only |
```

`Success rate` is hits over attempts in the hard block, and the reason the column exists: Rule 4 needs the last 20 attempts, and nobody can reconstruct them from memory a week later.

## artifacts/

One file per thing, at `~/Clawic/data/learn/artifacts/<kebab-name>.md`, created the first time it exists. Canonical types here: **cheat sheet** (the compressed reference the learner derived themselves), **written explanation** (produced from memory — the artifact of the Teaching level), **assessment** (a transfer test and its result), **learning decision** (what was tried, what was rejected, and why). Every artifact opens with when to read it, and gets its `## Boxes` line in the same turn.

```markdown
# Cheat sheet — borrow checker
*Read when ownership or lifetime errors come up. Written 2026-07-12 from the error log, not from the book.*
```

```markdown
# Assessment — Rust, stage 4 transfer test
*Read before re-testing or promoting this topic. 2026-07-18.*

Task: unseen problem, different crate, 90 minutes, no notes.
Result: 4/5 — failed on trait objects, added 3 items to the queue.
Level reached: Application. Retention re-test due 2026-08-17 (`## Due`).
```

A test written once is reusable: keep the task and the rubric, append each attempt's date and result, so "did it improve" is answerable.

## Shared projects box

Lives at `~/Clawic/data/projects/<project>.md` and is shared with every other skill that tracks work — the learner may have none of them installed, so the format travels with this skill. Write here when the learner builds something in order to learn.

```markdown
# rust-cli
status: active
goal: CLI with subcommands, tests, error handling — the Rust exit test
started: 2026-05-04
learning: Rust (`~/Clawic/data/learn/plans/rust.md`)

## Milestones
- 2026-06-02 — argument parsing done without copying
```

- **Identity is the file name** (the project slug). Read the folder before creating: if a file for this project already exists, add to it in place — never a second file for the same project under a different slug.
- **Retirement is a status, not a deletion**: `status: done | cancelled — <date>` inside the file. The record of what was shipped is the point. Past ~20 closed projects, move them to `projects/archive/<project>.md` without renaming.
- **Foreign structure wins.** If the file or folder already uses different headings, match them and add what is missing as a trailing section. Never rewrite someone else's layout.
- The learning topic stays in `## Topics` here; the project file carries only the pointer back. One entity, one home.

## Shared contacts box

Lives at `~/Clawic/data/contacts/contacts.md`. Write here when a mentor, tutor, language partner, code reviewer or study-group organiser becomes part of the loop.

```markdown
# Contacts

| Name | Key | Role | Preferred channel | Context | Last contact | File |
|------|-----|------|-------------------|---------|--------------|------|
| Marta Ruiz | marta@example.com | Rust reviewer | email | reviews the CLI weekly, 48h turnaround | 2026-07-21 | — |
```

- **Identity is `Key`**: lowercase email if there is one, otherwise a handle, otherwise `<kebab-name>` plus a stable disambiguator. `Key` is a column of the row, never implicit. `Preferred channel` is the *type* of channel, not the address, so it can never serve as the key.
- **Read before adding.** If the `Key` is already there, update that row in place — never append a second row for the same person, and never edit a row this skill did not create beyond adding a missing field.
- **Leaving the loop is a deletion, not a stale row.** When a mentor, tutor, language partner or reviewer stops being part of the learning — the topic was retired, the tutoring ended, the study group dissolved — delete their row and note the date in `memory.md`, as a dated clause in the topic's `## Topics` row if the loop was that topic's, otherwise a line under `## How They Learn`. Delete only rows this skill wrote; a row another skill owns stays untouched. An inventory that only grows stops being an inventory, and a reviewer who left two years ago still reads as available feedback.
- **Amounts carry their currency in the value** (`40 EUR/h`), because rows written by other skills may be in another currency.
- **Scale cut**: one row per person while there are ≤15, or until one no longer fits its row. Past that, `~/Clawic/data/contacts/<name>.md` per person and `contacts.md` becomes the index with the `File` pointer. If the folder already looks like that, follow it — do not start a parallel `contacts.md`.
- **Foreign columns win.** If the file exists with a different column set, match its columns and add anything missing as a trailing note. Never rewrite its header.
- Contact details only. Never a password, a portal login, or a payment detail.

## Shared subscriptions box

Lives at `~/Clawic/data/finances/subscriptions.md`. Write here only when the learner names a **recurring paid** course, tutor or platform — a one-off book purchase belongs in `## Resources`, not here.

```markdown
# Subscriptions

| Service | Purpose | Amount | Cycle | Started | Renews | Status |
|---------|---------|--------|-------|---------|--------|--------|
| italki | Italian tutor, 2 h/week | 96 EUR | monthly | 2026-03-01 | 2026-08-01 | active |
```

- **Identity is the service name.** Read the file before adding; if the row exists, update it in place.
- **Cancellation deletes the row** and gets a dated line in `memory.md` under `## Resources`. A subscriptions table that only grows stops being usable — and this table is exactly where the abandoned course nobody cancelled shows up.
- **Amounts carry their currency in the value** (`96 EUR`), and estimated amounts carry the date of the estimate.
- **Foreign columns win**: match the existing header, add what is missing as a trailing note.
- Never a card number beyond the last four digits, never a portal login.

## Split-out files

Created only by the split procedure above, never on day one. Each keeps the exact headings it had inside `memory.md`.

`topics.md` — `## Topics`, one row per topic, with the retired and paused rows kept. It is the answer to "what have I actually learned", which is unanswerable once the rows are scattered.

`resources.md` — `## Resources`, plus a `## Lookup Shelf` heading for the ones demoted to reference rather than abandoned, so a demoted book is not re-evaluated as a candidate every quarter.
