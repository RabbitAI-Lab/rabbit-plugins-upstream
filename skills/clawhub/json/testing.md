# Testing — Fixtures, Golden Files, and Contracts

Two failure modes to design against: a test suite that passes while the payload is wrong (mocks that lie), and a suite that fails on every unrelated change (snapshots full of noise).

**Before writing a fixture for a producer you have already worked with**, check `~/Clawic/data/json/fixtures/` and the `## Boxes` index — a redacted sample probably exists.

**Contents:** [Fixtures From Real Payloads](#fixtures-from-real-payloads) · [Redaction](#redaction) · [Golden Files Without Noise](#golden-files-without-noise) · [Comparing Documents in Assertions](#comparing-documents-in-assertions) · [Schema Tests](#schema-tests) · [Contract Testing](#contract-testing) · [Property and Fuzz Testing](#property-and-fuzz-testing) · [Generated Test Data](#generated-test-data) · [Keeping Fixtures Honest](#keeping-fixtures-honest)

## Fixtures From Real Payloads

- A hand-written fixture encodes what you *believe* the producer sends. Only a captured payload encodes what it sends. Capture from production or staging traffic, redact, and commit.
- Keep one fixture per **shape**, not per test: the happy path, each documented variant, and every payload that ever caused an incident. That last category is the most valuable set of files in the repository.
- Name by content, never by date: `order-refunded.json`, not `payload-2026-07-26.json`. A folder of dated copies of the same shape is where nobody looks (`memory-template.md`).
- Trim, but do not invent: dropping 900 of 1000 array elements is fine, changing a field's type to make a test pass is how a fixture starts lying.
- Store the provenance in a sibling contract file — which endpoint, which date, which version (`api-payloads.md`).

## Redaction

Before any payload is committed or written under `~/Clawic/data/`:

- Replace secrets with the pointer form (`<env:VENDOR_TOKEN>`), never with a plausible fake — a plausible fake gets tried against production by someone eventually (`security.md`).
- Replace personal data with **stable** placeholders that preserve shape and length class: `user-1@example.com`, `+10000000001`, `REDACTED-9`. Stable means the same input maps to the same placeholder every time, so diffs remain meaningful and referential integrity across records survives.
- Keep everything that is not sensitive: field names, types, enum values, ids that are not credentials, sizes, timestamps' format. A fixture stripped of its structure is worthless.
- Automate it: a redaction pass in the capture script, plus a CI check that fails when a fixture matches secret patterns (token-like strings, private-key headers, long base64 blobs). Manual redaction fails exactly once and that once is enough.

## Golden Files Without Noise

A golden file that changes on every run gets regenerated unread, which is the same as not having one.

1. **Canonicalize before writing**: sorted keys, consistent number formatting, no insignificant whitespace (`signing.md`). Then a real change is the only thing that appears in the diff.
2. **Pretty-print with one value per line** for the stored form, so line-based review and merge work (`patching.md`).
3. **Neutralize volatile fields** before comparison — timestamps, generated ids, durations, hostnames, request ids. Two approaches, both fine: substitute placeholders during normalization, or use matchers that assert type and shape rather than value.
4. **Review regeneration deliberately.** An update flag that rewrites every golden file is necessary and dangerous: require the diff to be read in review, and never regenerate as a reflex when a test fails.
5. Keep golden files small enough to read. A 3,000-line golden file is a checksum with extra bytes; assert on the parts that matter.

## Comparing Documents in Assertions

- Compare **parsed structures**, never strings. String comparison fails on key order, whitespace and escaping — all of which are meaningless (`patching.md`).
- Object key order is irrelevant; array order is data. A test helper that sorts arrays to make comparison easy is hiding real bugs.
- Numbers compare by value: `1` and `1.0` are equal in JSON semantics but may be different types in your language. Normalize before comparing, or assert on the field with an explicit numeric comparison.
- Floats compare with a tolerance, never with equality (`numbers.md`).
- Absent and null must be distinguished by the assertion, or the test passes for both and the bug ships (Rule 3).
- Prefer targeted assertions on the fields under test plus one schema validation of the whole document, over a full-document equality check. Full equality couples every test to every field.

## Schema Tests

- Validate every recorded fixture against the current schema in CI. It is the cheapest possible regression test for a contract, and it catches the producer's silent change on the day you upgrade the fixture.
- Test the **schema itself** with negative cases — a schema with only positive tests passes when it is inert (`schema.md`).
- **Backward-compatibility gate**: every fixture from previous versions must still validate against the new schema. A change that breaks an old fixture is a breaking change, and the build should say so before a consumer does (`evolution.md`).
- Validate responses against the schema inside integration tests, not only the request bodies. Response drift is what breaks clients.

## Contract Testing

- Consumer-driven contract testing (the Pact family) means: each consumer records what it needs, and the provider's build verifies it can still satisfy every recorded expectation. It catches exactly the failure that schema validation misses — the provider removing a field only one consumer used.
- Worth the setup when there are multiple internal consumers of a service you also own. Not worth it for a public API with unknown consumers, where a published schema plus a deprecation policy is the mechanism (`evolution.md`).
- The lighter version that captures most of the value: each consumer commits a fixture of the response shape it depends on, and the provider's CI validates its real responses against those fixtures' schemas.
- Contracts test shape and semantics, not behavior. They do not replace integration tests; they make the payload part of the interface reviewable.

## Property and Fuzz Testing

- Round-trip property: for generated documents, `parse(serialize(x))` must equal `x` under your own equality. It finds the whole Round-Trip Losses table in SKILL.md, in your specific stack, automatically.
- Idempotency property: applying a merge patch twice equals applying it once (`patching.md`).
- Invariant properties: validated documents always satisfy the business invariants; a rejected document never mutates state.
- Fuzz the ingress boundary with a corpus that includes: truncated documents, unbalanced brackets, deep nesting, huge arrays, duplicate keys, lone surrogates, BOMs, `NaN`, enormous integer literals, `__proto__` keys, and empty bodies. Every item on that list is a bug someone shipped (`security.md`, `encoding.md`).
- Assert the *response*, not just the absence of a crash: a hostile document should produce a 400 with a generic message, not a 500 with a stack trace.

## Generated Test Data

- Schema-driven generators (json-schema-faker and equivalents) produce documents that satisfy the schema and nothing else — the values are nonsense, and they will not include the awkward real-world case that breaks you.
- Use generated data for load testing, index sizing and rough performance work. Use captured data for correctness.
- If a generator is the only source of test data, at minimum seed it deterministically so a failure is reproducible, and pin the seed in the failure output.
- Generated data drifts from reality as the schema loosens; a fixture captured from production does not.

## Keeping Fixtures Honest

A fixture is a snapshot of someone else's behavior, and it decays silently:

- Schedule a **fixture refresh** — capture current payloads, diff against the stored fixtures, and treat a structural difference as a signal even when the tests still pass. Put the cadence in the `## Due` table of `memory.md` (`memory-template.md`).
- Diff structurally, not textually: added and removed paths, changed types (`patching.md`). A new optional field is information; a changed type is an incident in waiting.
- When a producer's shape changes, update the fixture **and** the contract file in the same turn, with the date — otherwise the contract describes a payload that no longer exists.
- Delete fixtures for shapes that no longer occur. A folder of stale fixtures makes every future diff ambiguous.

**When a payload worth keeping is captured**, write it redacted to `~/Clawic/data/json/fixtures/<name>.json` and add its `## Boxes` line with the condition under which it should be read (`memory-template.md`).
