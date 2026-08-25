# Config — JSON as a Configuration File

JSON was designed for machine-to-machine data interchange, and configuration is a human-editing job. Everything awkward here follows from that mismatch.

**Contents:** [What JSON Costs as Config](#what-json-costs-as-config) · [JSONC and JSON5](#jsonc-and-json5) · [Which Files Are Actually Strict JSON](#which-files-are-actually-strict-json) · [Comments in Strict JSON](#comments-in-strict-json) · [package.json](#packagejson) · [tsconfig-Style Files](#tsconfig-style-files) · [Lockfiles](#lockfiles) · [Layering and Merge Semantics](#layering-and-merge-semantics) · [Validating Config at Startup](#validating-config-at-startup) · [Secrets in Config](#secrets-in-config)

## What JSON Costs as Config

| Missing | Consequence |
|---|---|
| Comments | The reason a setting exists lives in a commit message nobody reads |
| Trailing commas | Every reordering is a two-line diff and an occasional parse error |
| Multi-line strings | Scripts and templates become one line with `\n` escapes |
| References and interpolation | Repeated values, and no way to say "same as above" |
| Environment variable substitution | Either an invented `${VAR}` convention with a custom resolver, or duplication per environment |
| Any type beyond the six | Dates, durations and paths are strings with conventions the reader must know |

Choose JSON for config when the file is written by tools (lockfiles, generated manifests) or when an ecosystem mandates it. Choose the alternatives when humans edit it daily: `yaml` for nesting and comments, `toml` for flat-to-moderate configuration with unambiguous types. What matters is not repeating the mismatch: a hand-edited 600-line JSON config is a decision that gets re-litigated every quarter.

## JSONC and JSON5

Two different supersets, and tools support one or the other — never assume.

| Feature | JSONC | JSON5 |
|---|---|---|
| `//` and `/* */` comments | Yes | Yes |
| Trailing commas | Yes | Yes |
| Unquoted keys | No | Yes |
| Single-quoted strings | No | Yes |
| Multi-line strings (escaped newline) | No | Yes |
| Hex numbers, leading/trailing decimal point | No | Yes |
| `Infinity`, `NaN`, `+1` | No | Yes |
| Where you meet it | Editor settings, `tsconfig.json`, many .NET config files | Babel and build-tool configs, projects that opted in |

Neither is JSON. A JSONC file handed to a strict parser fails at the first comment, so any file that may be read by a foreign tool — CI scripts, other languages, a `jq` invocation — should stay strict. If comments are worth the incompatibility, say so in the file's own header comment.

## Which Files Are Actually Strict JSON

The distinction that causes real bugs:

- **Strict JSON, no comments**: `package.json`, `composer.json`, `*.lock`/lockfiles, most `manifest.json` files, anything read by a shell tool.
- **JSONC in practice**: `tsconfig.json` and `jsconfig.json`, VS Code's `settings.json`/`launch.json`/`tasks.json`, .NET `appsettings.json` in most hosts, `devcontainer.json`.
- **Depends on the reader**: `.eslintrc.json` and similar tool configs — the tool's own parser may be lenient while your CI's `jq` check is not.

Test the actual constraint rather than the folklore: run the file through a strict parser. If it fails and the tool still works, the tool is lenient — and your linting must match the tool, not the specification.

## Comments in Strict JSON

- The `"//"` key: `{"//": "why this exists", "port": 8080}`. It parses, and most tools ignore unknown keys. Two of them in the same object is a duplicate key, with undefined behavior (`security.md`) — number them (`"//1"`, `"//2"`) if there are several.
- `"$comment"` is a real JSON Schema keyword, ignored by validators, and the right choice inside schemas (`schema.md`).
- A leading-underscore convention (`"_note"`) is common and breaks any schema with `additionalProperties: false` unless the schema allows the pattern.
- The honest alternative: keep the explanation in a sibling `README` or in the schema's `description`, where it survives a tool that rewrites the file.

## package.json

- Strict JSON. npm and other tools **rewrite the file** on install: dependency blocks get sorted, formatting normalized. Hand-formatting and comment keys inside dependency blocks do not survive.
- Order inside `exports` is significant: condition matching takes the **first** match, so `"types"` must come before `"import"`/`"require"`, and `"default"` must be last. This is the one place in a JSON file where object key order is load-bearing, and it contradicts the general rule that objects are unordered.
- Version ranges are strings with their own grammar; a typo is a valid JSON string and an invalid range, caught only at install.
- `"engines"` is advisory unless enforced by configuration — declaring a Node range does not prevent installation by default.
- Adding a `$schema` key is harmless in most tools and gives editors completion and validation; check that the tool tolerates unknown top-level keys first.

## tsconfig-Style Files

- Comments and trailing commas are accepted by the TypeScript parser, which is why `tsconfig.json` looks like JSON and is not.
- `extends` resolves relative paths **relative to the file that declares them**, not to the final config; a path that works in the base file breaks when a child overrides part of it.
- Merge semantics of `extends` are shallow per top-level key: an overriding `compilerOptions` merges key by key, but an array (`include`, `paths`) is replaced entirely, not concatenated. The most common config surprise in the ecosystem.
- Other tools reading the same file (bundlers, test runners, `jq` in a CI script) may use a strict parser and fail on the comments. Keep a strict machine-readable copy if a shell script needs one.

## Lockfiles

- Never hand-edit. They are generated, and a manual edit produces a state no tool can reproduce.
- Merge conflicts are resolved by regenerating from the merged manifest, not by picking hunks. A hand-merged lockfile can install a combination that was never tested.
- They are the largest JSON files in most repositories and a poor place for review effort: review the manifest diff and the resulting dependency changes, not the lock's line diff.
- If review noise is intolerable, that is a tooling setting (sorted output, deterministic ordering), not a reason to stop committing the file.

## Layering and Merge Semantics

Almost every config system layers sources; the two decisions that must be written down:

1. **Precedence order.** The conventional one: built-in defaults < config file < environment-specific file < environment variables < command-line flags. Whatever you choose, put it in the documentation and in the error messages ("port=8080 from config.json, overridden by PORT=9000").
2. **How objects and arrays merge.** Objects deep-merge, arrays *replace* — that is the least surprising default, because concatenating arrays makes it impossible to remove an inherited entry. Say it explicitly; a user who expects concatenation and gets replacement loses their inherited list silently (`patching.md` for the same distinction).

Additional rules that prevent support tickets: a null in an override means "unset", not "set to null"; an unknown key is an error, not a warning (`languages.md`, strict for your own config); and the effective merged configuration should be printable with a flag, with secrets masked.

## Validating Config at Startup

- Validate against a schema **before** anything else initializes, and fail with the file path, the JSON Pointer to the offending value, and the expected type (`schema.md`).
- Add `"$schema": "https://…"` as the first key of the config file: editors that support it give completion and inline validation, which catches typos at the moment of editing rather than at the next deploy.
- Fail fast and completely: report every invalid key at once. A config that fails one key per restart cycle wastes a deploy per typo.
- Check invariants a schema cannot express (a port that is already bound, a directory that must exist, two settings that are mutually exclusive) immediately after validation, in the same error style.
- Log the effective configuration once at startup, with secrets masked. Half of all "the config is not being applied" reports are answered by that one line.

## Secrets in Config

- No credentials in a config file that is committed, backed up, or shipped in an image. The file holds a **reference** in the `<kind>:<locator>` scheme — `env:DB_PASSWORD`, `keychain:prod-db`, `ssm:/prod/db/password` — resolved at startup by the application.
- A `.env` file is not config: it is credentials, and it belongs outside version control with the same pointer discipline applied to anything written down (`memory-template.md`).
- Never write a secret into `~/Clawic/data/` when a config file is pasted for review — strip the value, keep the pointer, say so in one line (`security.md`).
- Config files often carry near-secrets that are safe and useful to keep: hostnames, ports, bucket names, account ids, profile names. Keeping them is what makes the file worth reading.

**When a config layout or merge policy is settled for a codebase**, write it as a row in `## Conventions` of `memory.md`; when it took a decision with alternatives, `~/Clawic/data/json/artifacts/<kebab-name>.md` with its `## Boxes` line (`memory-template.md`).
