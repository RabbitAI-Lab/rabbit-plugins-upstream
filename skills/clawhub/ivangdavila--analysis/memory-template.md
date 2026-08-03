# Working File Templates — Analysis

Read this file only when WRITING. `config.yaml` is what the user **declared**; `memory.md` and everything it indexes is what you **observed** or produced. An observation never overwrites a declaration.

## Where each thing goes

| Data | Home | How it grows |
|---|---|---|
| Declared preferences — table keys and preference areas alike | `~/Clawic/data/analysis/config.yaml` | Key by key, read-modify-write |
| Setup baseline, open findings, acceptances, credential inventory, spend, due dates, box index | `~/Clawic/data/analysis/memory.md` | Rewritten in place; stays small |
| Findings still open, with severity, first-seen date and action | `## Open Findings` in `memory.md`; `findings.md` past the split threshold | One row per finding |
| Things the user decided are fine | `## Accepted` in `memory.md`; `suppressions.md` past the threshold | One row per acceptance, each with a review date |
| Where credentials live, their kind, owner and expiry — pointers only | `## Credential Inventory` in `memory.md`; `credentials.md` past the threshold | One row per credential |
| What the setup consists of: paths, jobs, integrations, allowlist posture, measured sizes and timings | `## System Baseline` in `memory.md`; `baseline.md` past the threshold | Rewritten as it is re-measured |
| Monthly token spend and the savings that landed | `## Spend` in `memory.md`; `spend-log.md` past the threshold | One row per month, overwritten within the month |
| Audit runs and the fixes applied in them | `~/Clawic/data/analysis/runs/<year>.md` | Append-only, cut by year — never inside `memory.md` |
| Things you produced that get re-read — incident write-ups, runbooks, health reports, posture decisions | `~/Clawic/data/analysis/artifacts/<kebab-name>.md` | Born as its own file, from the first one |
| Hosts that run or serve the agent | `~/Clawic/data/servers/servers.md` (**shared**) | One row per host, every provider in one inventory |
| Paired non-server devices (phone, tablet, single-board machine) | `~/Clawic/data/devices/devices.md` (**shared**) | One row per device |
| Recurring paid services the audit turns up | `~/Clawic/data/finances/subscriptions.md` (**shared**) | One row per subscription, amount with currency |
| A person who owns a credential, a job, or an account | `~/Clawic/data/contacts/contacts.md` (**shared**); referenced here by name only | One row per person |
| **Anything durable this table does not name** | `~/Clawic/data/analysis/<plural-noun>.md`, or `artifacts/<kebab-name>.md` if it is a long text read whole | Name the file after what it holds, never after when it was made; add its `## Boxes` line in the same turn |
| Credentials of any kind | Nowhere under `~/Clawic/data/` | Pointer only — see Secrets |

## When to write

No permission needed; every write is announced in one line that names the file. Writes and deletions stay inside the paths declared in this skill's `configPaths`. A deletion is named in that same line, and in a shared box only rows this skill itself wrote are ever updated or removed.

| It happened | Write |
|---|---|
| An audit run finished, whatever it found | A row in `runs/<year>.md`, with phases run and phases skipped |
| A finding survived the run | Its row in `## Open Findings`, with first-seen date |
| A finding was fixed | Close its row; the fix, its inverse and its verification go in the run row |
| The user said something is fine, intentional, or not worth fixing | `## Accepted`, with scope and review date |
| A credential was found, rotated, or given an expiry | `## Credential Inventory` — pointer, kind, owner, expiry; never the value |
| A job, integration, tool server, path or allowlist posture was discovered or changed | `## System Baseline` |
| Spend was reviewed, or a saving landed | `## Spend` |
| Startup, task latency or always-loaded size was measured | `## System Baseline` |
| An incident, a repair procedure, a posture decision, or a report for a human came out of the session | `artifacts/` |
| A host, a paired device, or a paid service was identified | The matching shared box |
| A cadence was agreed or a scheduled check ran | `## Due` |
| The user declared a preference | Its key in `config.yaml` |

## Start flat, split only when it hurts

Everything except runs, artifacts and the shared boxes begins inside `memory.md`. Splitting is a procedure, not a suggestion:

