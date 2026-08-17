# Working File Templates — JSON

Read this file only when WRITING. `config.yaml` is what the user **declared**; `memory.md` and everything it indexes is what you **observed** or produced. An observation never overwrites a declaration.

## Where each thing goes

| Data | Home | How it grows |
|---|---|---|
| Declared preferences — table keys and preference areas alike | `~/Clawic/data/json/config.yaml` | Key by key, read-modify-write |
| Conventions this codebase settled on, producers and their quirks, saved expressions, due dates, box index | `~/Clawic/data/json/memory.md` | Rewritten in place; stays small |
| A schema that validates real payloads | `~/Clawic/data/json/schemas/<name>.schema.json` | Its own file from the first one; one file per document type |
| Field-by-field contract of a payload you reverse-engineered | `~/Clawic/data/json/contracts/<producer>.md` | Its own file from the first one; read whole when that producer comes up |
| A redacted sample payload worth keeping | `~/Clawic/data/json/fixtures/<name>.json` | Its own file; overwritten when the producer changes shape |
| Things you produced that get re-read — transformation mappings, migration runbooks, format decisions and why the alternative lost | `~/Clawic/data/json/artifacts/<kebab-name>.md` | Born as its own file, from the first one |
| Format or contract decisions for work tracked as a project | `~/Clawic/data/projects/<project>.md` (**shared**) | One file per project, one entry per decision |
| The person or company behind a producer | `~/Clawic/data/contacts/contacts.md` (**shared**) | One row per person; referenced here by name only |
| **Anything durable this table does not name** | `~/Clawic/data/json/<plural-noun>.md`, or `artifacts/<kebab-name>.md` if it is a long text read whole | Name the file after what it holds, never after when it was made; add its `## Boxes` line in the same turn |
| Credentials of any kind, and real personal data inside a sample | Nowhere under `~/Clawic/data/` | Pointer or redaction placeholder — see Secrets |

## When to write

No permission needed; every write is announced in one line that names the file. Writes and deletions stay inside the paths declared in this skill's `configPaths`. A deletion is named in that same line, and in a shared box only rows this skill itself wrote are ever updated or removed.

| It happened | Write |
|---|---|
| A schema was written or fixed and now validates real payloads | `schemas/<name>.schema.json`, plus its `## Boxes` line |
| A payload's fields, nullability or quirks were worked out by reading real data | `contracts/<producer>.md` |
| A producer surprised you: a quirk, a violated assumption, a measured size or record count | Its row in `## Producers` |
| An expression took more than one attempt to get right | Its row in `## Queries` |
| The codebase settled a convention: casing, dates, nulls, envelope, error shape, limits | `## Conventions` — unless the **user** declared it, which is `config.yaml` |
| A sample payload is worth keeping for tests or reference | `fixtures/<name>.json`, redacted |
| A transformation mapping, a migration runbook, or a format decision came out of the session | `artifacts/`, and the decision line in `~/Clawic/data/projects/<project>.md` when it belongs to tracked work |
| A parse, precision, or encoding failure cost real time to diagnose | `## Pain Points`, one line with the cause |
| The user declared a preference | Its key in `config.yaml` |
| Recurring work was scheduled or run | `## Due` |

## Start flat, split only when it hurts

Everything except schemas, contracts, fixtures, artifacts and the shared boxes begins inside `memory.md`. Splitting is a procedure, not a suggestion:

1. Before appending to a section, count its entries.
2. If the append would take it past **~15 entries or ~40 lines of real content** — scaffolding, headings and comments do not count — then, in the same turn: create the new file in `~/Clawic/data/json/`, move the whole section into it, **delete the section from `memory.md`**, add its line to `## Boxes`, and append the new entry to the new file.
3. Keep the headings identical on both sides of the move, so the split is a copy-paste and never a rewrite. `## Conventions` → `conventions.md`, `## Producers` → `producers.md`, `## Queries` → `queries.md`.
4. Never leave a copy behind. If the same data ever appears in both places, the extracted file wins and the `memory.md` copy is deleted.

Schemas, contracts, fixtures and artifacts are the exception: each is born as its own file whatever its size, because each is read whole and only when its subject comes up.

## Secrets

Nothing under `~/Clawic/data/` ever holds a secret value — not the files named here, not files you create, not a payload, curl command, or `.env` the user pastes in and asks you to keep. Store the pointer in its place, in this shape: `<kind>:<locator>`.

`env:API_TOKEN` · `keychain:stripe-live` · `1password:Work/Vendor/webhook` · `bitwarden:Shared/Partner API` · `vault:kv/prod/webhook` · `ssm:/prod/webhook/secret` · `profile:prod` · `file:~/.config/app/creds.json`

When the user pastes something to save, replace each secret value before writing and leave the pointer visible: `"api_key": "<env:VENDOR_API_KEY>"`. Say in one line that you did it.

