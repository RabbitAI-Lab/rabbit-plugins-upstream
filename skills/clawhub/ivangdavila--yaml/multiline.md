# Multiline — Block Scalars, Folding, and Chomping

Everything that goes wrong with embedded scripts, certificates and long text is one of three decisions: literal or folded, how many trailing newlines, and where the block's left margin is. Each has an exact rule.

**Contents:** [Literal vs Folded](#literal-vs-folded) · [Chomping — the Trailing Newline](#chomping--the-trailing-newline) · [The Full Header Grammar](#the-full-header-grammar) · [Indentation Indicator](#indentation-indicator) · [How Folding Actually Works](#how-folding-actually-works) · [Multiline Without a Block Scalar](#multiline-without-a-block-scalar) · [Recipes](#recipes) · [Round-Trip Behavior](#round-trip-behavior)

**Before deriving a block-scalar header from scratch**, read `## Boxes` and `## Gotchas Hit` in `~/Clawic/data/yaml/memory.md` — a chain, a ConfigMap or a script whose header already took three tries is stored under `artifacts/`, and reusing it costs one read instead of three failed applies.

## Literal vs Folded

| | `\|` literal | `>` folded |
|---|---|---|
| Single newline between lines | kept | becomes a space |
| Blank line | kept as a newline | becomes one newline |
| More-indented line | kept verbatim | **kept verbatim, newlines preserved** |
| Correct for | scripts, PEM, SQL, embedded YAML/JSON, logs, anything a machine parses line by line | prose read by a human, long descriptions, commit-message bodies |

Decision test: *if two lines were joined by a space, would the value still be correct?* If no, it is `|`. A shell script, a certificate, and a multi-statement SQL block all fail that test — which is why `>` for a script is the single most common multiline bug.

## Chomping — the Trailing Newline

The indicator controls only what happens at the *end* of the block.

| Header | Name | Trailing newlines kept |
|---|---|---|
| `\|` or `>` | clip (default) | exactly one, regardless of how many blank lines follow |
| `\|-` or `>-` | strip | zero |
| `\|+` or `>+` | keep | all of them, exactly as written |

- A PEM certificate or private key needs `|` (clip): the format requires a final newline after `-----END …-----`, and `|-` produces a key that OpenSSL and most libraries reject.
- A single-line value that must have no newline — a token, a one-line command, a base64 blob split for readability — uses `|-` or `>-`.
- `+` is for content where the number of trailing blank lines is data. That is rare, and the blank lines are invisible in review, so justify it in a comment.
- Interaction with the emitter: a value already ending in `\n` re-emits as `|`; one that does not re-emits as `|-`. So the chomping indicator is not a style choice you can enforce on generated files — it is a fact about the value.

## The Full Header Grammar

`|` or `>`, then optionally an explicit indentation digit, then optionally a chomping indicator, then optionally a comment: `|2-  # keeps two-space margin, strips trailing newlines`. Order matters — `|-2` is invalid, `|2-` is not.

## Indentation Indicator

The block's indentation is normally taken from its **first non-empty line**. That breaks when the first line is itself indented relative to the rest, and the parser silently swallows the extra spaces as margin:

```yaml
script: |
    # this line sets the margin at 4
  echo "hi"        # ERROR: less indented than the margin
```

```yaml
script: |2
    indented line kept with 2 leading spaces
  normal line
```

- Use the digit when the content's first line starts with spaces and must keep them — YAML source embedded inside YAML, or a Python snippet whose first line is inside a block.
- The digit is relative to the *parent node's* indentation, not absolute. `|2` under a key indented 4 spaces means content at column 6.
- A leading blank line inside a block scalar is content, not margin: the margin comes from the first non-empty line, so an accidental empty first line does not shift anything, but a *deeper* first line does.
- Detection: the error `expected <block end>, but found ...` immediately after a block scalar almost always means the margin was set by a too-deep first line.

## How Folding Actually Works

For `>`, the exact rules, in order:

1. A single line break between two non-empty, equally-indented lines → one space.
2. `n` consecutive line breaks → `n-1` newlines. So one blank line gives exactly one `\n`.
3. A line that is **more indented than the block margin** keeps its own line breaks — before and after it. This is how a folded block can contain a code snippet, and also why a folded description with a stray indented line comes out with unexpected newlines.
4. Trailing whitespace on a folded line is stripped before folding.

Worked example:

```yaml
text: >
  a
  b

  c
    d
  e
```

→ `"a b\nc\n  d\ne\n"`. Line `d` is more indented so it and its neighbors keep their breaks; the blank line before `c` produced one newline; `a b` folded to a space; clip left one final newline.

## Multiline Without a Block Scalar

- **Plain scalar continuation**: a plain value continued on more-indented following lines folds to spaces. Legal, works, and unreadable in review — every reader has to check the indentation to know whether the next line is a value or a sibling key.
- **Quoted continuation**: inside double quotes, a line break folds to a space, and a trailing `\` suppresses even the space (`"long\` newline `  text"` → `longtext`). Inside single quotes, breaks fold to spaces with no escape available.
- **Flow sequences over lines**: `[a,` newline `  b]` is legal. It is also the fastest way to produce `could not find expected ':'` when someone deletes the closing bracket.

Use a block scalar for anything over two lines. The others exist; they are not the answer.

## Recipes

| Content | Header | Note |
|---|---|---|
| Shell script | `\|` | Add `set -euo pipefail` as the first content line; keep the trailing newline |
| PEM certificate or key | `\|` | Clip, not strip. Never write the value into a memory file — pointer only (`security.md`) |
| SQL | `\|` | `--` comments are safe inside a block; outside one they are not comments to YAML anyway |
| Long English description | `>-` | Fold to one paragraph, no trailing newline |
| Embedded YAML (a ConfigMap holding a config file) | `\|` | The inner document's indentation is content; a 1.2 parser will not touch it |
| Embedded JSON, pretty-printed | `\|` | Or one line, single-quoted, if the consumer wants a string |
| Multi-line command with continuations | `\|` | Backslash continuations inside the block are the shell's, not YAML's |
| Windows batch / CRLF-sensitive text | `\|` | Enforce LF in `.gitattributes`; a stray `\r` ends up inside the value (`strings.md`) |
| Text with meaningful trailing blank lines | `\|+` | Comment why, or the next editor deletes them |

## Round-Trip Behavior

- Most emitters do not reproduce block scalars: a loaded-then-dumped script comes back as a double-quoted string full of `\n`. Semantically identical, unreadable, and the diff is the whole file. `ruamel.yaml` in round-trip mode preserves the style; `yq` preserves it in place; PyYAML and go-yaml do not (`editing.md`).
- To force literal style when generating with PyYAML, register a representer for `str` that emits `style='|'` when the value contains `\n` — otherwise long scripts arrive as one escaped line.
- A block scalar whose content lines exceed the emitter width are **not** wrapped (literal blocks are never re-folded), which makes `|` the safe choice for anything long that must survive regeneration byte for byte.

**When a block-scalar layout finally works for something non-obvious** — a certificate chain, embedded YAML inside a ConfigMap, a script whose indentation kept shifting — save the shape, not the payload, to `~/Clawic/data/yaml/artifacts/<kebab-name>.md`, with every secret replaced by its pointer, and add its `## Boxes` line to `memory.md` in the same turn (`memory-template.md`). Deriving the right header takes two or three failed applies; nobody should pay that twice.
