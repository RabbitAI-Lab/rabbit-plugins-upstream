# API Payloads — The Shape of Request and Response Bodies

This is the document on the wire, not the endpoint design (`rest-api`, `api-design`) and not somebody else's API (`api`). Every default below is set by `config.yaml`; the rules are what makes a payload survive three clients and two years.

**Contents:** [Envelope](#envelope) · [Field Naming](#field-naming) · [Nulls, Absence, and Emptiness](#nulls-absence-and-emptiness) · [Errors](#errors) · [Collections and Pagination](#collections-and-pagination) · [Timestamps](#timestamps) · [Enums](#enums) · [Requests: Create, Update, Patch](#requests-create-update-patch) · [Things That Do Not Belong in a Payload](#things-that-do-not-belong-in-a-payload) · [Recording a Contract](#recording-a-contract)

## Envelope

| Style | Shape | Fits |
|---|---|---|
| Bare resource | `{"id": "…", "status": "paid"}` | Single resources, cache-friendly, nothing to unwrap |
| Data envelope | `{"data": {…}, "meta": {…}}` | Anything that ever needs pagination, warnings, or partial success |
| Problem details | `{"type": "…", "title": "…", "status": 422, …}` | Errors, always (Errors below) |

- Choose once and apply everywhere. A mixed API — bare here, enveloped there — costs every client a per-endpoint special case, which is worse than either choice (Where Experts Disagree in SKILL.md).
- **Never return a bare array at the top level of a collection endpoint.** There is nowhere to add pagination or a total later without a breaking change, and it removes any room for metadata. `{"data": [...], "meta": {...}}` costs eight bytes and buys the next five years.
- `meta` holds pagination, counts, and warnings. `data` holds only the resource. Mixing them means a client cannot tell a field of the resource from a field about the response.
- Envelope only the body. HTTP already carries status, caching, and content type; duplicating the status code inside the body creates two sources of truth that eventually disagree.

## Field Naming

- One casing across the whole API, set by `key_case`. `snake_case` reads well from SQL-shaped backends; `camelCase` matches JavaScript clients without mapping. Both are fine; a payload with `userId` next to `user_name` is not (it is also a reliable sign of two teams and no review).
- Collections are plural nouns (`items`, `users`), scalars singular. A field named `user` that holds an array costs a debugging session per consumer.
- Booleans read as assertions: `is_active`, `has_children`, `accepts_marketing`. Avoid negations — `is_not_disabled` inverts twice in the reader's head, and `disabled: false` is worse.
- Units and precision go in the name (`timeout_ms`, `weight_kg`, `amount_cents`) or in an adjacent field, never in the documentation only (`numbers.md`).
- Keys are stable identifiers, not display text. Never localize keys, never use spaces, never put an id in a key (`{"user_42": …}` is a map where an array of objects belongs — it is unqueryable by schema and unpageable).
- Reserved-ish names to avoid as top-level keys: `type` (collides with problem details), `data` and `meta` inside `data`, `errors` when it is not an error, `id` for something that is not the resource's identity.

## Nulls, Absence, and Emptiness

The three states again (Rule 3), applied to a real API:

| Situation | Emit |
|---|---|
| Optional field with no value, `null_policy: omit` | Omit the key |
| Field the client must know exists but has no value | `"note": null` — and say so in the schema |
| Empty collection | `[]` or `{}`, **never** `null`. A client that iterates without a null check is not wrong |
| A relationship that was not loaded | Omit it, or use an explicit sentinel like `{"items": {"loaded": false}}` — never an empty array, which means "there are none" |
| A field the caller is not allowed to see | Omit it. `null` says "empty", omission says "not applicable to you"; leaking the difference leaks the existence of data |

Consistency is the requirement: a field that is sometimes absent, sometimes null, and sometimes `""` for the same semantic state forces every consumer to write a three-way check.

## Errors

Default is `error_shape: problem-json` — RFC 9457 `application/problem+json`, which obsoleted RFC 7807 and is the closest thing to a standard error body:

```json
{
  "type": "https://example.invalid/probs/insufficient-funds",
  "title": "Insufficient funds",
  "status": 403,
  "detail": "Balance 12.50 USD is below the 30.00 USD charge.",
  "instance": "/accounts/12345/transfers/98765",
  "balance_cents": 1250,
  "required_cents": 3000
}
```

- `type` is a **stable URI** and the only machine-readable part. Clients switch on `type`, never on `title` or `detail`, which are human text and may be localized or reworded at any time.
- Extension members (`balance_cents` above) are allowed at the top level and are how a client gets structured context without parsing prose.
- Field-level validation errors need a list, and problem details accommodates it as an extension: `"errors": [{"pointer": "/items/3/qty", "code": "min", "message": "must be ≥ 1"}]`. Use a JSON Pointer for the location so it maps mechanically to the request body (`querying.md`).
- One error shape for the whole API, including 500s and gateway errors you generate. A client with two error parsers has one that is never tested.
- Never return 200 with an error body. Every retry, cache, and monitoring tool reads the status code, and none of them read your envelope.
- Error `code` values are an enum in the contract: adding one is additive, changing the meaning of one is breaking (`evolution.md`).

## Collections and Pagination

| Style | Shape | Use |
|---|---|---|
| Cursor | `{"data": [...], "meta": {"next_cursor": "eyJpZCI6…", "has_more": true}}` | Default. Stable under inserts and deletes, cheap on the database |
| Offset/limit | `{"data": [...], "meta": {"total": 4210, "offset": 40, "limit": 20}}` | Only when the client must jump to page N and the dataset is small and stable |
| Link header / `_links` | `{"_links": {"next": {"href": "…"}}}` | When clients should not construct URLs themselves |

- Cursors are **opaque strings**. The moment a client decodes one, its contents become the contract; document them as opaque and change them freely.
- `total` costs a second query on most databases and is frequently the slowest part of a list endpoint. Emit it only if a client displays it, and consider `has_more` instead.
- Always cap `limit` server-side and echo the effective value. An uncapped `limit` is a denial-of-service parameter (`security.md`).
- Sort order must be deterministic and total — a tiebreaker on a unique column — or pagination silently repeats and skips records.
- Sparse fieldsets (`?fields=id,name`) make responses smaller and schemas conditional; a client asking for fewer fields still gets a document that validates against the full schema only if those fields are optional.

## Timestamps

- Default `date_format: rfc3339-utc`: `"2026-07-26T14:30:00Z"`. Sortable as a string, unambiguous, parseable everywhere.
- Include the offset when the local time carries meaning: `"2026-07-26T16:30:00+02:00"`. An offset is not a timezone — for anything recurring or in the future, add the IANA zone in its own field (`"timezone": "Europe/Madrid"`), because offsets change with DST and legislation.
- Epoch numbers are compact and unreadable, and their unit is invisible: `1785000000` is seconds, `1785000000000` is milliseconds, and a client that guesses wrong lands in 1970 or 58,500 AD. If you use them, put the unit in the name.
- Dates without time are `"2026-07-26"` (RFC 3339 full-date), not a timestamp at midnight in an unstated zone — a birthday is not an instant.
- Durations: `timeout_ms` as an integer, or ISO 8601 (`"PT30S"`) when humans edit the value.
- Field naming: `created_at`, `updated_at`, `expires_at` — the `_at` suffix says instant. `*_date` says calendar date. Keep the distinction; it is the difference between a DST bug and no bug.

## Enums

- Enum values are lowercase, stable, and machine-facing: `"payment_failed"`, not `"Payment Failed"`. Display text is the client's, or a separate `label` field.
- **Consumers must tolerate unknown values.** A closed enum in a client turns a producer's additive change into a crash; document an `unknown`/default branch as part of the contract (`evolution.md`).
- Never encode structure in the value (`"status": "failed:card_declined"`). Two fields, always.
- Booleans that will grow a third state should have started as an enum. `"status": "active" | "paused"` extends; `"is_active": true` does not.

## Requests: Create, Update, Patch

| Verb | Body semantics | Trap |
|---|---|---|
| POST create | Full resource minus server-assigned fields | Accepting a client-supplied `id` without validating uniqueness and authority |
| PUT replace | The **whole** resource; absent fields are cleared | Clients that send a partial body to PUT silently wipe fields — this is the most common data-loss bug in JSON APIs |
| PATCH merge | Only the fields to change; `null` means clear (Rule 3) | Without a documented null policy, "clear this field" is unexpressible |
| PATCH with JSON Patch | An array of ops, applied atomically | Different media type (`application/json-patch+json`) and different semantics (`patching.md`) |

- Echo the resulting resource in the response to a create or update. It saves the client a GET and makes server-computed fields visible immediately.
- Idempotency for creates: accept a client-generated key (header or field), store it with the result, and return the same body on retry. A retried POST without one is a duplicate charge.
- Validate the whole body and return **all** field errors at once (`schema.md`); returning them one at a time turns a form into a conversation.
- Reject unknown fields on your own write endpoints (a typo'd field name that is silently ignored is a data-loss bug) while staying tolerant when *reading* other people's payloads (`languages.md`).

## Things That Do Not Belong in a Payload

- **A stringified JSON document inside a field.** `"payload": "{\"a\":1}"` doubles every escape, defeats schema validation of the inner content, and breaks every path expression. A nested object costs nothing. The only defensible exception is an opaque blob that must round-trip byte-exact for a signature (`signing.md`) — say so in the field name (`raw_body`).
- **Secrets.** Tokens, keys, and full card numbers do not travel in a response body that gets logged by three layers of infrastructure (`security.md`).
- **HTML or Markdown in a field whose name does not say so.** `description_html` vs `description` is the difference between rendering and an XSS incident.
- **Base64 blobs above a few kilobytes.** +33% size and full memory materialization on both ends; use a URL and a separate transfer (`performance.md`).
- **Server-side pagination state, internal ids, or SQL fragments.** Anything exposed becomes a contract someone depends on.
- **Locale-formatted numbers or dates.** Formatting is presentation; the payload carries values (`numbers.md`).

## Recording a Contract

**When a payload's real shape is worked out** — the field meanings, the lies in the documentation, the quirks — write `~/Clawic/data/json/contracts/<producer>.md` with the field table and add its `## Boxes` line in the same turn (`memory-template.md`). When the shape is your own and the work is tracked as a project, the decision line also goes to `~/Clawic/data/projects/<project>.md`. Contracts are the highest-value thing this domain produces: they are what nobody writes down and everybody re-derives.
