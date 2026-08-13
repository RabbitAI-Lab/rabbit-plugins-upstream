# JSON Schema — Authoring, Drafts, and Validation That Catches Things

A schema earns its place by rejecting documents that would otherwise fail deeper in the system. A schema that accepts everything is worse than none, because it is trusted.

**Before writing one for a payload you have seen**, read `~/Clawic/data/json/schemas/` and the `## Boxes` index in `memory.md`: a schema derived from real samples already exists more often than not.

**Contents:** [Drafts, and Which Keywords Exist](#drafts-and-which-keywords-exist) · [The Skeleton](#the-skeleton) · [The Five Mistakes That Make a Schema Useless](#the-five-mistakes-that-make-a-schema-useless) · [Null, Absent, and Optional](#null-absent-and-optional) · [Composition](#composition) · [$ref and Where It Resolves](#ref-and-where-it-resolves) · [Error Output People Can Act On](#error-output-people-can-act-on) · [Performance](#performance) · [Deriving a Schema From Samples](#deriving-a-schema-from-samples) · [Code Generation](#code-generation) · [Testing the Schema Itself](#testing-the-schema-itself)

## Drafts, and Which Keywords Exist

`schema_draft` decides this. Mixing keywords across drafts is the most common cause of "the validator ignores my rule" — unknown keywords are **silently ignored** by the specification.

| Draft | Brings | Watch out |
|---|---|---|
| draft-07 | `if`/`then`/`else`, `definitions`, widest tool support | Any keyword **beside** a `$ref` is ignored — `{"$ref": "#/definitions/x", "description": "…", "minLength": 3}` silently drops `minLength` |
| 2019-09 | `unevaluatedProperties`, `unevaluatedItems`, `dependentRequired`, `$defs`, `$anchor`, annotations | `$ref` siblings now apply; `$recursiveRef` introduced here and replaced later |
| 2020-12 | `prefixItems` for tuples, `items` becomes schema-only, `$dynamicRef`/`$dynamicAnchor` | An array-valued `items` written for draft-07 means something different, and validators may accept it silently |
| OpenAPI 3.0 | A modified subset of draft-04/05 with `nullable: true` | Not JSON Schema; `nullable` does not exist in real JSON Schema, and `type: ["string","null"]` does not exist in 3.0 |
| OpenAPI 3.1 | Full 2020-12 alignment | `nullable` is gone; use the type array. Migrating 3.0 → 3.1 requires rewriting every nullable |

Always write `$schema` at the root. Without it, each validator picks its own default draft and two teams get different results from the same file.

## The Skeleton

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.invalid/schemas/order.schema.json",
  "title": "Order",
  "type": "object",
  "required": ["id", "status", "amount_cents", "currency"],
  "properties": {
    "id": { "type": "string", "minLength": 1 },
    "status": { "enum": ["pending", "paid", "failed", "refunded"] },
    "amount_cents": { "type": "integer", "minimum": 0 },
    "currency": { "type": "string", "pattern": "^[A-Z]{3}$" },
    "note": { "type": ["string", "null"], "maxLength": 500 },
    "items": {
      "type": "array",
      "minItems": 1,
      "maxItems": 500,
      "items": { "$ref": "#/$defs/lineItem" }
    }
  },
  "unevaluatedProperties": false,
  "$defs": {
    "lineItem": {
      "type": "object",
      "required": ["sku", "qty"],
      "properties": {
        "sku": { "type": "string" },
        "qty": { "type": "integer", "minimum": 1 }
      }
    }
  }
}
```

Every array gets `maxItems` and every string gets `maxLength` on an untrusted boundary — a schema without bounds validates a 400 MB document happily (`security.md`).

## The Five Mistakes That Make a Schema Useless

1. **`required` is a separate array, not a per-property flag.** Writing `"id": {"type": "string", "required": true}` puts an unknown keyword inside a property schema; it is ignored, and the field is optional. This is the single most common JSON Schema bug.
2. **A typo in a keyword is silently ignored.** `requried`, `mininum`, `additionalProperies` — all valid schemas, all no-ops. Turn on the validator's strict mode (ajv `strict: true` and equivalents), which converts unknown keywords into an error at compile time. Without it, a schema can be 100% inert and still "pass".
3. **`additionalProperties: false` does not cross `allOf`.** Each subschema only knows its own `properties`, so the base's fields count as additional in the branch and every valid document fails. Use `unevaluatedProperties: false` at the composition root (2019-09+), which sees annotations from all applied subschemas.
4. **`format` is an annotation, not an assertion, by default.** `format: "date-time"` on a value of `"yesterday"` passes unless format assertion is explicitly enabled (in ajv, by adding the formats plugin). Enable it, or back the format with a `pattern`.
5. **A property with no `type` validates anything.** `"email": {"description": "the user's email"}` accepts `42`, `null`, and an array. Every property gets a type or an `enum`.

## Null, Absent, and Optional

Three orthogonal switches — this table is the whole subject (Rule 3):

| Intent | How |
|---|---|
| May be missing | Leave it out of `required` |
| Must be present, may be null | In `required`, `"type": ["string", "null"]` |
| Must be present and non-null | In `required`, `"type": "string"` |
| May be missing, never null | Out of `required`, `"type": "string"` |
| Enum that allows null | The `null` value must be listed inside `enum`; a type array does not extend an enum |
| OpenAPI 3.0 | `nullable: true` alongside `type: string`; no type arrays |

Defaults: `default` is an **annotation**. No validator fills it in, and consumers that assume it does end up with `undefined` in production. If a default matters, apply it in code after validation and say so in the description.

## Composition

| Keyword | Semantics | Cost |
|---|---|---|
| `allOf` | All subschemas must pass | Cheap; the standard way to extend a base type. Breaks `additionalProperties` (mistake 3) |
| `anyOf` | At least one passes | Errors list every failed branch — noisy but complete |
| `oneOf` | Exactly one passes | Most expensive and the worst errors: a document that fails every branch produces N error sets and no indication of which branch was intended |
| `if`/`then`/`else` | Conditional | Readable, and errors point at the branch actually taken. Preferred over `oneOf` when a discriminating field exists |
| `not` | Negation | Produces an error that says only "must not match" — use once, never nested |

Discriminated unions: give each variant a `const` on the tag field and select with `if`/`then` on that `const`, or use `oneOf` with the tag as the first constraint in each branch so the error points at the right variant. In OpenAPI, `discriminator` gives generators the mapping — it does not make validation stricter.

## $ref and Where It Resolves

- `$id` at the root sets the base URI; every relative `$ref` resolves against it. Change `$id` and every reference in the file changes meaning.
- `#/$defs/name` is a JSON Pointer into the current document (`querying.md`). `other.json#/$defs/name` is a different document, which the validator must be able to load.
- Validators do **not** fetch `$ref` URLs from the network by default, and should never be allowed to on untrusted schemas (`security.md`). Register the referenced schemas explicitly, or bundle.
- **Bundling** inlines every external reference into a single document with `$defs`, keeping `$id`s so pointers still resolve. That is what ships to a service that must validate offline.
- Recursive structures (a comment tree) reference their own root: `{"$ref": "#"}` inside the child property. That works in every draft; `$dynamicRef` exists for the harder case of extending a recursive schema.
- Circular `$ref` between two files is legal and defeats naive bundlers — check the output before trusting it.

