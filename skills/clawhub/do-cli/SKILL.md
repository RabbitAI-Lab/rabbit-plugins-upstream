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

# See what's actionable today (overdue, scheduled, due, in-progress)
do today

# Complete a task (idempotent — a no-op success if already done)
do task done 01J9Z2K7Q8ABCDEF0123456789

# Snooze a task forward (default +1 day, or an explicit target)
do task snooze 01J9Z2K7Q8ABCDEF0123456789 --days 3
do task snooze 01J9Z2K7Q8ABCDEF0123456789 --until 2026-07-01

# Log a habit check-in (value defaults to 1; --at for a past time)
do habit log 01J9Z2K7Q8ABCDEF0123456789
do habit log 01J9Z2K7Q8ABCDEF0123456789 --value 30 --at 2026-06-18T21:00:00Z

# Read entities: `do <entity> list` / `do <entity> get <id>`
do tasks list --filter unsorted     # the GTD inbox
do habits list
do notes get 01J9Z2K7Q8ABCDEF0123456789

# Pipe JSON into jq (auto-JSON because stdout is piped)
do today | jq '.items[] | select(.bucket == "overdue") .title'
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
