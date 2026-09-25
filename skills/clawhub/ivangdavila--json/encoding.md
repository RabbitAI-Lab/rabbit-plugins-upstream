# Encoding — Bytes, Unicode, and Where Text Breaks

JSON text exchanged between systems is UTF-8 (RFC 8259 §8.1). Everything in this file is a consequence of somebody's stack not believing that.

**Contents:** [The Byte Layer](#the-byte-layer) · [Escapes](#escapes) · [Surrogates and Emoji](#surrogates-and-emoji) · [Mojibake Decoder](#mojibake-decoder) · [Control Characters](#control-characters) · [Embedding JSON in Other Formats](#embedding-json-in-other-formats) · [Content-Type and Charset](#content-type-and-charset) · [Normalization and String Identity](#normalization-and-string-identity) · [Line Endings](#line-endings)

## The Byte Layer

| Rule | Detail |
|---|---|
| UTF-8, no BOM | A BOM (`EF BB BF`) must not be added; parsers *may* ignore it, which is why the same file works in Python and fails in Node |
| UTF-16 and UTF-32 | Legal only inside a closed ecosystem. A UTF-16 file read as UTF-8 looks like `{` followed by a null byte — often reported as "invalid control character" |
| Byte length ≠ character length | `"café"` is 5 bytes, 4 code points, 4 UTF-16 units. Size limits must be measured in bytes, cursors in code points, and never mixed (`security.md`) |
| Invalid UTF-8 in a value | PHP returns `false` from `json_encode`; Go replaces with U+FFFD; Python raises. The producer decides which corruption you get |
| Empty file | Not `null`, not `{}` — a parse error. An empty response body is an API defect |

Detect the encoding before blaming the parser: check the first four bytes. `EF BB BF` is a UTF-8 BOM, `FF FE` or `FE FF` is UTF-16, and a `00` in the first four bytes of what should be ASCII punctuation means a wide encoding.

## Escapes

- Required escapes inside a string: `"` `\` and every character U+0000-U+001F. Everything else may be literal.
- Optional escapes that are legal but rarely useful: `\/` (a historical convention for embedding in HTML, harmless), `\uXXXX` for any BMP character.
- Escaping all non-ASCII (`ensure_ascii=True` in Python, the .NET default) costs up to 6 bytes per character and is only worth it when the transport is genuinely not 8-bit clean. It also hides real encoding bugs behind a correct-looking document (Rule 4).
- `\uXXXX` is **UTF-16**, not a code point: characters above U+FFFF need two escapes. `\u1F600` is therefore not the grinning-face emoji: a parser reads `\u1F60` (a Greek omega with psili) followed by the literal digit `0`.
- A backslash in data must be doubled. Windows paths and regex sources are the usual source of "Bad escaped character".

## Surrogates and Emoji

- U+1F600 written as escapes is the surrogate pair `\uD83D\uDE00`. Written as UTF-8 bytes it is four bytes and needs no escaping at all.
- A **lone surrogate** — `"\uD800"` with no pair — is accepted by many parsers and cannot be encoded as valid UTF-8. Since ES2019, `JSON.stringify` emits lone surrogates as escapes rather than producing invalid UTF-8 output ("well-formed stringify"), which keeps the document parseable but does not make the string meaningful.
- Emoji shift every offset-based error message: a parse error "at position 300" in Node counts UTF-16 units, so a document with 20 emoji before the error is 20 units off from the character you would count by hand (`debug.md`).
- Truncating a string by bytes or by UTF-16 units splits emoji and combining sequences. Truncate by grapheme cluster, or accept that a name field will occasionally end in half a flag.
- Emoji, skin-tone modifiers and flags are multi-code-point sequences: a family emoji is three people joined by two zero-width joiners, five code points for one visible glyph. `length` will not match what a human counts, in any language.

## Mojibake Decoder

Read the symptom, name the double-encoding:

| Looks like | What happened |
|---|---|
| `caf` + `Ã` + `©` (two visible characters where one accent belongs) | UTF-8 bytes interpreted as Latin-1, then re-encoded as UTF-8 — the classic double encoding |
| The same two characters, but the stored bytes are correct UTF-8 | A display or terminal encoding problem, not a data problem — check before "fixing" the data |
| `caf?` or `caf□` | Transcoded through an encoding without the character; the data is gone, not recoverable |
| `\u00e9` visible in rendered text | The document was escaped twice: a JSON string containing a JSON document, never parsed (`api-payloads.md`) |
| `"{\"a\":1}"` | Same thing: a document embedded as a string value; parse twice or fix the producer |
| Chinese characters where accents belong | UTF-8 read as UTF-16 |

Double-encoded text is recoverable exactly once: re-encode to Latin-1 bytes and decode as UTF-8. Triple encoding usually is not, because the second pass introduces unmappable characters.

## Control Characters

- U+0000-U+001F must be escaped. Raw tabs and newlines inside a string value are the second-most-common parse failure after trailing commas, and they arrive when user-pasted text goes into a field unescaped by a hand-built document (Traps in SKILL.md).
- U+007F (DEL) and the C1 range U+0080-U+009F are legal unescaped, and are almost always corruption from a Windows-1252 source.
- Zero-width characters (U+200B ZWSP, U+FEFF used mid-string) survive parsing and break equality comparisons: two "identical" strings that fail `==` usually differ by one invisible character. Strip them at ingress for identifiers, keep them in free text.
- Bidi controls (U+202E and friends) can make a stored value display in a different order than it parses. Reject them in identifiers and anything rendered as code (`security.md`).

## Embedding JSON in Other Formats

| Target | Hazard | Fix |
|---|---|---|
| HTML `<script>` | `</script>` inside any string value closes the tag mid-document — an XSS vector, not a formatting bug | Escape `<`, `>`, `&` as `\u003c`, `\u003e`, `\u0026`; or use `<script type="application/json">` and parse the text content |
| JS source, legacy runtimes | U+2028 and U+2029 are valid in JSON strings; they were illegal in JS string literals before ES2019 | Escape both when generating JS source, always |
| HTML attribute | Quotes and `&` break the attribute | HTML-escape after JSON encoding, never before |
| URL query string | `+`, `&`, `#`, `/` change the URL's meaning | Percent-encode the whole document; base64url when it is long |
| Shell | Single quotes in the document break single-quoted shell strings | Heredoc with a quoted delimiter, or a file |
| CSV cell | Commas, quotes and newlines inside the document | Quote the cell and double the internal quotes; better, do not put documents in CSV (`csv`) |
| Another JSON document | Double-escaping, forever | A nested object, not a stringified one (`api-payloads.md`) |

## Content-Type and Charset

- `application/json` has **no charset parameter** — UTF-8 is implied by the media type. `application/json; charset=utf-8` is redundant but harmless; `charset=iso-8859-1` is a producer bug and a signal to check the bytes.
- NDJSON uses `application/x-ndjson`; JSON Patch uses `application/json-patch+json`; merge patch uses `application/merge-patch+json`; error bodies use `application/problem+json` (`patching.md`, `api-payloads.md`).
- A missing `Content-Type` makes most server frameworks skip body parsing and hand the handler an empty object — with no error (`debug.md`).
- Any `+json` suffix means "parse it as JSON with these extra semantics"; a client that matches on exact equality to `application/json` will reject valid responses.

## Normalization and String Identity

- Unicode has multiple encodings for the same visible text: `é` is one code point (NFC) or `e` + combining acute (NFD). They are different strings to every JSON parser and every database index.
- macOS filesystems hand you NFD filenames; most other sources produce NFC. A file list synced between two machines produces duplicate entries that look identical.
- **Normalize to NFC at ingress** for anything used as a key, an identifier, or a deduplication target; leave free text as received so it round-trips unchanged.
- JSON object keys are compared as sequences of code units, with no normalization and no case folding. A document can therefore hold two keys that render identically on screen — one NFC, one NFD — and every tool will report a two-key object while a human reviewer reports a duplicate.

## Line Endings

- Inside a JSON string, a line break must be `\n` or `\r\n` escaped as `\n`/`\r\n` — a literal one is a control character error.
- NDJSON is delimited by `\n`. A CRLF-written NDJSON file leaves a trailing `\r` on every record's last field, which parses fine and corrupts every value at the end of a line (`streaming.md`).
- The last line of an NDJSON file may or may not end with a newline. Consumers must handle both; producers should always write the trailing newline.
- A `.gitattributes` rule converting line endings on `*.json` will silently rewrite fixtures and break any signature over them (`signing.md`, `testing.md`).

**When a producer turns out to have an encoding quirk** — escaping everything, emitting a BOM, sending NFD, using CRLF in NDJSON — write the row in `## Producers` of `memory.md` with the workaround (`memory-template.md`). It is invisible in the parsed object and will be rediscovered otherwise.
