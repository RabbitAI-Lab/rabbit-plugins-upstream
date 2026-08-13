# Evolution — Changing a Payload Without Breaking Consumers

A payload is a contract with an unknown number of readers, some of which are mobile apps that will never be updated. Rule 7 in one line: **add, never repurpose**.

**Contents:** [Breaking or Not](#breaking-or-not) · [The Tolerant Reader](#the-tolerant-reader) · [Renaming a Field](#renaming-a-field) · [Changing a Type](#changing-a-type) · [Removing a Field](#removing-a-field) · [Enums and Status Values](#enums-and-status-values) · [Versioning Strategies](#versioning-strategies) · [Deprecation That Actually Ends](#deprecation-that-actually-ends) · [Consumer-Side Defenses](#consumer-side-defenses)

## Breaking or Not

Classification is the whole discipline. "Breaking" means: a consumer that worked yesterday fails today, or worse, silently reads wrong data.

| Change | Verdict | Why |
|---|---|---|
| Add an optional field | Safe | Unless a consumer uses strict deserialization (Jackson's default) — which is why you publish the tolerance requirement in the contract |
| Add a required field to a **response** | Safe | Consumers ignore what they do not read |
| Add a required field to a **request** | Breaking | Every existing caller now fails validation |
| Add a value to an enum | Breaking in practice | Any consumer with a closed switch or a strict deserializer fails on it |
| Make a required response field optional | Breaking | Consumers modeled it as non-null |
| Make an optional request field required | Breaking | Same as adding one |
| Change a type (`12` → `"12"`) | Breaking | Typed consumers fail at parse; dynamic ones fail at comparison, later and worse |
| Widen a number's range past 2^53−1 | Breaking, invisibly | Nothing errors; values silently change (`numbers.md`) |
| Rename a field | Breaking | It is a removal plus an addition |
| Change the meaning of a field, same name and type | The worst kind | Nothing fails; every consumer is now wrong. This is the change that gets found by a customer |
| Change a `null` to an omission (or back) | Breaking | Only for consumers that distinguish them — which is the ones that care most (Rule 3) |
| Reorder object keys | Safe | Objects are unordered by spec — except for signatures and byte-exact caches (`signing.md`) |
| Reorder array elements | Breaking | Arrays are ordered by spec, and someone is indexing element 0 |
| Tighten a validation rule (shorter `maxLength`) | Breaking for writers | Payloads that were accepted yesterday are rejected today |
| Loosen a validation rule | Safe for writers, breaking for readers | A consumer's own schema now rejects what you send |
| Change an error `code` or problem `type` URI | Breaking | Clients branch on it (`api-payloads.md`) |

## The Tolerant Reader

The mechanism that makes additive evolution work, and it only works if consumers do their half:

- **Ignore unknown fields.** Publish this as a requirement of your contract, in the documentation and in the schema (`unevaluatedProperties` absent rather than `false` for third-party consumers).
- **Do not validate what you do not use.** A consumer that validates the entire payload against its own copy of the schema breaks on every additive change — the exact opposite of the intent.
- **Accept unknown enum values** with a defined fallback.
- **Do not depend on key order, whitespace, or the absence of a field.**
- Be strict about what you send, tolerant in what you accept — and be strict about what you accept on **your own** write endpoints, where an unknown field is a typo (`languages.md`).

## Renaming a Field

Never in place. The expand-contract sequence:

1. **Expand**: emit both `old_name` and `new_name` with identical values. Accept both on input, with a documented precedence (new wins).
2. **Announce**: mark `old_name` deprecated in the schema `description`, in the docs, and in the changelog, with a date.
3. **Measure**: instrument reads of `old_name` per consumer. "Nobody uses it" without a metric is a guess.
4. **Contract**: remove `old_name` only after traffic to it is zero for a full business cycle — a month at minimum, a quarter if there are mobile clients, never if there are embedded devices.

Cost of skipping step 3: the removal happens, the incident happens, the field comes back, and now the API has both names forever anyway.

## Changing a Type

Same expand-contract, with a new field name — a type change under the same name is unfixable for a consumer that cannot branch on type:

- `12` → `"12"`: emit `amount_cents` (int) and `amount` (decimal string) simultaneously; retire the old one on the schedule above (`numbers.md`).
- Scalar → object (`"address": "…"` → `"address": {…}`): new field, `address_detail`. A consumer that string-concatenates the old field would produce `[object Object]` in the UI.
- Object → array (one relation becomes many): new plural field. Never make a field "sometimes an object, sometimes an array" — it is legal JSON and it doubles the branch count of every consumer forever.
- Widening an id past 2^53−1: this is the one type change that is urgent, silent, and dated — it lands when the sequence grows a digit. Ship the string form long before that (Rule 2).

## Removing a Field

- Removal is breaking, always. The sequence is the same: deprecate, measure, remove.
- Emitting `null` instead of removing is not a soft landing: a consumer that renders the value now renders "null" or crashes on a non-null type.
- If the field must go for legal or privacy reasons (it is personal data that should never have been there), that overrides the schedule: remove it, publish the reason, and treat the resulting client failures as the cheaper outcome.
- Removing a field from a **request** is safe — accept and ignore it for a deprecation window, and never start rejecting the old field in the same release you stop reading it.

## Enums and Status Values

Adding a status is the most common accidental break in a mature API:

- Publish, from day one, that consumers must handle unknown values, and give them the fallback in the documentation and in the client SDKs.
- Group new statuses under an existing coarse field when possible: keep `status` at four stable values and put the detail in `status_reason`. Coarse fields that never change plus fine fields that grow is the shape that survives.
- Never reuse a retired enum value for a new meaning. It is the "change the meaning, keep the name" failure with extra steps.
- If a client genuinely cannot tolerate unknown values (a device firmware), that constraint belongs in the contract, and it means enum changes are a versioned change for that client.

## Versioning Strategies

| Strategy | Shape | Trade-off |
|---|---|---|
| No version, additive-only | One URL forever | Cheapest and the default when you can hold the discipline; impossible if a breaking change is truly required |
| URL path | `/v2/orders` | Obvious, cacheable, easy to route; encourages big-bang v2s that then need their own migration |
| Media type | `Accept: application/vnd.acme.order.v2+json` | Precise, per-resource, invisible in logs and hard to test in a browser |
| Header | `X-API-Version: 2026-07-01` | Flexible; date-based versions make "which behaviors do I get" answerable |
| Field-level flags | `?include=new_shape` | Fine-grained, but combinatorial explosion of shapes to test |

- Whatever the strategy, **version the payload's semantics, not every wire change**. A version bump per additive field means five versions a quarter and nobody upgrades.
- Pin new consumers to the version that exists at their integration date and never move it silently. Date-based versions make this mechanical.
- Two versions live is manageable; three is a maintenance product. Every version needs its own schema, its own tests, and its own fixtures (`testing.md`).

## Deprecation That Actually Ends

- Announce in three places: the schema `description`, the changelog, and the response itself — the `Deprecation` and `Sunset` HTTP headers exist for exactly this and are machine-readable.
- Give a date, not "soon". A deprecation with no sunset date is a permanent field.
- Instrument per-consumer usage, not aggregate: "0.1% of traffic" can be one client that matters more than the change.
- Send a warning to identified consumers before the sunset, then apply brownouts — short deliberate outages of the deprecated behavior — before permanent removal. A brownout finds the consumers that ignored every email, at a time you chose.
- After removal, keep the field name reserved forever. Reusing it for something else is the meaning-change failure.

## Consumer-Side Defenses

When you are the one reading someone else's payload:

- Parse into your own model and ignore everything you do not need; never re-emit a payload you received unless you are forwarding raw bytes (Rule 5).
- Validate only the fields you depend on, with your own narrow schema (`schema.md`).
- Handle unknown enum values with a defined fallback and log the unknown value once per value, not per record.
- Snapshot the producer's payload as a redacted fixture and re-validate it on a cadence: a producer's silent change is found by a scheduled check, never by a code review (`testing.md`, `## Due`).
- Treat a field that disappears as an incident signal, not a null — a missing `total` is different from `total: 0`.

**When a contract change is decided** — a rename, a type migration, a version scheme, a sunset date — write it to `~/Clawic/data/json/artifacts/<kebab-name>.md` with the date, the rejected alternative and the sunset date, add its `## Boxes` line, and put the one-line decision in `~/Clawic/data/projects/<project>.md` when the work is tracked there (`memory-template.md`). Set the "check deprecated fields for zero traffic" cadence in `## Due` at the same time — a deprecation with no scheduled check never ends.
