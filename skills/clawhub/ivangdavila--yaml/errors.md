# Errors — From Message to Cause

YAML errors point at where the parser gave up, which is often lines below where the mistake is. The message's *class* is more informative than its text: scanner errors are about characters, parser errors about structure, composer errors about anchors, constructor errors about types, and everything else is the consumer's schema, not YAML.

**Contents:** [The Four Error Classes](#the-four-error-classes) · [Message Index](#message-index) · [The Bisect Procedure](#the-bisect-procedure) · [Errors That Are Not Reported](#errors-that-are-not-reported) · [Duplicate Keys](#duplicate-keys) · [Reading a Parser's Error Format](#reading-a-parsers-error-format) · [When the File Is Generated](#when-the-file-is-generated)

**Before diagnosing from the message alone**, read `## Gotchas Hit` and `## Toolchain` in `~/Clawic/data/yaml/memory.md` — grep the verbatim error text there first, because this class of failure recurs in the same repo, and the `## Toolchain` row says whether this library reports the line of the mistake or the line where it gave up.

## The Four Error Classes

| Class | Emitted by | Means | Look at |
|---|---|---|---|
| Scanner | tokenizer | An illegal character: tab in indentation, control char, bad encoding | The exact column, with whitespace visible |
| Parser | grammar | Structure does not close: indentation, unclosed flow collection, a second `: ` on one line | The lines *above* the reported line |
| Composer | node graph | Alias without anchor, duplicate anchor issues | The whole file — anchors are file-scoped |
| Constructor | type resolution | A tag with no constructor, an unrepresentable value | The tag, and which parser is running |
| (not YAML) | the consumer | `cannot unmarshal`, `additionalProperties`, `required` | The schema — the YAML parsed fine (`schemas.md`) |

## Message Index

| Message (any parser, wording varies) | Cause | Fix |
|---|---|---|
| `found character '\t' that cannot start any token` | Tab used as indentation | Spaces only; show whitespace in the editor |
| `found a tab character where an indentation space is expected` | Same, SnakeYAML wording | Same |
| `mapping values are not allowed in this context` | A `: ` inside an unquoted value, or a key indented under a scalar | Quote the value (`strings.md`) |
| `did not find expected key` | A line's indentation matches no open block — usually one space off | Compare leading spaces with the sibling above |
| `did not find expected '-' indicator` | A sequence item at the wrong indentation, or a mapping key where an item was expected | Check `sequence_indent` consistency |
| `expected <block end>, but found '<scalar>'` | Extra indentation opened an implicit block that never closes; also the signature of a block scalar whose first line set a too-deep margin (`multiline.md`) | Look at the block scalar or the over-indented line above |
| `could not find expected ':'` | Unclosed `{` or `[` — very often an unquoted `{{ template }}` | Quote templated values (`dialects.md`) |
| `while parsing a flow node ... expected the node content` | A `,` with nothing after it, or a trailing comma | YAML has no trailing commas |
| `found unexpected end of stream` | Unterminated quote or unclosed flow collection at EOF | Search for an odd number of quotes on one line |
| `found undefined alias 'x'` | Alias before its anchor, or in another file/document | Anchors are per document (`anchors.md`) |
| `found duplicate anchor 'x'` | Same anchor name defined twice where the parser is strict | Rename; the redefinition silently shadows elsewhere |
| `duplicated mapping key` / `key "x" already set` | Two identical keys | Below |
| `could not determine a constructor for the tag '!Ref'` | Tool-local tag, generic parser | Use the tool's own parser or register the constructor (`dialects.md`) |
| `unacceptable character #x0000: control characters are not allowed` | UTF-16 read as UTF-8, stray NUL, or a BOM mid-stream | Check the encoding (`strings.md`) |
| `special characters are not allowed` | Non-breaking space or zero-width character, usually pasted | `grep -nP '[^\x00-\x7F]'` |
| `yaml.constructor.ConstructorError: could not determine a constructor for '!!python/object'` | Full-tag content hitting a safe loader — **this is the loader working** | Do not switch to an unsafe loader (`security.md`) |
| `The merge key is not allowed here` / `<<` treated as a literal key | 1.2-strict parser or a validator that does not implement merge | `anchors.md` |
| `line too long` / `wrong indentation` from yamllint | Lint rule, not a parse error | Configure the rule or fix the style (`schemas.md`) |
| Anything else | Class it with the table above, then bisect | Below |

## The Bisect Procedure

For a file whose error line makes no sense — the fastest reliable method, ~5 rounds for a 1,000-line file:

1. Copy the file. Delete the bottom half. Re-parse.
2. Still failing → the error is in the top half; repeat on it. Parses fine → the error is in the deleted half; restore it and delete the *other* quarter.
3. Stop when you are down to a block of ten lines. Deleting a nested block can create a new error (an orphaned key); if the new error is different, you have gone too far — restore and halve the other side.
4. If nothing localizes it, the file is fine and the consumer is failing: dump the parsed tree (`editing.md`) and compare it against the schema.

`yamllint -f parsable file.yaml` reports *all* problems in one pass instead of stopping at the first, which often beats bisecting.

## Errors That Are Not Reported

The dangerous half of this domain. Nothing raises for any of these:

| Silent failure | How to detect |
|---|---|
| A value coerced to bool/int/date | Load and print types; grep the shapes (`types.md`) |
| Duplicate keys where last-wins is the parser's default | Lint rule `key-duplicates` |
| A key indented under the wrong parent | Dump the parsed tree and read it, once |
| A key the consumer ignores (typo, wrong case, deprecated) | Schema validation with `additionalProperties: false` (`schemas.md`) |
| `key:` with nothing after it overriding a default with `null` | Compare merged config against defaults (`config-design.md`) |
| An anchor redefined later in the file | Search for `&name` twice |
| Trailing whitespace preserved inside a literal block | `cat -A`, or a checksum comparison |
| `>` folding a script into one line | Print the value with `repr`, not `print` |
| A CRLF ending inside a block scalar | `file` reports CRLF; `cat -A` shows `^M$` |

The general defense is Rule 10: run the file through the consumer's own validator, and once through a load-and-dump diff.

## Duplicate Keys

| Parser | Default behavior |
|---|---|
| PyYAML | Last wins, silently |
| ruamel round-trip | Error |
| go-yaml v3 | Error (`already defined at line N`) |
| go-yaml v2 | Last wins |
| js-yaml | Error (`duplicated mapping key`) |
| SnakeYAML | Error by default in recent versions; configurable |
| Ruby Psych | Last wins |

Consequences: the same file can *work* on the CI runner and *fail* on a developer's machine because of the library version alone. Treat any duplicate key as a defect, and check which occurrence is currently live before deleting one — deleting the winning copy changes behavior.

Common source: two `env:` or two `volumes:` blocks in a manifest edited by two people, or a merge conflict resolved by keeping both sides.

## Reading a Parser's Error Format

- **PyYAML**: two contexts — `while parsing a block mapping ... in "file", line 4` (where the structure started) and `expected <block end> ... line 12` (where it broke). The **first** line number is the useful one.
- **go-yaml**: `yaml: line N: <message>`, and N is 0-indexed in some wrappers — check line N and N+1.
- **js-yaml**: prints a code snippet with a caret. Trustworthy column, sometimes a late line.
- **SnakeYAML**: gives the problem mark and the context mark, same pattern as PyYAML.
- **kubectl**: `error converting YAML to JSON: yaml: line N` means the YAML failed; `error validating data` means the YAML parsed and the schema rejected it. Two completely different investigations (`kubernetes.md`).

## When the File Is Generated

If the broken YAML came out of a template (Helm, Jinja, envsubst, a CI expression), the YAML is a symptom:

1. Render first, then parse the render — never debug the template as if it were YAML (`helm template`, `ansible-playbook --list-tasks`, `docker compose config`).
2. Indentation bugs dominate: a template inserting a block at the wrong depth. In Helm that is `nindent` vs `indent` (`kubernetes.md`).
3. Quoting bugs are second: a rendered value that starts with `{`, `*`, `!` or is `yes`/`no` breaks the document *after* substitution. Wrap the substitution in `quote`/`| to_json`/explicit quotes at the template level.
4. A rendered empty value leaves `key:` → `null`, which the schema may reject with a message about types.

**After diagnosing a non-obvious parse failure**, write one row to `## Gotchas Hit` in `~/Clawic/data/yaml/memory.md`: the message, the real cause, the file, and the fix (`memory-template.md`). Error text is what people search for six months later, so keep the message verbatim. If the diagnosis turned on a library's behavior — a duplicate-key policy, a wrapper's off-by-one line numbers — that belongs in `## Toolchain` instead.
