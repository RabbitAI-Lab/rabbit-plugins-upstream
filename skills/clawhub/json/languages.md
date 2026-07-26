# Languages — What Each Stack Turns Your Document Into

The document is the same on both ends of the wire; the objects are not. Every entry here is a default that produces a different value, not an opinion about style.

**Before writing a decoder for a known producer**, read its `contracts/<producer>.md` and the `## Producers` row in `~/Clawic/data/json/memory.md`: the quirk you are about to rediscover is usually written down.

**Contents:** [JavaScript and TypeScript](#javascript-and-typescript) · [Python](#python) · [Go](#go) · [Java and Kotlin (Jackson)](#java-and-kotlin-jackson) · [C# and .NET](#c-and-net) · [PHP](#php) · [Ruby](#ruby) · [Rust (serde_json)](#rust-serde_json) · [Cross-Language Interop Table](#cross-language-interop-table) · [Choosing How Strict To Be](#choosing-how-strict-to-be)

## JavaScript and TypeScript

- `JSON.stringify` **drops** `undefined`, functions and symbols from objects and turns them into `null` inside arrays. The same value, two behaviors, one document.
- `toJSON()` runs silently if it exists. `Date` becomes an ISO string; a class with a `toJSON` you forgot about becomes whatever it returns.
- `Map`, `Set` and typed arrays serialize as `{}` — no error, no data.
- `BigInt` throws `TypeError`. It is the only round-trip loss that fails loudly; serialize as a string.
- Key order on output: integer-like keys first, ascending, then string keys in insertion order. This breaks naive canonicalization (`signing.md`).
- The replacer argument is the cleanest allowlist there is: `JSON.stringify(obj, ["id", "name"])` emits only those keys, recursively — a one-line way to keep secrets out of a log.
- `JSON.parse` with a reviver visits every node bottom-up; returning `undefined` deletes the key. Use it for typed reconstruction, never for validation.
- TypeScript types are erased: `JSON.parse` returns `any`, and a cast is a lie the compiler accepts. Parse into `unknown` and validate (Rule 1).

## Python

- `json.dumps` defaults to `allow_nan=True` and emits `NaN`, `Infinity`, `-Infinity` — **invalid JSON** that Go, Java and browsers reject. Set `allow_nan=False` on anything that leaves the process.
- `json.dumps` defaults to `ensure_ascii=True`, escaping every non-ASCII character: `"café"` becomes `"café"`. Legal, larger, and it hides encoding problems. `ensure_ascii=False` plus a UTF-8 write is the honest form (`encoding.md`).
- Integers are arbitrary precision, so Python parses `9007199254740993` correctly and hands the browser a number it cannot hold. Python is often the producer in a precision bug it will never see (`numbers.md`).
- Floats: `parse_float=Decimal` on the way in, and a custom encoder on the way out, or money loses cents.
- Dict keys that are not strings are coerced: `{1: "a"}` serializes to `{"1": "a"}` and never comes back as an int. `True` as a key becomes `"true"`.
- Duplicate keys: last wins, silently. `object_pairs_hook` is the only way to see them.
- `datetime` is not serializable — a `TypeError`, which is the good outcome; the bad one is a `default=str` that emits a non-RFC-3339 string with a space instead of `T`.
- Since 3.11, converting integers with more than 4300 digits to or from a string raises `ValueError` by default (a DoS mitigation). Documents with enormous integer literals fail to parse until the limit is raised deliberately.

## Go

- Unknown fields are ignored by default. `dec.DisallowUnknownFields()` is the difference between catching a renamed field and shipping nulls.
- Numbers decoded into `any` become `float64` — every int64 id above 2^53−1 corrupts. `dec.UseNumber()` gives you a `json.Number` you can convert exactly.
- Field matching is case-insensitive when there is no exact tag match, which surprises people the other direction: `userid` binds to `UserID`.
- `omitempty` omits zero values, so `0`, `false` and `""` disappear — it cannot express "present and zero". Use a pointer or `json.RawMessage` when absent and zero differ (Rule 3).
- A nil slice marshals to `null`, an empty slice to `[]`. Consumers that iterate without a null check break on the first empty result.
- `[]byte` marshals to base64, which is usually what you want and never what you expect the first time.
- Unexported fields are silently skipped. A struct with no tags and lowercase fields marshals to `{}`.
- Decoding into a struct with a `json.RawMessage` field defers that subtree, which is how you forward bytes unchanged and keep a signature valid (Rule 5).
- A v2 of `encoding/json` has been in development with different defaults; check which one your toolchain uses before relying on any behavior above (verified 2026-07).

## Java and Kotlin (Jackson)

- `FAIL_ON_UNKNOWN_PROPERTIES` is **on** by default: a producer adding a field breaks your consumer. This is the exact opposite of Go and the reason the same payload works in one service and 500s in another. Disable it for third-party input (`evolution.md`).
- Never enable polymorphic default typing (`enableDefaultTyping`, `@JsonTypeInfo` on `Object`): it turns any JSON into a class-instantiation primitive and is the root of the Jackson deserialization CVE family (`security.md`).
- Floats decode to `double` unless `USE_BIG_DECIMAL_FOR_FLOATS` is set; for money that flag is not optional.
- `@JsonInclude(NON_NULL)` vs `NON_ABSENT` vs `NON_EMPTY` are three different contracts — `NON_EMPTY` also drops empty strings and collections, which is rarely what the API meant.
- Kotlin needs the Kotlin module registered, or non-null types get null through reflection and blow up far from the parse.
- Java records and `@JsonCreator` remove the need for setters; without either, a class with no default constructor fails at runtime, not compile time.

## C# and .NET

- `System.Text.Json` matches property names **case-sensitively** by default; Newtonsoft.Json did not. Migrating a service and getting silent nulls is the single most common .NET JSON bug. `PropertyNameCaseInsensitive = true`, or generate the correct names.
- Default output escapes anything non-ASCII and HTML-sensitive: `é` becomes `é`, `+` becomes `+`. `JavaScriptEncoder.UnsafeRelaxedJsonEscaping` emits UTF-8 directly and is safe for non-HTML contexts.
- `JsonSerializerOptions` is expensive to construct and caches its metadata — create one static instance, or serialization dominates the profile (`performance.md`).
- Default naming is exact-match; `PropertyNamingPolicy = JsonNamingPolicy.CamelCase` handles output only, not input matching, unless case-insensitivity is also on.
- `System.Text.Json` will not serialize fields by default, only properties; source generators change the tradeoffs for AOT.

## PHP

- `json_encode` returns `false` on invalid UTF-8 rather than throwing — the symptom is an empty body with a 200. Always pass `JSON_THROW_ON_ERROR`.
- Empty arrays: `[]` in PHP is both an empty list and an empty map, and it encodes as `[]`. A consumer expecting an object gets an array for exactly the empty case. Cast to `(object)` or use `JSON_FORCE_OBJECT`, and expect this quirk from any PHP producer.
- Large integers: `json_decode($s, true, 512, JSON_BIGINT_AS_STRING)` keeps them exact; without it they become floats.
- The default decode depth is 512; deeply nested input fails with a depth error rather than exhausting the stack.
- `json_decode($s, true)` gives arrays, `false` gives `stdClass`. Mixing the two in one codebase produces "cannot use object as array" at runtime.

## Ruby

- `JSON.parse` returns string keys; `symbolize_names: true` is a different object graph, so pick one per boundary.
- `to_json` is defined per class and Rails overrides it widely — `Time#to_json` and `ActiveSupport::TimeWithZone#to_json` do not emit the same string as `Time#iso8601` unless configured.
- `JSON.generate` raises on NaN/Infinity by default; `JSON.dump` allows them. The safe default is the strict one.
- `OpenStruct` from JSON is convenient and turns typos into `nil` forever.

## Rust (serde_json)

- Unknown fields are ignored; `#[serde(deny_unknown_fields)]` for config, tolerant for third-party input.
- Key order is not preserved unless the `preserve_order` feature is enabled (which swaps the map implementation).
- Numbers: without the `arbitrary_precision` feature, a large integer or a high-precision decimal is normalized through `u64`/`i64`/`f64`; with it, `Number` keeps the literal text.
- `Option<T>` distinguishes null from absent only with `#[serde(skip_serializing_if = "Option::is_none")]` on output; on input, absent and null both give `None` unless you use `Option<Option<T>>` with `deserialize_with` (Rule 3).
- `#[serde(untagged)]` enums produce error messages that name no field at all — fine for internal use, painful as a public contract.
- `Box<RawValue>` forwards a subtree byte-for-byte, the equivalent of Go's `json.RawMessage`.

## Cross-Language Interop Table

The five decisions that must be agreed between producer and consumer, and what happens if nobody agrees:

| Decision | If unstated | Set it to |
|---|---|---|
| Unknown fields | Go/Rust ignore, Jackson throws — the same payload succeeds and fails depending on which service reads it | Tolerant inbound, strict for config (Choosing How Strict To Be) |
| Big integers | Python and Java produce them, JavaScript silently corrupts them | Strings above 2^53−1 (Rule 2) |
| Absent vs null | Go `omitempty` cannot express it; Rust needs a nested Option; Java needs `NON_ABSENT` | Declare per field in the schema (Rule 3) |
| Empty collections | PHP emits `[]` for an empty object; Go emits `null` for a nil slice | Always emit `[]` and `{}`, never `null`, for collections |
| Non-ASCII | Python and .NET escape by default, Go and JS do not | UTF-8 on the wire, escapes only where the target needs them (Rule 4) |

**When a stack's default surprises you on a real producer**, write the row in `## Producers` of `memory.md` with the workaround, and the language-level rule in `## Conventions` if the codebase adopts it (`memory-template.md`).

## Choosing How Strict To Be

One default with an escape hatch, applied per direction — not per codebase:

- **Reading your own config files**: strict. Unknown fields are typos; reject them and name the key. A silently ignored config key is a support ticket with no evidence.
- **Reading another system's API**: tolerant. Unknown fields are the mechanism that lets them ship without breaking you (Rule 7).
- **Reading user-submitted documents**: strict *and* limited — validate against a schema, cap size and depth, reject duplicates (`security.md`).
- **Writing anything public**: strict about what you emit, so consumers can be strict too — no NaN, no undefined-shaped keys, collections never null.
