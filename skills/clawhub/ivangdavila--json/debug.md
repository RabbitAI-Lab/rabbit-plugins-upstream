# Debug — From Symptom to the Layer That Broke

Order of work: (1) confirm it is even JSON, (2) find the smallest document that still fails, (3) name the layer — bytes, grammar, type mapping, contract, size. Skipping step 2 is why JSON bugs take hours: a 40 MB document hides its one bad record.

**Before diagnosing a feed you have seen before**, read `## Producers` in `~/Clawic/data/json/memory.md` (or `producers.md` if `## Boxes` points there) and its `contracts/<producer>.md`. Half of these symptoms are a quirk somebody already paid for.

**Contents:** [Is It Even JSON](#is-it-even-json) · [Parse Error Messages](#parse-error-messages) · [Offsets Lie in Three Different Ways](#offsets-lie-in-three-different-ways) · [Bisecting a Large Document](#bisecting-a-large-document) · [Parsed Fine, Data Is Wrong](#parsed-fine-data-is-wrong) · [Works in curl, Fails in Code](#works-in-curl-fails-in-code) · [Works for 99% of Records](#works-for-99-of-records) · [Validity Checks Worth Running](#validity-checks-worth-running)

## Is It Even JSON

Print the first 200 bytes before anything else. The most common "JSON parse error" is not JSON at all:

| First bytes | What it is | Fix |
|---|---|---|
| `<!DOCTYPE`, `<html`, `<?xml` | An HTML error page, a login redirect, a captive portal, or a proxy | Check the status code and `Content-Type` before parsing; the error text is in the HTML |
| `EF BB BF` then `{` | UTF-8 BOM | Strip the three-byte `EF BB BF` prefix before parse; fix the producer's writer (`encoding.md`) |
| `[object Object]` | Something stringified a JS object with `String()` instead of `JSON.stringify` | Fix the caller, not the parser |
| `{...}` but gibberish | gzip/br body decoded as text, or UTF-16 read as UTF-8 | Decompress first; check `Content-Encoding` |
| Empty | 204, an early-returning proxy, or a body already consumed by a middleware | Never call parse on a zero-length body — that is not `null` |
| `{"a":1}{"b":2}` | Concatenated documents or NDJSON read as one | One parse per line, or a streaming decoder (`streaming.md`) |

## Parse Error Messages

| Message (any language) | What it almost always is |
|---|---|
| `Unexpected end of JSON input` / `Expecting value: line 1 column 1` on an empty string | Truncated or empty body: response cut by a proxy body limit, a stream read before completion, or a `Content-Length` mismatch |
| `Unexpected token } ` after a value | Trailing comma before the brace — the parser reports the brace, the error is the comma before it |
| `Unexpected token in string` / `Invalid control character` | A raw newline, tab, or U+0000-U+001F inside a string literal; usually a log line or user text pasted into a value |
| `Unexpected token '` | Single quotes — Python `str(dict)`, or a JS object literal, not JSON |
| `Unexpected non-whitespace character after JSON` | Two documents in one buffer, or a duplicated write |
| `Bad escaped character` | A Windows path with single backslashes, `\d` from a regex, or a stray `\` at the end of a value |
| `Unterminated string` | The document was cut mid-value: size limit, killed process, or disk full |
| `Maximum call stack size exceeded` / `RecursionError` | Nesting depth beyond the parser's recursion limit; treat as hostile input until proven otherwise (`security.md`) |
| `Cannot create a string longer than 0x1fffffe8 characters` (Node) | The file exceeds V8's ~512 MB string cap; you cannot `readFile` your way out of it (`streaming.md`) |

## Offsets Lie in Three Different Ways

The number in the error is not always a byte offset, and never points at the *cause*:

- **Node/V8** reports `position N` as a 0-based index into the JS string — UTF-16 code units, so any emoji before the error shifts it by one per emoji.
- **Python** reports `line L column C (char N)`, where `N` counts Unicode code points, not bytes.
- **Go** reports `offset N` in bytes, and `json.SyntaxError.Offset` points **after** the offending token.

Practical rule: **look at the 40 characters before the reported position, not at it.** A parser reports where it noticed, and it notices at the first token that cannot follow what came before — one token past the actual mistake.

## Bisecting a Large Document

For an array or NDJSON that fails somewhere:

1. Confirm the whole file fails and a known-good subset passes, or you are chasing the wrong file.
2. Halve it at record boundaries — never at byte offsets, which cut strings in half and manufacture a second error.
3. For NDJSON, validate line by line and print the line number of the first failure; a single bad line in six million is the normal case.
4. For a single huge object, extract the top-level keys with a streaming parser and validate each subtree separately (`streaming.md`).
5. Once isolated, reduce the failing record to the smallest document that reproduces: drop siblings, shorten strings, keep the structure. Ten lines is a bug report; 40 MB is a request for someone else's afternoon.

## Parsed Fine, Data Is Wrong

Grammar is not the problem; the type mapping or the contract is (`languages.md`).

| Symptom | Cause | Where |
|---|---|---|
| An id ends in `0` or `2` when it should not | Integer beyond 2^53−1 through a double | `numbers.md` |
| Money is off by fractions of a cent | Float arithmetic, or a decimal parsed as binary float | `numbers.md` |
| A field is missing that is in the payload | Unknown-field policy, name mapping, or case sensitivity (Defaults That Decide Behavior in SKILL.md) | `languages.md` |
| A field is `null` in the object but absent in the payload | Your language cannot distinguish the two without a pointer or option type (Rule 3) | `api-payloads.md` |
| A value appears twice with different content | Duplicate keys; your parser took the last, theirs took the first | `security.md` |
| Accents or emoji broken | Byte layer, not JSON | `encoding.md` |
| A date is off by hours, or by a day | No offset in the timestamp, or an instant treated as wall-clock | `api-payloads.md` |
| A boolean is `"false"` (string) and reads as true | Producer stringifies everything; a truthiness check on a non-empty string | Validate types at ingress (Rule 1) |
| Array order changed | The producer has no ordering guarantee; JSON preserves array order, so the change is upstream (databases return unordered rows without `ORDER BY`) | `databases.md` |

## Works in curl, Fails in Code

| Difference | Effect |
|---|---|
| `curl -d` vs `--data-binary` | `-d` strips newlines from the payload, which changes the bytes and breaks any signature over them (`signing.md`) |
| Missing `Content-Type: application/json` | Most frameworks skip JSON body parsing entirely and hand you an empty object, not an error |
| Shell quoting | Single-quoted heredoc in the shell preserves the document; double quotes let the shell expand `$` and backticks inside it |
| Automatic decompression | curl sends `Accept-Encoding` only with `--compressed`; an HTTP client that always sends it gets a gzipped body the code forgot to decode |
| Proxy body limits | A reverse proxy truncates or rejects above its own cap before your handler sees it — the symptom is a truncated document, not a 413 |
| Client-side re-serialization | An interceptor or middleware parsed and re-emitted the body; key order and formatting changed (Rule 5) |

## Works for 99% of Records

The pattern that eats days. Causes, in order of frequency:

1. **One record has a different type for a field** — `"count": null` in 1 of 200k, or `[]` where `{}` was expected from a PHP producer.
2. **An optional object is `[]` instead of absent** (PHP empty arrays) or `""` instead of null.
3. **A record contains an unescaped control character**, usually because a user pasted text with a newline into a name field.
4. **A number crosses 2^53−1** for the first time when the id sequence grows.
5. **Deeper nesting than the rest**, hitting a depth limit only for that record.

Find it with a validator that reports the record index, not the first error: validate every record, collect all failures, and print the distinct error types with counts. One pass over the whole dataset beats five bisections.

## Validity Checks Worth Running

- Whole-file validity, exit code only: `jq empty file.json` — silent and zero means valid.
- Reformatting as a check: piping through a strict pretty-printer surfaces BOMs, trailing commas, and duplicate keys the eye misses.
- Duplicate keys: a normal parser will not tell you. Parse with a hook that receives key/value **pairs** (`object_pairs_hook` in Python, a custom decoder elsewhere) and compare the pair count to the resulting map size.
- Schema conformance across a whole dataset, with the failing instance path in the output (`schema.md`).
- Byte-level: check the first three bytes for a BOM and the last byte for a missing newline before blaming the parser.

**After a diagnosis that cost real time**, write the cause in one line in `## Pain Points` of `memory.md`, and the producer's quirk as a row in `## Producers` (`memory-template.md`) — with the workaround, not just the symptom.
