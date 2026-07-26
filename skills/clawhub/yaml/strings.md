# Strings — Quoting, Escapes, and Invisible Characters

Three scalar styles, three different escape universes. Choosing wrong produces either a parse error (loud, cheap) or a string that lost a character (silent, expensive). Multiline content has its own rules in `multiline.md`; what a scalar *resolves to* is `types.md`.

**Contents:** [The Three Styles](#the-three-styles) · [When a Plain Scalar Is Illegal](#when-a-plain-scalar-is-illegal) · [Single vs Double Quotes](#single-vs-double-quotes) · [Escape Sequences](#escape-sequences) · [Characters That Need a Decision](#characters-that-need-a-decision) · [Whitespace](#whitespace) · [Encoding, BOM, Line Endings](#encoding-bom-line-endings) · [Embedding Other Languages](#embedding-other-languages) · [Comments](#comments) · [Keys and Long Strings](#keys-and-long-strings)

**Before quoting anything in a file that already exists**, read `quote_style` in `~/Clawic/data/yaml/config.yaml` and `## Repo Style` in `~/Clawic/data/yaml/memory.md` — a declared style wins, an observed one is matched, and either beats re-quoting a repo into a whole-file diff.

## The Three Styles

| Style | Written | Escapes available | Use for |
|---|---|---|---|
| Plain | `value` | none — the character set *is* the escape mechanism | Values that are unambiguous and stay that way |
| Single-quoted | `'value'` | `''` for a literal `'`, nothing else | Anything containing backslashes: regexes, Windows paths, `\n` you want literal |
| Double-quoted | `"value"` | full C-style set plus `\u`/`\x` | Anything needing a real control character or a non-typeable codepoint |

Default to plain, quote when Rule 1 or the list below demands it, and reach for double quotes only when an escape is actually needed. A file that mixes all three arbitrarily is a review burden; `quote_style` settles it.

## When a Plain Scalar Is Illegal

A plain scalar cannot:

- **start** with any indicator: `- ? : , [ ] { } # & * ! | > ' " % @ \``  — this is why `*` for a wildcard, `@latest` for a version, and `!Ref` all need quotes
- contain `: ` (colon followed by space) — it would open a mapping
- contain ` #` (space then hash) — it would open a comment
- start with `- ` — it would open a sequence item
- end with `:` — `key: value:` is a parse error, `key: "value:"` is not
- span lines with meaningful indentation (multiline plain scalars fold to spaces, which is almost never what was wanted)

Inside flow collections (`[ ]`, `{ }`) a plain scalar additionally cannot contain `,` `[` `]` `{` `}`. And the colon rule tightens: `{a:1}` is the single scalar `a:1`, not a pair — the pair needs the space, `{a: 1}`. Quote inside flow style whenever the value contains punctuation at all; the failure there is a shape change, not an error.

## Single vs Double Quotes

- `'C:\Users\dev'` is exactly that. `"C:\Users\dev"` is a parse error or a mangled string, because `\U` starts a 32-bit escape.
- `'It''s here'` → `It's here`. There is no backslash escaping inside single quotes at all.
- `"line1\nline2"` gives a real newline; `'line1\nline2'` gives a backslash and an `n`.
- A regex almost always wants single quotes: `'^\d{3}-\d{4}$'`.
- A double-quoted string is also the only style that can express a character your editor cannot type: `"\u00a0"` for a non-breaking space, `"\u200b"` for a zero-width space.

## Escape Sequences

Valid inside double quotes only: `\0 \a \b \t \n \v \f \r \e \" \\ \N \_ \L \P \x41 \u00e9 \U0001F600`, plus `\ ` (escaped space) and a backslash at end of line to join lines without a space.

- `\e` (escape, 0x1B) and `\0` are YAML-specific extensions to the C set — they work, and a JSON consumer of the same value will not have produced them.
- `\/` is *not* a YAML escape even though it is valid JSON. `"a\/b"` is an error in strict parsers.
- Unicode escapes are resolved at parse time: the file contains `\u00e9`, the value contains `é`, and re-emitting writes the literal character unless the emitter is configured with `allow_unicode: false`.

## Characters That Need a Decision

| Character in a value | Plain scalar behavior | Do |
|---|---|---|
| `:` not followed by space (`http://x`, `12:30`) | Legal plain scalar, but 1.1 may read digits as sexagesimal (`types.md`) | URLs fine unquoted; digit pairs quoted |
| `: ` | Splits into a mapping | Quote |
| `#` after a space | Comment starts | Quote |
| `#` inside a word (`ab#cd`) | Legal, no comment | Leave |
| Leading/trailing space | Stripped | Quote to preserve |
| `%` at line start | Directive indicator | Quote |
| `@` and `` ` `` at start | Reserved indicators, error in strict parsers | Quote |
| `*` or `&` at start | Alias / anchor | Quote |
| `!` at start | Tag | Quote |
| `{` or `[` at start | Flow collection — the classic `{{ template }}` break | Quote (`dialects.md`) |
| `-` at start followed by non-space (`-abc`) | Legal plain scalar | Leave; `- abc` is a list item |
| Emoji, CJK, accents | Legal in UTF-8 | Leave; ensure the file is UTF-8 |

## Whitespace

- Trailing spaces on a line are stripped in plain and folded scalars, **preserved inside a literal block** — which is how a copy-pasted certificate keeps invisible trailing spaces until an editor's "trim on save" silently changes the value.
- A line with only spaces inside a block scalar counts as an empty line, not as content.
- Leading spaces inside a quoted scalar survive: `key: "  padded"` keeps both spaces. Plain `key:   padded` does not.
- Non-breaking space (U+00A0) is *not* whitespace to the parser: it is part of the scalar, and as indentation it produces `found character that cannot start any token` while looking identical to a space. Pasting from a browser or a chat client is the usual source.
- Zero-width characters (U+200B, U+FEFF mid-file) do the same thing and are worse, because the error points at a column that looks empty.

Detection: `grep -nP '[^\x00-\x7F]' file.yaml` lists every non-ASCII byte with its line; `cat -A` shows tabs as `^I` and line ends as `$`.

## Encoding, BOM, Line Endings

- UTF-8 is the only encoding to use. YAML 1.2 also permits UTF-16 with a BOM; several parsers do not implement it, and the error is unhelpful.
- A UTF-8 BOM at the very start of the stream is allowed by the spec and rejected by some tools (and by shells reading `#cloud-config` or shebang-style first lines). Strip it: `sed -i '1s/^\xEF\xBB\xBF//'`.
- CRLF: parsers accept `\r\n` as a line break, but `\r` at the end of a *scalar* inside a literal block becomes part of the value. A shell script embedded with CRLF then fails with `bad interpreter: ^M`. Enforce LF with `.gitattributes` (`* text=auto eol=lf`) for YAML.
- Control characters other than tab, LF and CR are illegal outside quotes and produce `control characters are not allowed`.

## Embedding Other Languages

| Embedded | Best style | Why |
|---|---|---|
| Shell script | `\|` literal block | Newlines are data, `#` comments survive, no escaping needed |
| JSON | single quotes on one line, or `\|` block | JSON is valid YAML, so an unquoted JSON object parses as a YAML flow map — usually fine, but it stops being a *string* |
| Regex | single quotes | Backslashes are literal |
| SQL | `\|` literal block | Preserves formatting and lets `--` comments live |
| Windows path | single quotes | Backslashes |
| Template expression (`{{ }}`, `${{ }}`) | double or single quotes | `{` starts a flow map (`dialects.md`) |
| Base64 blob | plain, or `\|` if wrapped | No special characters except `=` and `/`, both safe |
| PEM certificate/key | `\|` literal, keep trailing newline | `multiline.md`, and never store the value in a memory file |

Embedded JSON is the case people get wrong twice: `config: {"a": 1}` gives a *map*, and `config: '{"a": 1}'` gives a *string* the app will parse itself. Decide which one the consumer wants before choosing.

## Comments

- A `#` starts a comment only at the start of a line or **after whitespace**. `key: value#notacomment` has no comment — the value is `value#notacomment`. `key: value #comment` does.
- There is no block-comment syntax. Every line needs its own `#`; editors that "comment the selection" are doing exactly that.
- **Inside a block scalar there are no comments** — a `#` line is content. A comment cannot be attached to a line of an embedded script from the outside; put it inside the script with the script's own comment syntax (`multiline.md`).
- A comment after a block scalar's header is legal (`script: | # runs on boot`), a comment line between the header and the content is not.
- Comments are attached to nothing: every loader that is not a round-trip loader discards them at parse time, so a comment is documentation for the *file*, never metadata a program can read (`editing.md`).
- Consequence for generated files: put the generator's warning header in the file's first line and expect the tool that rewrites the file to drop it — the only durable warning is a filename (`*.generated.yaml`) or a CI check.

## Keys and Long Strings

- A simple key must be a single line and at most 1024 characters. Past that, the explicit form: `? <long key>` on one line, `: <value>` on the next.
- Long values should not be broken by hand — a plain scalar continued on the next line folds to a single space, which usually works and produces a diff nobody can review. Use a `>` folded block deliberately (`multiline.md`) or set the emitter width (`max_line_width`).
- URLs and tokens containing no spaces cannot be folded by the emitter at all, so they will exceed any line-length lint rule. Configure `line-length` to warn rather than error, or add an inline `# yamllint disable-line rule:line-length`.

**When quoting style is settled for a repo** — the user says "we quote everything", "single quotes here", "keep it minimal" — that is a declaration: write `quote_style` (and `max_line_width` if line breaking came up) to `~/Clawic/data/yaml/config.yaml`, key by key, leaving every other key untouched. What you merely *observed* in an existing repo instead goes to `## Repo Style` in `~/Clawic/data/yaml/memory.md`, so the two never get confused (`memory-template.md`).