1. Before appending to a section, count its entries.
2. If the append would take it past **~15 entries or ~40 lines of real content** — scaffolding, headings and comments do not count — then, in the same turn: create the new file in `~/Clawic/data/analysis/`, move the whole section into it, **delete the section from `memory.md`**, add its line to `## Boxes`, and append the new entry to the new file.
3. Keep the headings identical on both sides of the move, so the split is a copy-paste and never a rewrite.
4. Never leave a copy behind. If the same data ever appears in both places, the extracted file wins and the `memory.md` copy is deleted.

Two exceptions: **runs** are a temporal log and live in `runs/<year>.md` from the first run, never inside `memory.md`; **artifacts** are born as their own file whatever their size, because they are read whole and only when their subject comes up.

## Secrets

Nothing under `~/Clawic/data/` ever holds a secret value — not the files named here, not files you create, not text the user pastes in and asks you to keep, and not a finding that quotes the line where the secret was found. Store the pointer in its place, in this shape: `<kind>:<locator>`.

`env:GITHUB_TOKEN` · `keychain:deploy-bot` · `1password:Work/API/prod` · `bitwarden:Personal/Registry` · `vault:secret/data/prod/api` · `ssm:/prod/db/password` · `secretsmanager:prod/api/key` · `profile:prod` · `file:~/.ssh/id_ed25519`

When the user pastes something to save, replace each secret value before writing and leave the pointer visible: `password: <ssm:/prod/db/password>`. Say in one line that you did it.

In this domain — **not secrets, keep them**: file paths and line numbers, credential *kinds* and prefixes as a class name (never the matched string), environment variable names, account and project ids, usernames and emails, hostnames, port numbers, job names and schedules, skill slugs, expiry dates, key fingerprints, public keys, profile names. **Secrets, strip them**: access keys and secret keys, session tokens, passwords and passphrases, private key bodies, JWTs, OAuth client secrets, refresh tokens, webhook signing secrets, connection strings carrying a password, external-id values, one-time codes, and any matched substring long enough to be usable.

