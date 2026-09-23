# Config Design — Shaping the File Itself

The traps in the rest of this skill are about syntax. This one is about the decisions that make a config file survive three years and four maintainers: how it layers, what a missing key means, where lists go wrong, and what should not be in YAML at all.

**Contents:** [Layering](#layering) · [Merge Semantics Are the Contract](#merge-semantics-are-the-contract) · [Lists Are the Weak Point](#lists-are-the-weak-point) · [Null, Absent, and Defaults](#null-absent-and-defaults) · [Naming and Shape](#naming-and-shape) · [What Does Not Belong in the File](#what-does-not-belong-in-the-file) · [Environment Interpolation](#environment-interpolation) · [Splitting Files](#splitting-files) · [Evolving the Format](#evolving-the-format) · [When YAML Is the Wrong Choice](#when-yaml-is-the-wrong-choice)

**Before designing a new file for an existing system**, read `## Config Files` in `~/Clawic/data/yaml/memory.md` — the conventions already in play, and which loader merges them, decide most of what follows.

## Layering

The standard stack, lowest precedence first:

1. Defaults in code — the only complete, always-present layer
2. A committed base file (`config.yaml`)
3. An environment overlay (`config.prod.yaml`)
4. A local, gitignored file (`config.local.yaml`)
5. Environment variables
6. Command-line flags

Rules that keep it debuggable:

- **Defaults live in code, not in a `defaults.yaml`.** A default file can be missing or stale; code cannot. The base file then contains only what differs from the default, and reading it tells you what this deployment actually changed.
- **Every layer has the same shape.** An overlay with a different structure cannot be merged mechanically, and diffing base against overlay stops being meaningful.
- **Print the merged result.** Any config system past two layers ships a `--show-config`/`config dump` command, or people debug by guessing. `docker compose config` and `helm template` exist for this reason.
- Keep the number of layers to what is used. Four layers "for flexibility" is four places to look during an incident.

## Merge Semantics Are the Contract

Pick one and document it at the top of the base file:

| Semantics | Maps | Lists | `null` in overlay |
|---|---|---|---|
| Replace | replaced | replaced | sets null |
| Deep merge (most common) | recursive | **replaced** | sets null |
| Deep merge + append | recursive | concatenated | sets null |
| Delete-aware | recursive | replaced | **deletes the key** |

- The single most common surprise is list replacement under deep merge: an overlay adding one item to `plugins` removes the rest (`editing.md`).
- Deletion is rarely supported. Where it matters, either use a delete-aware merger (Helm) or design the key to accept an explicit `enabled: false` instead of relying on removal.
- Precedence must be *total and stated*: for every pair of layers, one wins, always. "It depends on the key" is how a config becomes unmaintainable.

## Lists Are the Weak Point

Three shapes, and the choice is architectural:

```yaml
# A. Plain list — cannot be overridden per item
plugins: [auth, cache, metrics]

# B. List of maps with a name key — overridable by a strategic merger only
plugins:
  - name: auth
    enabled: true

# C. Map keyed by name — overridable by every merger, and diffs cleanly
plugins:
  auth: {enabled: true}
  cache: {enabled: false, ttl: 300}
```

- **Shape C for anything an overlay must modify.** Deep merge handles it natively, a single key can be changed without restating the collection, and duplicates become impossible (two entries with the same name is a duplicate-key error rather than a silent double).
- Shape A is right when order is meaningful and the whole list is always specified: middleware chains, a search path.
- Shape B is the Kubernetes convention and only works because Kubernetes has strategic merge patch. Copying it into a system whose merger replaces lists gives the worst of both.
- Order-sensitivity should be explicit: if order matters, say so in a comment, because maps in shape C have no guaranteed order after a round trip.

## Null, Absent, and Defaults

- `key: null` means "explicitly nothing"; an omitted key means "use the default". Most mergers treat them differently and most users do not know that (`types.md`).
- Design so that *absent* is always the safe state. A required key with no default should fail loudly at load, not produce a `None` that surfaces 200 lines later.
- Booleans default to `false` unless there is a strong reason; a feature that turns itself on when the key is missing is a support ticket.
- Empty collections: `[]` and `{}` mean "explicitly none". `key:` alone means null and will fail a `type: array` schema — which is a good reason to schema-validate (`schemas.md`).

## Naming and Shape

- One naming convention per file: `snake_case` or `kebab-case`, never both. Kubernetes uses `camelCase`, Ansible `snake_case`, most CLIs `kebab-case` — match the ecosystem, not personal taste.
- Group by *lifecycle*, not by type: everything a deploy changes together goes together. A file organized by "all the timeouts, then all the URLs" forces every change to touch three sections.
- Depth beyond three or four levels means the structure is modelling a class hierarchy the config does not need. Flatten with dotted keys or split the file.
- Units in the key name or the value, never implied: `timeout_seconds: 30` or `timeout: 30s`. `timeout: 30` starts an argument in every incident.
- Comment *why*, never *what*: `# raised from 30 after the 2026-05 timeout incident` earns its line; `# the timeout` does not.
- Keep an explicit `version:` or `apiVersion:` key from day one (quoted, `"1"`), so the loader can migrate later without guessing.

## What Does Not Belong in the File

| Content | Where it goes |
|---|---|
| Secrets | A secret manager, or sops-encrypted (`security.md`) |
| Anything per-machine (paths, hostnames) | The gitignored local layer or env vars |
| Data that changes without a deploy | A database or a feature-flag service, not a file |
| Logic — conditionals, loops, expressions | Code. A config with an expression language is a program with bad tooling |
| Large blobs (certs, dashboards, datasets) | A file next to the config, referenced by path |
| Anything that grows unboundedly (per-customer entries) | A database; a 10,000-line YAML is a table with worse tooling (`parsers.md`) |

The test: *would a non-author be able to change this safely without reading the code?* If not, it is not configuration — it is source, and it belongs where source is reviewed.

## Environment Interpolation

- YAML has **no** variable substitution. Every `${VAR}` you have seen is the consumer's feature (Compose, Helm, Spring, envsubst, a config library) — so it works in one file and is a literal string in another.
- Prefer the loader's own env support to a pre-processing step: `envsubst < a.yaml.tpl > a.yaml` produces a generated file that then drifts from its template and gets edited by hand.
- Always give a default or a fail-fast: `${PORT:-8080}` or a schema `required`. Unset variables silently interpolating to an empty string produce `key:` → null.
- Quote the whole value: `url: "${BASE_URL}/api"` — `$` is not special to YAML but `{` at the start is (`strings.md`).

## Splitting Files

Split when a file is hard to *review*, not when it is long:

- By concern (`database.yaml`, `logging.yaml`) once sections are edited by different people.
- By environment once the diff between environments is more interesting than the base.
- Never by size alone — 400 well-grouped lines beat four files someone has to hold in their head at once.
- A directory the tool reads in lexical order (`conf.d/10-base.yaml`, `20-app.yaml`) is a good pattern, and the numeric prefix is the only thing making the order visible.
- A multi-document single file is the wrong split: one syntax error takes down every document, and text-level splitting on `---` is unsafe (`kubernetes.md`).

## Evolving the Format

- Additive changes with defaults are free. Renames and removals are not.
- Deprecate in three steps: accept both keys and warn, then warn louder for a release, then remove. A config load that fails on an old key after an upgrade is an outage.
- Ship a migration path with the release note: the exact `yq` expression that rewrites the old shape into the new one (`editing.md`).
- Bump the `version:` key on a breaking change, and make the loader refuse a version it does not understand rather than guessing.
- Keep a schema and version it with the format; the schema is the changelog people actually read (`schemas.md`).

## When YAML Is the Wrong Choice

| Situation | Better |
|---|---|
| Deeply repetitive across many environments | Generate the YAML from CUE, Jsonnet, or plain code |
| Machine-written, machine-read, never reviewed | JSON — no whitespace semantics, no implicit typing |
| Flat application settings, human-edited | TOML — explicit types, no indentation traps (`toml`) |
| Thousands of records | A database or NDJSON (`json`) |
| Needs conditionals and functions | A real language emitting the config at build time |
| A single value | An environment variable |

Ecosystem gravity is a legitimate counter-argument: Kubernetes, CI systems and Ansible take YAML, and generating it only moves the parsing problem to render time. The decision is where the human edits, not where the bytes end up.

**When a config layout or a merge policy is decided**, write the decision and its rejected alternatives to `~/Clawic/data/yaml/artifacts/<kebab-name>.md` — one file, from the first one, with its `## Boxes` line in `memory.md` in the same turn — and add each file it defines to `## Config Files` (`memory-template.md`). If the work belongs to a tracked project, the decision summary also goes to `~/Clawic/data/projects/<project>.md` and this box keeps only the project name as a pointer; duplicating the project record is how two skills start contradicting each other.