In this domain — **not secrets, keep them**: field names and key paths, types and enum values, schema documents, `$id` and `$ref` URIs, endpoint paths and HTTP status codes, request ids and trace ids, ETag values, record counts and byte sizes, object ids that are not bearer tokens, last four digits, timezone and locale codes.

**Secrets, strip them**: bearer, access and refresh tokens, `Authorization` header values, API keys and `client_secret`, webhook signing secrets, session cookies, passwords and private keys, connection strings carrying a password, pre-signed URLs (the signature is the credential), and any JWT — its payload is readable and its signature is a credential.

**Personal data is not a secret but never goes in verbatim.** In fixtures and contracts, replace real values with stable placeholders that keep the shape: `"email": "user-1@example.com"`, `"phone": "+10000000001"`, `"national_id": "REDACTED-9"`. Stable means the same input maps to the same placeholder every time, so diffs stay meaningful.

**Contents:** [config.yaml](#configyaml) · [memory.md](#memorymd) · [schemas/](#schemas) · [contracts/](#contracts) · [fixtures/](#fixtures) · [artifacts/](#artifacts) · [shared projects box](#shared-projects-box) · [shared contacts box](#shared-contacts-box) · [split-out files](#split-out-files)

## config.yaml

Keys come from the Configuration table in `SKILL.md`, plus free-form keys nested under a preference area. Write a key only when the user states the preference.

**Writing is read-modify-write**: load the existing file, set or replace only the key just declared, keep every other key byte for byte. Never emit a `config.yaml` from this template — the template shows shape, not content. Create `~/Clawic/data/json/` if it does not exist.

```yaml
key_case: snake_case
null_policy: omit
id_as_string: true
date_format: rfc3339-offset
error_shape: problem-json
schema_draft: 2020-12
validator: ajv
query_tool: jq
indent: 0
max_payload_mb: 5
untrusted_default: true

# Preference areas — free-form keys added as the user reveals them.
# A preference the user states is a declaration and belongs here, never in memory.md.
conventions:
  envelope: data-meta
  pagination: cursor
  unknown_fields: tolerant-inbound-strict-config
platform:
  producer_lang: python
  consumer_lang: typescript
  store: postgres-jsonb
restrictions:
  no_floats_for_money: true
  no_comments_in_shipped_config: true
```

If you find a preference recorded in `memory.md`, move it here and note the move.

## memory.md

Write only the sections you have content for — a heading with nothing under it is noise, and it inflates the line count that decides a split. Never copy these hints into the user's file. `## Boxes` is the one section that is never dropped when `memory.md` is rewritten: deleting a line there orphans a file forever. This is what a populated file looks like:

```markdown
# JSON Memory

## Status
status: ongoing
last: 2026-07-26

## Boxes
- Order payload schema → `schemas/order.schema.json`; read before validating or changing an order body
- Vendor payout contract → `contracts/acme-payouts.md`; read whenever an Acme payload is involved
- Redacted webhook sample → `fixtures/acme-payout-webhook.json`; read when reproducing a payout bug
- NDJSON-over-array decision → `artifacts/export-format-decision.md`; read before changing the export endpoint
- Producers (19) → `producers.md`; read before trusting any feed's shape

## Due
| What | Every | Last run | Next due |
|------|-------|----------|----------|
| Re-validate stored schemas against live payloads | quarter | 2026-04-14 | 2026-07-14 |
| Refresh fixtures from production shapes | quarter | 2026-05-02 | 2026-08-02 |
| Check deprecated fields for zero traffic | month | 2026-07-01 | 2026-08-01 |

## Conventions
| Area | Settled on | Where it applies | Since |
|------|-----------|------------------|-------|
| Casing | snake_case on the wire, camelCase in TS models, mapped at the boundary | all public endpoints | 2026-03 |
| Ids | strings everywhere; ints only in internal DB rows | all | 2026-03 |
| Absent vs null | absent = untouched, null = clear, PATCH only | /v2/* | 2026-05 |
| Errors | RFC 9457 problem+json, `type` is a stable URI | all | 2026-05 |
| Limits | 5 MB body, depth 32, duplicate keys rejected | public ingress | 2026-06 |

## Producers
| Producer / feed | Shape | Typical size | Quirk | Contract |
|---|---|---|---|---|
| acme payouts webhook | single object | 4 KB | amounts are strings; `metadata` may be `[]` instead of `{}` | `contracts/acme-payouts.md` |
| internal events export | NDJSON | 2.1 GB / 6.4M lines, parses at ~4× RSS | last line has no newline | — |
| legacy CRM sync | array | 180 MB | duplicate `id` keys inside records; first occurrence is the real one | — |

## Queries
| Need | Expression | Tool | Against |
|------|-----------|------|---------|
| Failed payouts with reason | `.data[] \| select(.status=="failed") \| {id, reason: .failure.reason}` | jq | acme payouts |
| Flatten export to CSV columns | `[.id, .user.email, (.items \| length)] \| @csv` | jq | internal events export |
| Instance ids from a describe call | `Reservations[].Instances[].InstanceId` | jmespath | AWS CLI output |

## Pain Points
2026-06: three days lost to ids silently truncating in the browser — the API sends int64. All ids string since.

---
*Updated: 2026-07-26*
```

Rules that keep this readable next month:

- **`## Boxes`**: one line per file that exists — `<what> (<volume>) → <file>; read when <condition>`. Written in the same turn the file is created. Never delete a line without deleting the file it points to. A box with no index line does not exist.
- **`## Due`**: check it against today's date at the start of a session and state any overdue item in one line — a statement, not a question. Every recurring thing this skill schedules belongs here.
- **`## Conventions`**: what the codebase settled on, with the date, because "why is this snake_case" gets asked once a quarter. A convention the **user** declares is a preference and goes to `config.yaml` instead; this section is for what the code already does. When they conflict, say so once and let the user decide — never silently overwrite either.
- **`## Producers`**: one row per feed or endpoint whose payload you have actually seen. Sizes carry their unit (`2.1 GB`, `6.4M lines`) and parse cost is recorded as a ratio to file size, because that ratio is what decides streaming (SKILL.md Rule 6). `Contract` points at `contracts/<producer>.md` when one exists, `—` when it does not.
- **`## Queries`**: an expression only earns a row if it took more than one attempt or encodes a quirk. Record the tool, because the same path expression is invalid in the other three (`querying.md`).
- These headings are exactly the ones the split-out files get, so a split stays a copy-paste.

| Status | Meaning |
|-------|---------|
| `ongoing` | Still learning their payloads and conventions |
| `complete` | Know their formats, producers and rules well |

## schemas/

One file per document type, at `~/Clawic/data/json/schemas/<name>.schema.json`, saved the first time it validates real payloads — deriving a schema from samples costs hours and nobody should pay it twice.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.invalid/schemas/order.schema.json",
  "title": "Order — as returned by /v2/orders/{id}",
  "description": "Derived 2026-07-26 from 400 production payloads. Read before changing an order body.",
  "type": "object",
  "required": ["id", "status", "amount_cents", "currency", "created_at"],
  "properties": {
    "id": { "type": "string", "description": "int64 upstream; string on the wire" },
    "status": { "enum": ["pending", "paid", "failed", "refunded"] },
    "amount_cents": { "type": "integer", "minimum": 0 },
    "currency": { "type": "string", "pattern": "^[A-Z]{3}$" },
    "created_at": { "type": "string", "format": "date-time" },
    "note": { "type": ["string", "null"] }
  },
  "unevaluatedProperties": false
}
```

- `$id` uses a domain the user controls or `example.invalid`; it is an identifier, not a URL anyone fetches.
- The `description` records **when** and **from how many samples** it was derived. A schema with no provenance gets distrusted and rewritten.
- If the schema came from the producer, say so and never edit it — write your additions in the contract file instead.
- Enum values are data, not secrets. Keep them.

## contracts/

One file per producer, at `~/Clawic/data/json/contracts/<producer>.md`. This is what a schema cannot hold: meaning, lies, and history.

```markdown
# Contract — Acme payouts webhook
*Read when: any Acme payload is involved. Observed from live traffic, last confirmed 2026-07-26.*