**Contents:** [config.yaml](#configyaml) · [memory.md](#memorymd) · [runs/](#runs) · [artifacts/](#artifacts) · [shared servers inventory](#shared-servers-inventory) · [shared devices inventory](#shared-devices-inventory) · [shared subscriptions](#shared-subscriptions) · [shared contacts](#shared-contacts) · [split-out files](#split-out-files)

## config.yaml

Keys come from the Configuration table in `SKILL.md`, plus free-form keys nested under a preference area. Write a key only when the user states the preference.

**Writing is read-modify-write**: load the existing file, set or replace only the key just declared, keep every other key byte for byte. Never emit a `config.yaml` from this template — the template shows shape, not content. Create `~/Clawic/data/analysis/` if it does not exist.

```yaml
default_mode: quick
autofix_policy: safe-only
workspace_paths:
  - ~/work/main-project
  - ~/work/ops
excluded_paths:
  - ~/work/client-*/**
audit_cadence: monthly
secret_rotation_days: 90
memory_budget_mb: 5
max_findings_shown: 10
secret_store: keychain

# Preference areas — free-form keys added as the user reveals them.
# A preference the user states is a declaration and belongs here, never in memory.md.
tooling:
  search: rg
  stat_flavor: bsd
safety_posture:
  history_rewrite: never
  kill_sessions: propose-only
escalation:
  private_repo_read_token: warning   # not critical in this setup
output_register: terse-grouped-by-severity
```

If you find a preference recorded in `memory.md`, move it here and note the move.

## memory.md

Write only the sections you have content for — a heading with nothing under it is noise, and it inflates the line count that decides a split. Never copy these hints into the user's file. `## Boxes` is the one section that is never dropped when `memory.md` is rewritten: deleting a line there orphans a file forever. This is what a populated file looks like:

```markdown
# Analysis Memory

## Status
status: ongoing
last: 2026-07-26

## Boxes
- Audit runs and fixes (2026) → `runs/2026.md`; read before comparing counts or claiming a trend
- Permission posture and what it rejected → `artifacts/permission-posture.md`; read before changing any grant
- July health report → `artifacts/health-report-2026-07.md`; read when someone asks how the setup is doing
- Checkout job runbook → `artifacts/job-nightly-sync-runbook.md`; read the moment the nightly sync fails

## Due
| What | Every | Last run | Next due |
|------|-------|----------|----------|
| Full audit | month | 2026-06-28 | 2026-07-28 |
| Quick check | week | 2026-07-20 | 2026-07-27 |
| Acceptance review | quarter | 2026-05-02 | 2026-08-02 |
| Restore drill | quarter | 2026-04-11 | 2026-07-11 |
| Deploy token reissue | on 2026-09-14 | — | 2026-08-31 (warn) |

## System Baseline
Workspace: ~/work/main-project (repo, remote origin) · data root ~/Clawic/data
Always-loaded: 3 files, 18 KB (~4.5k tokens/turn); largest is the instruction file at 11 KB
Jobs: 4 (nightly-sync 02:30 UTC, weekly-report Mon 09:00, hourly-poll, backup 03:15 UTC)
Integrations: 3 APIs, 1 tool server (11 tools), 1 webhook
Allowlist: 12 entries, no shell forms, write scope = project only, config tracked in git
Measured: startup 4.1s · representative task p95 38s · memory tree 3.2 MB
Last full inventory: 2026-07-26

## Open Findings
| ID | Sev | Phase | Finding | First seen | Action |
|----|-----|-------|---------|------------|--------|
| F-031 | WARNING | scheduled | nightly-sync has no dead-man's switch | 2026-05-28 | Add absence alert at 2× interval |
| F-044 | WARNING | secrets | deploy token has no expiry, age 140d | 2026-07-26 | Set rotation date, reissue with expiry |
| F-045 | INFO | skills | 2 skills unfired in 60d with domain activity | 2026-07-26 | Rewrite first sentences or uninstall |

## Accepted
| Rule | Scope | Reason | Accepted | Review |
|------|-------|--------|----------|--------|
| memory tree over budget | `~/work/main-project/notes/**` | Archive kept on purpose, read rarely | 2026-06-02 | 2026-09-02 |
| skill overlap | `writing` vs `editing` | Wants both, picks manually | 2026-04-18 | 2026-07-18 (overdue) |

## Credential Inventory
| Name | Kind | Pointer | Owner | Issued | Expires | Rotation |
|------|------|---------|-------|--------|---------|----------|
| deploy token | code host PAT | `keychain:deploy-bot` | us | 2026-03-08 | none | set one |
| model API key | provider key | `env:MODEL_API_KEY` | us | 2026-01-12 | none | 2026-10-12 |
| sync service | OAuth refresh | `1password:Work/Sync/prod` | ops (see contacts) | 2026-06-01 | 2026-09-14 | reissue by 08-31 |

## Spend
| Month | Amount | As of | Top drivers | Notes |
|-------|--------|-------|-------------|-------|
| 2026-06 | 96 USD | 2026-06-30 | history 41 · always-loaded 22 · jobs 18 | closed |
| 2026-07 | 34 USD | 2026-07-26 | history 15 · jobs 11 · always-loaded 6 | month-to-date |
Anomaly baseline: median 3.1 USD/day, MAD 0.6, floor 4.7 USD

## How They Work
Wants the finding and the command, not the reasoning. Fixes things immediately or never.

---
*Updated: 2026-07-26*
```

Rules that keep this readable next month:

- **`## Boxes`**: one line per file that exists — `<what> (<volume>) → <file>; read when <condition>`. Written in the same turn the file is created. Never delete a line without deleting the file it points to. A box with no index line does not exist.
- **`## Due`**: check it against today's date at the start of a session and state any overdue item in one line — a statement, not a question. Credential expiries appear here as a warn date, not the expiry itself.
- **`## Open Findings`**: `ID` is stable for the life of the finding (`F-<n>`, monotonic) so recurrence can be counted. `First seen` never changes — a reopened finding keeps its original date and gains a note in the run row. Closing a finding means deleting the row, with the closure recorded in `runs/<year>.md`.
- **`## Accepted`**: five fields, all required. Past its review date the row is *raised* on the next run, not honored.
- **`## Credential Inventory`**: pointers only, and the row for a credential the audit found in plaintext keeps its status until rotation is verified (`secrets.md`).
- **`## Spend`**: `As of` is the day the number was read. Re-checking the current month **overwrites** its row; never a second row for the same month. Amounts always carry their currency.
- These headings are exactly the ones the split-out files get, so a split stays a copy-paste.

| Status | Meaning |
|-------|---------|
| `ongoing` | Still mapping the setup; phases remain unrun |
| `complete` | Full audit has covered every phase at least once and the baseline is current |

## runs/

Append-only, one file per year, from the first run — never inside `memory.md`.

```markdown
# Analysis Runs — 2026

| Date | Mode | Phases run | Skipped (why) | CRIT | WARN | INFO | Opened | Closed | Suppressed |
|------|------|-----------|---------------|------|------|------|--------|--------|------------|
| 2026-07-26 | full | 1-10 | — | 0 | 2 | 3 | 2 | 1 | 1 |
| 2026-07-20 | quick | 1-3 | 4-10 (mode) | 0 | 1 | 0 | 1 | 0 | 0 |

## Fixes
| Date | Finding | Change | Inverse recorded | Verified | Held |
|------|---------|--------|------------------|----------|------|
| 2026-07-26 | F-029 | key file 644 → 600 | mode 644 | re-stat clean | yes |
| 2026-07-20 | F-018 | broke stale lock (pid 4411, 6d old) | holder recorded | job ran once | yes |

## Threshold changes
| Date | Key | From | To | Why |
|------|-----|------|----|-----|
| 2026-06-14 | memory_budget_mb | 5 | 8 | archive kept deliberately |
```

The `Skipped` and `Threshold changes` columns exist so a dip in the counts is never mistaken for an improvement.

## artifacts/

One file per thing, at `~/Clawic/data/analysis/artifacts/<kebab-name>.md`, created the first time it exists. Canonical types here: **incident write-up**, **repair runbook**, **posture decision**, **health report**, **skill edit log**. Every artifact opens with when to read it, and gets its `## Boxes` line in the same turn.

```markdown
# Incident — deploy token in committed config
*Read when a credential leak is suspected, or before anyone asks why that token changed. 2026-07-26.*

Leaked: code host PAT, repo-scoped write, `keychain:deploy-bot`.
Exposure: added 2026-05-02, private remote, no forks; revoked 2026-07-26.
Used by anyone else: no — access log clean for the window.
Changed: reissued with 90-day expiry, value moved to the keychain, `.env` added to ignore rules.
Still open: history rewrite proposed, declined for now (see Accepted).
```

```markdown
# Posture decision — unattended jobs run read-only
*Read before granting any new permission or adding a scheduled job. 2026-07-26.*

Decision: jobs run at scope rung 2 — read-only, project paths, egress to two named hosts.
Rejected: full allowlist reuse from the interactive setup — a triggered run has no attention behind it.
Cost: two jobs need a human step monthly. Accepted deliberately.
```

## Shared servers inventory

Lives at `~/Clawic/data/servers/servers.md` and is shared with every other infrastructure skill — the user may not have any of them installed, so the format travels with this skill.

```markdown
# Servers

| Name | Provider | Account / Project | Region | Type | Role | Monthly | Access reference |
|------|----------|-------------------|--------|------|------|---------|------------------|
| agent-box-1 | hetzner | personal | fsn1 | cx22 | runs scheduled agent jobs | 5 EUR | file:~/.ssh/id_ed25519 |
```

- **Identity is `Name` + `Provider`.** Read the file before adding. If that pair is already there, update the row in place — it is yours. Never touch a row whose `Provider` points at a machine this audit did not verify.
- **Retirement is part of the inventory.** When a host is decommissioned, delete its row and note the date in `memory.md`. An inventory that only grows stops being an inventory.
- **Amounts carry their currency in the value** (`5 EUR`), because rows from other providers are in other currencies and someone will add the column up.
- **Scale cut**: one row per host while there are ≤15. Past that, one file per host at `~/Clawic/data/servers/<name>.md` with the same fields, and `servers.md` becomes the index (`Name | Provider | Role | → file`). If the folder already looks like that, follow it — never start a parallel `servers.md`.
- **Foreign columns win.** If the file already exists with a different column set, match its columns and add anything missing as a trailing note. Never rewrite its header.
- Access reference is a pointer only. Never a key, token, or password.

## Shared devices inventory

Lives at `~/Clawic/data/devices/devices.md`, shared with home-automation and hardware skills. Only for non-server devices paired with the setup — a phone running the client, a tablet, a single-board machine that is not a host.

```markdown
# Devices

| Name | Kind | Model | Location | Network id | Role | Notes |
|------|------|-------|----------|------------|------|-------|
| pixel-personal | phone | Pixel 8 | with user | aa:bb:cc:dd:ee:ff | paired client | notifications only |
```

- **Identity is the network id (MAC) when known, otherwise `Name`.** Read before adding; if the identity exists, update in place.
- A device that also runs services belongs in `servers.md` instead — one machine, one inventory, and the host row wins.
- Retirement: delete the row and note the date in `memory.md`.
- **Scale cut**: one row per device while there are ≤15. Past that, one file per device at `~/Clawic/data/devices/<name>.md` with the same fields, and `devices.md` becomes the index (`Name | Kind | Role | → file`). If the folder already looks like that, follow it — never start a parallel `devices.md`.
- Foreign columns win, exactly as above. Never write a credential here; pairing secrets are pointers.

## Shared subscriptions

Lives at `~/Clawic/data/finances/subscriptions.md`, shared with every money and billing skill.

```markdown
# Subscriptions

| Service | What for | Amount | Cycle | Renews | Owner | Reference |
|---------|----------|--------|-------|--------|-------|-----------|
| model provider | agent API usage | 40 USD | monthly | 2026-08-03 | us | env:MODEL_API_KEY |
```

- **Identity is the service name.** Read the file first; if the service is already there, update the amount and renewal in place rather than adding a second row.
- **Amount always carries its currency in the value** (`40 USD`), and a usage-based service records the last observed month with its `As of` date rather than a fixed price.
- Cancellation: delete the row and note the date in `memory.md`. This file is kept small precisely because cancellations remove rows; it is never split.
- Do not duplicate an account owner here — a person goes in the shared `~/Clawic/data/contacts/contacts.md` (`Name | Key | Role | Preferred channel | Context | Last contact | File`, key = lowercase email) and is referenced here by name only.
- Foreign columns win. Never a card number, never a credential — the `Reference` column holds a pointer.

## Shared contacts

Lives at `~/Clawic/data/contacts/contacts.md`, shared with every skill that deals with people. Written here only when a person owns a credential, a job, an account, or a subscription this audit touched — the entity goes there, and this skill's rows carry their name as a pointer.

```markdown
# Contacts

| Name | Key | Role | Preferred channel | Context | Last contact | File |
|------|-----|------|-------------------|---------|--------------|------|
| Dana Ruiz | dana@example.com | ops lead | email | owns the sync service credential | 2026-07-26 | — |
```

- **Identity is `Key`**: lowercase email, else a handle, else `<kebab-name>` plus a stable disambiguator. It is a column of the row, never implicit. Read before adding; if the key exists, update that row in place.
- `Preferred channel` is the *type* of channel, not the address, and never a credential.
- **Retirement is part of the inventory.** When the person stops owning the credential, job, account, or subscription that put them here, clear the context this skill wrote; if nothing another skill wrote is left in the row, delete the row — and their `<name>.md` if the folder is split per person — and note the date in `memory.md`. A shared box is not yours alone: never delete a row that another skill is still using.
- **Scale cut**: one row per person while there are ≤15, or until one no longer fits its row. Past that, a `~/Clawic/data/contacts/<name>.md` per person and `contacts.md` becomes the index with the `File` pointer. Follow whatever the folder already does.
- Foreign columns win: match the existing header, add anything missing as a trailing note, never rewrite it.
- Never duplicate a person into `memory.md`, `credentials.md`, or the subscriptions box — name only.

## Split-out files

Created only by the split procedure above, never on day one. Each keeps the exact headings it had inside `memory.md`.

- `findings.md` — `## Open Findings`, same columns. Split first in practice: findings are the section that grows.
- `suppressions.md` — `## Accepted`, same five fields. Its review dates still get checked every run from here.
- `credentials.md` — `## Credential Inventory`, same columns, pointers only.
- `baseline.md` — `## System Baseline`, with one `## <path or machine>` subsection per workspace once there is more than one.
- `spend-log.md` — `## Spend` plus the anomaly baseline line. The savings rows are the reason this file exists: without them the same trim is rediscovered every quarter and nobody can say what the last one was worth.
