# Types — What an Unquoted Scalar Becomes

YAML has no declared types. Every unquoted scalar is matched against a list of regexes (the *resolver*) and becomes whatever matches first. Two parsers with different resolvers read the same bytes as different values, and neither reports anything. This file is the resolver, per version, plus the reverse operation: forcing the type you meant.

**Contents:** [The Two Schemas](#the-two-schemas) · [Booleans and the Norway Problem](#booleans-and-the-norway-problem) · [Numbers That Are Not Numbers](#numbers-that-are-not-numbers) · [Octal and File Modes](#octal-and-file-modes) · [Sexagesimal](#sexagesimal) · [Null, Empty, and Absent](#null-empty-and-absent) · [Dates and Timestamps](#dates-and-timestamps) · [Forcing a Type With a Tag](#forcing-a-type-with-a-tag) · [Keys Have Types Too](#keys-have-types-too) · [Auditing a File for Coercion Bugs](#auditing-a-file-for-coercion-bugs)

**Before changing types in a file that already exists**, read `## Config Files` and `## Gotchas Hit` in `~/Clawic/data/yaml/memory.md` — which parser reads that file, and whether this exact coercion has already bitten here, are both recorded there.

## The Two Schemas

| | YAML 1.1 (2005) | YAML 1.2 core (2009, revised 2021) |
|---|---|---|
| Bools | `y n yes no on off true false`, any case | `true false` and case variants only |
| Octal | `0644` → 420 | `0o644` → 420; `0644` → 644 decimal |
| Sexagesimal | `1:30` → 90 | plain string |
| Timestamps | ISO dates → date/datetime objects | plain string |
| Merge key `<<` | part of the type library | not in the core schema |
| Speakers | PyYAML, Ruby Psych, SnakeYAML 1.x, go-yaml v2 | js-yaml v4, SnakeYAML Engine, ruamel in 1.2 mode |

go-yaml v3 and ruamel sit in between: they follow 1.2 for most resolution but keep `yes/no/on/off` or merge keys for compatibility. Never reason from "the spec"; reason from the library in `## Toolchain` (`parsers.md`).

The `%YAML 1.2` directive at the top of a document declares the version, but a 1.1-only parser ignores or rejects it. It documents intent; it does not change PyYAML's behavior.

## Booleans and the Norway Problem

`country: NO` is `false` in every 1.1 parser. `SE`, `FR` and every other code stay strings — which is worse than if all of them broke, because the failure is selective: a country list works for 200 rows and breaks on Norway.

- The 1.1 type library lists `y` and `n` as bools; PyYAML's resolver deliberately omits them, js-yaml never had them. Do not rely on either behavior — a single-letter value gets quoted.
- Truthiness leaks into *keys*, not just values: `on:` becomes the key `True` in a 1.1 parser (`pipelines.md`).
- The reverse trap: a config expecting a string gets `true` and stringifies it as `"True"` in Python, `"true"` in Go. Case-sensitive comparisons downstream then fail on one platform only.
- Fix is always the same: `"no"`, `"on"`, `"y"`. Quoting a real boolean by accident is caught by the schema; not quoting a string is not.

## Numbers That Are Not Numbers

| Value | Resolves as | What breaks |
|---|---|---|
| `1.0` | float | The trailing zero is not data: go-yaml and JS emitters re-emit it as `1` (PyYAML and Psych keep `1.0`), so a version pin round-tripped through kubectl or `yq` becomes a different version |
| `1.10` | float 1.1 | `1.10` and `1.1` become the same value |
| `1.2.3` | string | Nothing — two dots is not a float; still quote it for consistency with siblings |
| `007` | 7 (1.2) / 7 (1.1, no `8`/`9` so not octal-invalid) | Leading zeros lost — employee ids, order numbers |
| `+12` | int 12 | The sign is gone from a string that needed it |
| `12e3` | string in 1.1 (the float regex demands a dot *and* a signed exponent: `0.5e+3` is 500.0, `0.5e3` and `12e+3` are strings); float 12000 in 1.2 core | Same file, two types: a product code `4e5` stays a string in PyYAML and becomes 400000 in js-yaml |
| `0x1F` | int 31 | Hex-shaped ids and colors — `0xFF` as a color code becomes 255 |
| `1_000` | int 1000 in 1.1 (underscores allowed) | A string with underscores is silently a number |
| `.5` | float 0.5 in 1.1 | Rare, but a leading-dot code becomes a number |
| `Infinity` | string | Not a special float — only `.inf` is |

Rule of thumb with a test: **if two different-looking values must never compare equal, it is an identity, and identities are quoted.** `1.10` vs `1.1`, `007` vs `7`, `+1` vs `1` all collapse if left unquoted.

## Octal and File Modes

`mode: 0644` in a 1.1 parser is the integer **420** (6×64 + 4×8 + 4). Kubernetes `defaultMode`, `fileMode` in Ansible, and permissions in cloud-init all take this form, and 420 is a legal mode, so nothing errors — the file just gets the wrong bits.

- YAML 1.2 reads `0644` as decimal 644, which is *also* a legal-looking mode and also wrong.
- Correct forms: `"0644"` when the consumer wants a string (Kubernetes `defaultMode` wants an int — use `0644` deliberately on a 1.1 parser, or `420` written explicitly with a comment), `0o644` when the consumer parses 1.2.
- Ansible is explicit about this: `mode: "0644"` quoted, or `mode: u=rw,g=r,o=r` symbolic. Unquoted `0644` there is a documented footgun.
- Audit grep: any value matching `^0[0-7]{3}$` in a manifest is either a mode or a padded id, and both need a decision.

## Sexagesimal

Base-60 numbers are a YAML 1.1 feature that exists to write durations: `190:20:30` is 685230.

- Formula: `a:b` → `a×60 + b`; `a:b:c` → `a×3600 + b×60 + c`. So `22:22` → 1342 and `1:30:00` → 5400, but `08:00` stays the string `08:00`.
- Two sub-rules decide it: the first group must have no leading zero, and every later group must be `[0-5]?[0-9]`. That is why `22:22` coerces and `08:00` does not — the difference is one leading zero, in the same parser. Do not learn the sub-rules, quote both.
- Where it bites: Compose `ports: - 22:22` (short syntax, unquoted), `HH:MM` window settings, and the MAC addresses that happen to fit: `de:ad:be:ef:00:01` survives (hex letters never match), `00:11:22:33:44:55` survives (leading zero), but `12:34:56:12:34:56` becomes the integer 9783981296. A quoting rule that depends on which MAC you were handed is not a rule.
- Always: `"22:22"`, `ports: - "8080:80"`.

## Null, Empty, and Absent

Three different states that YAML makes easy to confuse:

| Written | Loads as | Means to most consumers |
|---|---|---|
| `key: value` | the value | set |
| `key: ""` | empty string | set, empty |
| `key:` | `null` | present but null |
| `key: null` / `key: ~` / `key: Null` | `null` | present but null |
| key omitted | absent | fall back to the default |

- `key:` and key-omitted are **not** the same thing: a null explicitly overrides a default in most merge implementations, while an absent key inherits it. This is the number one bug in environment overlays (`config-design.md`).
- An empty list is `[]` and an empty map is `{}`. Writing the key with nothing under it gives `null`, not an empty collection — so `resources:` in a Kubernetes manifest is not "no resources", it is a null the API may reject.
- Commenting out the only item of a list leaves `null` behind, not an empty list.
- `NULL`, `Null`, `null`, `~` all resolve; `nil`, `none`, `None` do not (they are strings) — which surprises Ruby and Python authors in opposite directions.

## Dates and Timestamps

1.1 resolvers turn `2026-07-26` into a date object and `2026-07-26T10:00:00Z` into a datetime. Consequences:

- The value re-emits in the emitter's format, not yours: `2026-07-26` may come back as `2026-07-26 00:00:00`.
- A comparison against the string `"2026-07-26"` fails, in a codebase where every other config value is a string.
- Timezone-naive datetimes acquire the loader's assumptions; PyYAML returns naive datetimes for values with no offset.
- Anything that is a *label* (a release date in a tag, a version-dated key) gets quoted. Anything that is genuinely a moment and whose consumer wants a date object stays unquoted — and gets a comment saying so.

## Forcing a Type With a Tag

Quoting forces a string. For the other direction, use the standard tags — they work in every parser because they are part of the failsafe/JSON schemas:

- `!!str 42`, `!!int "42"`, `!!float 1`, `!!bool "yes"`, `!!null ""`
- `!!set { a, b }` and `!!binary` (base64 payload) exist in 1.1 and are supported unevenly — check before using.
- Local tags (`!Ref`, `!secret`, `!include`) are tool extensions, not YAML: a generic parser raises `could not determine a constructor` (`dialects.md`).
- A tag on a value the schema rejects is still a schema error — tags change parsing, not validation.

## Keys Have Types Too

- `2026: value` is an int key; `"2026": value` is a string key. A JSON consumer sees `"2026"` either way, but a Python or Go consumer sees `2026` and a lookup by string fails.
- `yes: value` is the key `True`. `null: value` is the key `None`. Both are legal and both look normal in the file.
- Duplicate keys after resolution: `1` and `1.0` and `"1"` may collide or not depending on the language's dict semantics — a mapping with mixed-type keys is a bug waiting for a language change (`errors.md`).
- Keys longer than 1024 characters, or spanning lines, need the explicit form `? <key>` newline `: <value>`. Rare, and the error message when you hit the limit does not mention the limit.

## Auditing a File for Coercion Bugs

Fastest reliable pass, in order:

1. Load with the target parser, dump with `sort_keys=False`, diff against the original. Every changed token is a coercion.
2. Grep for the shapes: `: (y|n|yes|no|on|off|true|false)\s*$` case-insensitive, `: 0[0-9]`, `: [0-9]+:[0-9]`, `: [0-9]+\.[0-9]+\s*$`, `: [0-9]{4}-[0-9]{2}-[0-9]{2}`.
3. Turn on yamllint's `truthy` rule with `check-keys: true` — it catches `on:` and every bool-in-disguise the resolver would take (`schemas.md`).
4. Add the type constraints to the schema so the next occurrence fails in CI instead of at runtime.

**After a coercion trap actually bites**, write it to `## Gotchas Hit` in `~/Clawic/data/yaml/memory.md` — the value, the file, the parser, and the fix — and if the parser or spec version was the discovery, add or update its row in `## Toolchain` (`memory-template.md`). This is the class of bug that recurs in the same repo every few months; the log is what makes the second occurrence a ten-second fix. When a quoting or spec preference comes out of it, that is a declaration: it goes to `config.yaml`, not to memory.
