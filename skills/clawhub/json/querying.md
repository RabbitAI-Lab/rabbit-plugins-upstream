# Querying — Pointer, JSONPath, JMESPath, and jq

Four path languages with overlapping syntax and incompatible semantics. Picking the wrong one costs an afternoon of expressions that look right and return nothing.

**Before writing an expression against a familiar payload**, read `## Queries` in `~/Clawic/data/json/memory.md` (or `queries.md` if `## Boxes` points there) — the hard ones are already written.

**Contents:** [Which Language, and Who Accepts It](#which-language-and-who-accepts-it) · [JSON Pointer](#json-pointer) · [JSONPath](#jsonpath) · [JMESPath](#jmespath) · [jq](#jq) · [jq Idioms Worth Memorizing](#jq-idioms-worth-memorizing) · [Keys That Break Path Syntax](#keys-that-break-path-syntax) · [When Not to Use a Path Language](#when-not-to-use-a-path-language)

## Which Language, and Who Accepts It

| Need | Language | Notes |
|---|---|---|
| Address exactly one location in a document | **JSON Pointer** (RFC 6901) | Not a query language: no wildcards, no filters. Used by JSON Patch, validator error output, OpenAPI `$ref` |
| Extract a set of values with wildcards and filters, in a config file or a policy | **JSONPath** (RFC 9535, 2024) | Standardized late; implementations written before the RFC differ on unions, slices and functions |
| Query inside AWS tooling or anything that embedded it | **JMESPath** | The `--query` language of the AWS CLI; strong projections, no parent access, no arbitrary computation |
| Transform, reshape, aggregate, or produce non-JSON output | **jq** | A full language, not a path syntax. The default for anything on a command line |
| Query inside a database | The engine's SQL/JSON path | Postgres `jsonb_path_query`, MySQL `JSON_EXTRACT` (`databases.md`) |

The controlling constraint is usually **what the tool accepts**, not which is nicest: a validator emits Pointers, a policy engine takes JSONPath, the AWS CLI takes JMESPath. Record which one an expression is written in, in the `Tool` column of `## Queries` (`memory-template.md`) — the same string is invalid or, worse, means something different in the other three.

## JSON Pointer

- Syntax: `/data/items/0/price`. A leading `/` per segment; array indices are numbers; the empty string addresses the whole document.
- Escaping, and it is the only escaping: `~0` is a literal `~`, `~1` is a literal `/`. A key containing a slash is addressable only this way. Escape `~` **before** `/`, or the escapes eat each other.
- `-` as the last segment means "the position after the last array element" — only meaningful in JSON Patch `add` (`patching.md`).
- A key that is a number is indistinguishable from an array index in the pointer text; the document's structure disambiguates.
- Where you meet it: validator error paths, JSON Patch `path`/`from`, `$ref` fragments in JSON Schema and OpenAPI, and field-level API errors (`api-payloads.md`). Emitting pointers in your own error responses lets a client map an error to a form field mechanically.

## JSONPath

- Shape: `$.store.book[*].author`, `$..price` (recursive descent), `$.book[?@.price < 10]` (filter), `$.book[0,2]` (union), `$.book[1:3]` (slice).
- RFC 9535 fixed a decade of divergence, but **the implementation you are using may predate it**: check behavior for the descendant operator combined with filters, for union order, and for whether functions like `length()` exist at all.
- No parent or sibling access: once you descend, you cannot climb. If the result must include a value from an ancestor, JSONPath is the wrong tool.
- Filters compare against literals and simple paths; there is no arithmetic worth relying on across implementations.
- Result is always a list, even for a single match — a caller that assumes a scalar breaks on the first document with two matches.

## JMESPath

- Shape: `Reservations[].Instances[].InstanceId`, `Items[?Status=='active'].Name`, `sort_by(Items, &Price)`, `Items[*].{id: Id, cost: Price}` (multiselect hash).
- `[]` flattens a projection; `[*]` does not. That distinction is the single most common JMESPath confusion: `a[].b` flattens nested lists, `a[*].b` preserves the nesting level.
- Projections stop at the first step that returns null, so a filter on a field that is absent silently yields nothing rather than an error.
- String literals in filters use single quotes: `[?Status=='active']`. Double quotes mean an identifier and will fail to match.
- Pipe `|` stops a projection and starts a fresh evaluation: `Items[?Price>`10`] | length(@)`.
- Functions are a fixed, small set. There is no user-defined function, no arbitrary arithmetic on fields, and no parent access — by design, which is why it is safe to embed.

## jq

The one to reach for on a command line, and the only one of the four that can reshape.

- Filters compose left to right with `|`. Every filter takes a stream of values and produces a stream of values — that stream model explains most surprises (a filter producing nothing is not an error).
- `.a.b` on a missing key yields `null`; on a **non-object** it is an error. `?` suppresses it: `.a.b?`. `//` supplies a fallback: `.a.b // "unknown"` — note it also fires on `false`, not only on null.
- Output flags matter more than the language: `-r` emits raw strings without quotes (for shell consumption), `-c` emits one compact line per result (this is how you write NDJSON), `-j` joins without newlines, `-e` sets the exit code from the last output, `-n` starts with no input, `-s` slurps all input into one array (and defeats streaming, `streaming.md`).
- Arguments: `--arg name value` injects a **string**; `--argjson name '{"a":1}'` injects parsed JSON. Interpolating a shell variable into the program text instead is how a quote in the value becomes a syntax error or worse.
- Key order is input order; `-S` sorts keys. Sorting for a diff is fine; sorting for a hash is not canonicalization (`signing.md`).
- Numbers: jq ≥1.7 preserves the literal text of numbers it does not modify, so ids above 2^53−1 survive a pass-through; the moment a number enters arithmetic it becomes a double and loses precision (`numbers.md`).

## jq Idioms Worth Memorizing

| Need | Expression |
|---|---|
| Array to NDJSON | `jq -c '.[]'` |
| Filter records | `.[] \| select(.status == "failed")` |
| Reshape to a smaller object | `.[] \| {id, name: .user.name, n: (.items \| length)}` |
| Default for a missing field | `.count // 0` |
| Rename or drop keys | `with_entries(select(.key \| startswith("_") \| not))` |
| Key an array by id (array → object) | `INDEX(.id)`, or `map({(.id): .}) \| add` |
| Object → rows | `to_entries[] \| [.key, .value] \| @tsv` |
| Group and count | `group_by(.type) \| map({type: .[0].type, n: length})` |
| Sum money safely | `map(.amount_cents) \| add` (integers, never floats) |
| Unique by a field | `unique_by(.email)` |
| Find every path to a value | `[paths(. == "target")]` |
| Rewrite every string in the tree | `walk(if type == "string" then ascii_downcase else . end)` |
| Redact before saving a fixture | `walk(if type == "object" then with_entries(if .key \| test("token\|secret\|password") then .value = "<redacted>" else . end) else . end)` |
| CSV output | `.[] \| [.id, .email, .amount_cents] \| @csv` |
| Merge two documents | `jq -s '.[0] * .[1]'` (deep merge of objects; arrays are replaced, not concatenated) |
| Validate a file, exit code only | `jq empty file.json` |
| Stream a huge document | `jq --stream` emits `[path, value]` events instead of building the tree |

`*` merges objects recursively but **replaces** arrays; `+` merges shallowly and **concatenates** arrays. Choosing the wrong one is the standard jq merge bug (`patching.md`).

## Keys That Break Path Syntax

Every path language has a fallback for awkward keys, and every one of them is different:

| Key | jq | JSON Pointer | JSONPath |
|---|---|---|---|
| `user-name` (hyphen) | `.["user-name"]` | `/user-name` | `$['user-name']` |
| `a.b` (dot in the key) | `.["a.b"]` | `/a.b` | `$['a.b']` |
| `a/b` (slash) | `.["a/b"]` | `/a~1b` | `$['a/b']` |
| `` (empty string key) | `.[""]` | `/` | `$['']` |
| `0` as an object key | `.["0"]` | `/0` (ambiguous with an index) | `$['0']` |
| Key with a quote or newline | `.["a\"b"]` | escape per RFC 6901 only for `~` and `/` | implementation-dependent |

Bare-word paths are a convenience that fails on real data. When generating expressions programmatically, always emit the bracket form.

## When Not to Use a Path Language

- The transformation needs conditional logic across multiple documents, external lookups, or error handling: write code, and use a real model (`languages.md`).
- The result feeds a typed system: parse into structs and let the type checker do the work, rather than shipping stringly-typed path expressions into production.
- The document is bigger than memory: most path tools materialize the whole document. Stream first, then query per record (`streaming.md`).
- The data lives in a database: an expression over a fetched blob loses the index. Query with the engine's JSON path so the index is used (`databases.md`).

**When an expression takes more than one attempt**, write it to `## Queries` in `memory.md` with the tool, what it extracts and which producer it runs against (`memory-template.md`). Path expressions are the highest re-use, lowest re-derivation-value artifact in this domain.