## Error Output People Can Act On

- Validators report an **instance path** as a JSON Pointer (`/items/3/price`) and a **schema path**. Log both: the first says which value, the second says which rule.
- `allErrors` (or the equivalent) collects every failure instead of stopping at the first. It costs measurable time on large documents and lets an attacker force maximum work on a hostile payload — enable it for developer-facing tooling, keep it off on public ingress (`security.md`).
- Map validation failures to your API's error shape once, at the boundary: field pointer → `errors[].pointer`, plus a human message. Passing raw validator output to a client leaks schema internals and reads like a stack trace (`api-payloads.md`).
- The worst error messages come from `oneOf` and `not`. If support engineers read these errors, restructure to `if`/`then` before writing a translation layer.

## Performance

- **Compile once** (Rule 8). Compilation walks and code-generates the whole schema; validation is a function call. A per-request compile is routinely 100-1000× the validation cost and shows up as inexplicable p99 latency.
- Ahead-of-time standalone code generation removes the compile step and the `eval`-style code generation from the runtime — required in CSP-restricted or AOT environments.
- Deeply nested `oneOf` chains multiply work: the validator tries each branch fully. Flatten with a discriminator.
- Enormous `enum` arrays (thousands of values) are linear scans in most implementations; use a `pattern` or validate against a lookup in code.
- Validate once at ingress, not at every layer (Rule 1).

## Deriving a Schema From Samples

The usual case: no schema exists and the producer will not write one.

1. Collect a real sample set, not one payload — 200-500 documents spanning at least one full business cycle, so weekend-only and monthly fields appear.
2. Infer the union of fields and types with a generator, then **tighten by hand**. Inferred schemas are permissive by construction.
3. Mark `required` only for fields present in **100%** of samples, and record the sample count in the schema's `description`. A field present in 99.6% is optional, and the 0.4% is the record that breaks production.
4. Turn a field into an `enum` only if the set is genuinely closed (statuses, currencies); an inferred enum from samples will reject the next valid value (`evolution.md`).
5. Add bounds from observed maxima with headroom, not from the maximum seen.
6. Run the finished schema against the whole sample set and against the *next* week of traffic before enforcing it. Enforce in log-only mode first: count failures, then switch to rejection.

**Save the result** to `~/Clawic/data/json/schemas/<name>.schema.json` with its provenance line, and add its `## Boxes` entry in the same turn (`memory-template.md`). Deriving a schema costs hours; nobody should pay twice.

## Code Generation

- Schema → types (quicktype, datamodel-code-generator, go-jsonschema, NSwag) is the right direction: one source of truth, generated at build time, checked into review.
- Types → schema is the pragmatic alternative when the code is the contract; the risk is that internal refactors change the public schema silently.
- Never hand-edit generated files. Regenerate in CI and fail the build on a diff — a stale generated model is a contract violation nobody can see.
- Generated optionals follow the null/absent distinction only if the schema encodes it (Rule 3); most generators collapse both to a nullable field, so check what you get.

## Testing the Schema Itself

- Every schema ships with **negative** cases. Positive-only tests pass against a schema that validates nothing (mistake 2).
- Minimum test set per schema: one valid document; one missing each required field; one with a wrong type per field; one with an extra property; one at each boundary (`minLength`, `maxItems`, `minimum`).
- Keep the fixtures next to the schema and redact them (`fixtures/`, `testing.md`).
- When a production payload fails validation, add it as a test case *before* changing the schema. Otherwise the fix loosens a constraint nobody re-tightens.