Endpoint: POST /webhooks/acme  ·  Auth: signature header, secret at `env:ACME_WEBHOOK_SECRET`
Schema: `schemas/acme-payout.schema.json`  ·  Sample: `fixtures/acme-payout-webhook.json`

| Field | Type on the wire | Means | Watch out |
|---|---|---|---|
| `amount` | string decimal | minor units? No — major units, 2 dp | never parse as float |
| `metadata` | object, or `[]` | user tags | PHP producer emits `[]` for empty |
| `occurred_at` | RFC 3339, no offset | producer's local time | Europe/Madrid, not UTC |

Undocumented behavior: retries reuse the same `event_id`; treat it as the idempotency key.
Owner: Acme integrations team (see `contacts/`).
```

## fixtures/

Redacted samples at `~/Clawic/data/json/fixtures/<name>.json`, named after the payload, never after the date. One per shape, overwritten when the producer changes shape — a fixtures folder with six dated copies of the same payload is where nobody looks.

Redact before writing, using the placeholder rules in Secrets. A fixture that still contains a live token or a real customer's email is a leak waiting for a backup.

## artifacts/

One file per thing, at `~/Clawic/data/json/artifacts/<kebab-name>.md`, created the first time it exists. Canonical types here: **transformation mapping**, **migration runbook**, **format decision**. Every artifact opens with when to read it, and gets its `## Boxes` line in the same turn.

