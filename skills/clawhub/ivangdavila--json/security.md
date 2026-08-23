# Security — Parsing Input You Did Not Write

Three threats, in the order they actually happen: **resource exhaustion** (a small document that costs a lot to parse), **parser disagreement** (two systems read the same bytes differently), and **unsafe materialization** (the document chooses what code runs).

**Contents:** [Limits Before Parsing](#limits-before-parsing) · [Exhaustion Attacks](#exhaustion-attacks) · [Duplicate Keys and Parser Disagreement](#duplicate-keys-and-parser-disagreement) · [Prototype Pollution](#prototype-pollution) · [Unsafe Deserialization](#unsafe-deserialization) · [Mass Assignment](#mass-assignment) · [JSON as an Injection Carrier](#json-as-an-injection-carrier) · [Schema-Level Risks](#schema-level-risks) · [Secrets and Logs](#secrets-and-logs) · [Ingress Checklist](#ingress-checklist)

## Limits Before Parsing

Applied at the reader, before a parser allocates anything. `untrusted_default: true` means these ship with every parsing snippet.

| Limit | Default | Why this number |
|---|---|---|
| Body size | `max_payload_mb` (10 MB default) | Peak memory is 3-10× this (Rule 6); a 100 MB body is a 1 GB allocation |
| Nesting depth | 64 | Deeper than any legitimate business document; recursive-descent parsers overflow the stack well before their own limits |
| Array length | Per field, from the schema (`maxItems`) | An array is the cheapest amplification in the format |
| String length | Per field, from the schema (`maxLength`) | One string can be the entire body |
| Object key count | 10,000 unless the domain says otherwise | Guards against maps used as unbounded storage |
| Parse timeout | 1-2s for an API request | Turns any unforeseen amplification into a rejected request instead of a stuck worker |
| Number magnitude | Reject exponents beyond the double range | `1e999999` is legal grammar (Round-Trip Losses in SKILL.md) |

Enforce size at the proxy **and** in the application: the proxy protects the process, the application protects against internal callers, and a proxy-only limit disappears the day someone adds an internal route.

## Exhaustion Attacks

- **Depth bomb**: a 1 MB body of nothing but `[` is roughly a million levels of nesting. Parsers that recurse blow the stack; those that do not still allocate a million frames of state. Depth cap fixes it entirely.
- **Wide bomb**: `{"a":[[[...]]]}` repeated, or an array of a million empty objects — small on the wire, enormous once materialized as objects with per-object overhead. The byte cap is not enough; the memory multiplier is what matters.
- **Big number**: enormous integer literals cost superlinear time to convert in arbitrary-precision runtimes; Python caps integer-string conversion at 4300 digits by default for this reason (`languages.md`).
- **Key collision**: historically, thousands of keys hashing to the same bucket turned map insertion quadratic. Modern runtimes randomize hash seeds, which makes this largely historical — but only if the runtime is current and the map is the runtime's own.
- **Validator amplification**: `allErrors`-style validation on a hostile document does the maximum possible work. Off at public ingress, on in developer tooling (`schema.md`).
- **Decompression**: a gzipped body expands at up to ~1000:1. Cap the **decompressed** size, not the compressed one, and stop decompressing at the cap.

## Duplicate Keys and Parser Disagreement

The specification says names *should* be unique and leaves the rest undefined. Real behavior: most parsers take the last occurrence, some take the first, a few error.

The exploit is two components with different rules in the same request path: a gateway authorizes on `{"role":"user","role":"admin"}` reading `user`, the backend acts on it reading `admin`. Same bytes, two meanings, no bug in either component.

- **Reject duplicates at ingress** rather than picking a winner. Detection requires a parser that exposes key/value pairs before building the map (`debug.md`).
- Where rejection is impossible, ensure exactly one component parses the body and every downstream decision uses that component's parsed object — never re-parse the raw bytes later in the chain.
- Related disagreements worth knowing: leading zeros, `NaN` acceptance, trailing content after the top-level value, BOM tolerance, and comment tolerance. Any component parsing with a lenient parser next to one with a strict parser is a disagreement waiting to be found.

## Prototype Pollution

A JavaScript-specific failure with a precise mechanism, and most write-ups get it wrong:

- `JSON.parse('{"__proto__": {"isAdmin": true}}')` is **safe on its own**: the parser defines an own property named `__proto__` rather than assigning through the setter, so nothing is polluted yet.
- The damage happens **afterwards**, in code that walks the parsed object and *assigns*: a recursive merge, a `set(obj, path, value)` helper, a config loader, a query-string expander. That assignment goes through the prototype setter and every object in the process inherits the new property.
- Defenses, in order of value: (1) do not deep-merge untrusted input into shared objects; (2) skip the keys `__proto__`, `constructor` and `prototype` in any merge or path-set function; (3) use `Object.create(null)` or a `Map` for parsed data used as a lookup; (4) `Object.freeze(Object.prototype)` as a process-wide backstop; (5) validate against a schema with `additionalProperties: false`, which rejects the key before it reaches the merge.
- The reviver hook is not a defense by itself — deleting `__proto__` in a reviver helps only if nothing else re-introduces it.
- Python and Go have no equivalent, but "walk the document and set attributes by name" code in any language has the same shape: never let field names select attributes on an object you did not define.

## Unsafe Deserialization

The rule: **the document must never choose the class.**

- Jackson: polymorphic default typing (`enableDefaultTyping`, or `@JsonTypeInfo` over `Object`) lets a `@class`-style field name any class on the path — the root of the long CVE series. Use explicit `@JsonSubTypes` with a closed list and a discriminator you control (`schema.md`).
- .NET Newtonsoft: `TypeNameHandling` set to anything but `None` is the same vulnerability. `System.Text.Json` has no equivalent by default, which is one reason to prefer it.
- Python: `json` itself is safe; `jsonpickle`, `pickle` and `yaml.load` without a safe loader are not — a "JSON-ish" loader that reconstructs arbitrary objects is a code-execution primitive.
- Any language: a custom deserializer that instantiates by a name from the payload, or dispatches to a function by a payload field, reproduces the vulnerability without a library.
- Safe shape: parse to plain data, validate against a schema, then construct your own types from the validated data. Two steps, no reflection driven by input.

## Mass Assignment

- Binding a request body straight onto a persistence model lets a caller set `is_admin`, `balance_cents`, `owner_id` or `created_at`.
- Allowlist the fields each endpoint accepts, per role. A denylist is missing whatever field was added last week.
- The equivalent for PATCH is an allowlist of patchable pointers (`patching.md`).
- Server-controlled fields belong in the response, never in the accepted request. If the same DTO is used for both directions, one of the two is wrong.

## JSON as an Injection Carrier

| Sink | Vector | Defense |
|---|---|---|
| HTML page | `</script>` inside a string value breaks out of an inline script block | Escape `<`, `>`, `&` as escapes, or use a `type="application/json"` block and parse the text (`encoding.md`) |
| NoSQL query | A field whose value is an object: `{"password": {"$ne": null}}` matches everything | Reject non-scalar values where a scalar is expected — a schema does this for free (`schema.md`) |
| SQL | String-concatenating a JSON value into a query | Parameters, always; the JSON layer changes nothing (`databases.md`) |
| Logs | A newline inside a value forges a log line, or breaks a log parser | Structured logging that escapes values, never string interpolation of user text into a log line |
| Shell | A value interpolated into a command | Never; pass through a file or argument array |
| Path / filename | A value used to build a path (`../../etc/passwd`) | Validate against a pattern and resolve against a fixed base |
| Bidi and zero-width characters | A value that renders differently than it parses | Reject control and bidi characters in identifiers (`encoding.md`) |

## Schema-Level Risks

- **Remote `$ref` fetching** turns schema loading into SSRF and into a dependency on somebody's uptime. Register schemas explicitly or bundle them; never allow network resolution for a schema you did not write (`schema.md`).
- A regex in `pattern` can be catastrophically backtracking: nested quantifiers over attacker-controlled strings are a ReDoS. Keep patterns anchored and simple, and bound the string with `maxLength` first — the length cap alone defuses most of it.
- A schema is public information about your internals. Publishing the validation schema is usually fine; echoing raw validator errors to clients leaks structure and reads like a stack trace (`api-payloads.md`).

## Secrets and Logs

- Payloads carry tokens routinely, and logging middleware writes bodies to three destinations before anyone thinks about it. Redact at the serializer, with an **allowlist** of loggable fields, not a denylist of secret-looking names.
- A JWT in a payload is not opaque: its claims are base64url, readable by anyone with the log. Treat the whole token as a credential (`signing.md`).
- Error responses must not echo the offending value. "Invalid value for `password`: hunter2" is a log entry and a support ticket with a live credential in it.
- Nothing written under `~/Clawic/data/` holds a secret value — pointers only, and stable placeholders for personal data in fixtures (`memory-template.md`).

## Ingress Checklist

Run against any endpoint that accepts JSON from outside:

| Check | Passing looks like |
|---|---|
| Size cap | Enforced at the proxy and in the app, on the decompressed size |
| Depth cap | Explicit, ≤64 unless justified |
| Field bounds | `maxLength`/`maxItems` on every string and array in the schema |
| Duplicate keys | Rejected, or provably parsed exactly once in the whole path |
| Content type | `application/json` required; `text/plain` not accepted (it bypasses CORS preflight) |
| Validation | Schema validated at the boundary, before business logic (Rule 1) |
| Deserialization | No type information taken from the document |
| Field binding | Allowlist per endpoint and role |
| Merge functions | No deep merge of untrusted input; `__proto__`/`constructor`/`prototype` skipped |
| Errors | Generic to the client, detailed in the log, offending values never echoed |
| Logging | Allowlist serializer; no full bodies at info level |

**When the limits are set for a codebase**, write them as a row in `## Conventions` of `memory.md` (size, depth, duplicate-key policy, with the date). **After any incident**, write the runbook to `~/Clawic/data/json/artifacts/<kebab-name>.md` with its `## Boxes` line, every secret replaced by its pointer (`memory-template.md`).