```markdown
# Format decision — NDJSON for the events export
*Read before changing the export endpoint or its consumer. 2026-07-26.*

Decision: NDJSON, one event per line, gzip on the wire.
Rejected: a single JSON array — 2.1 GB parsed at ~4× RSS on an 8 GB worker (SKILL.md Rule 6).
Rejected: MessagePack — gzipped JSON was within 8% of gzipped msgpack on a 50k-record sample.
Consequences: consumers must tolerate a final line without a newline; no trailing `]` to signal completeness, so the export writes a `.done` marker.
```

```markdown
# Transformation mapping — legacy CRM → v2 contacts
*Read before touching the sync job. 2026-07-26.*

| Source path | Target path | Rule |
|---|---|---|
| `Cust.ID` | `id` | int64 → string |
| `Cust.Nm` | `full_name` | trim; empty → omit (null_policy) |
| `Cust.Dt` | `created_at` | `MM/DD/YY` local → RFC 3339 UTC |
```

If the user tracks this work as a project, the decision line also belongs in the shared `~/Clawic/data/projects/<project>.md`, with the full reasoning staying here and referenced by file name.

## Shared projects box

Lives at `~/Clawic/data/projects/<project>.md` and is shared with every other skill — the user may not have any of them installed, so the protocol travels with this skill.

```markdown
# Project — checkout-v2

status: active
objective: replace the v1 checkout API without breaking the mobile client

## Decisions
| Date | Decision | Why | Detail |
|------|----------|-----|--------|
| 2026-07-26 | All ids are strings on the wire | int64 truncates in the browser above 2^53−1 | `json/artifacts/id-typing.md` |
| 2026-07-26 | NDJSON for the events export | 2.1 GB array did not fit in the worker | `json/artifacts/export-format-decision.md` |
```

- **Identity is the project name**, which is the file name in kebab-case. Read the folder before creating a file: if a project file already exists, append to it — a second file for the same project is how two skills end up disagreeing about status.
- **Update in place.** A decision that changes gets its row rewritten with the new date and a note of what it replaced, never a second contradicting row.
- **Foreign structure wins.** If the file already exists with different headings, add your rows under the closest existing heading and never rewrite its structure or its front matter. Only add a `## Decisions` heading if none is there.
- **Closing is a status, not a deletion**: `status: done | cancelled — <date>` inside the file. The record of what was delivered is the point.
- **Scale cut**: one file per project directly in `~/Clawic/data/projects/`, however many are open. Past ~20 closed ones (`status: done` or `cancelled`), move those to `~/Clawic/data/projects/archive/<project>.md` without renaming them, so the folder shows live work and the links keep resolving. If the folder already has an `archive/`, follow it.
- Keep the reasoning in `artifacts/` and reference it by file name here. Duplicating the full rationale in both places guarantees they drift.

## Shared contacts box

Only when a producer belongs to a person or company the user deals with. Lives at `~/Clawic/data/contacts/contacts.md`, shared with every other skill.

```markdown
# Contacts

| Name | Key | Role | Preferred channel | Context | Last contact | File |
|------|-----|------|-------------------|---------|--------------|------|
| Dana Ruiz | dana@acme.example | Acme integrations lead | email | owns the payouts webhook contract | 2026-07-20 | — |
```

- **Identity is `Key`**: lowercase email, else the handle, else `<kebab-name>` plus a stable disambiguator. It is a column of the row, never implicit.
- **Read before adding.** If the key is already there, update the row in place; only its absence justifies a new row. Never touch a row this skill did not write.
- **Foreign columns win.** If the file already has a different column set, match it and add anything missing as a trailing note. Never rewrite its header.
- **Scale cut**: one row per person while there are ≤15. Past that, one file per person at `~/Clawic/data/contacts/<name>.md` and `contacts.md` becomes the index with the `File` pointer. If the folder already looks like that, follow it.
- **Retirement is part of the inventory.** When a contact stops existing for the user — the producer's owner left, the vendor relationship ended — delete their row (and their `<name>.md` if it was split out) and note the deletion with its date in `memory.md`, on the `## Producers` row of the feed they owned. Only rows this skill wrote. An inventory that only grows stops being an inventory.
- Contact details are data, not secrets — but never store their credentials, and never copy a real address into a fixture (Secrets).

## Split-out files

Created only by the split procedure above, never on day one. Each keeps the exact headings it had inside `memory.md`.

`conventions.md` — `## Conventions`. Grows when the user works across several codebases with different rules; add a `Codebase` column at the split, not before.

`producers.md` — `## Producers`. The reason this file exists is that a feed's quirks are rediscovered every time someone new touches it; each row saves a debugging session.

`queries.md` — `## Queries`. Group by `Against` once past ~30 rows, keeping one table per producer under an `### <producer>` heading.
