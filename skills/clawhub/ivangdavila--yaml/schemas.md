# Schemas and Linting — Making the Editor and CI Catch It

Every trap in this skill is detectable mechanically. A linter catches style and truthiness; a JSON Schema catches shape and types; the consumer's own validator catches everything else. Three layers, cheap to install, and they turn a class of runtime bugs into red text in the editor.

**Contents:** [The Three Layers](#the-three-layers) · [Editor Schema Binding](#editor-schema-binding) · [JSON Schema Against YAML](#json-schema-against-yaml) · [yamllint](#yamllint) · [Prettier and Formatters](#prettier-and-formatters) · [Per-Tool Validators](#per-tool-validators) · [The CI Gate](#the-ci-gate) · [Writing a Schema for Your Own Config](#writing-a-schema-for-your-own-config)

**Before adding a validation layer**, read `## Config Files` in `~/Clawic/data/yaml/memory.md` — the inventory records which files already have a schema and which validator each consumer uses, so the gate is added once and not three times.

## The Three Layers

| Layer | Catches | Misses | Cost |
|---|---|---|---|
| Linter (yamllint) | Tabs, indentation drift, duplicate keys, truthy values, trailing spaces, line length | Anything about meaning | Minutes |
| JSON Schema | Wrong types, unknown keys, missing required keys, bad enums and patterns | Cross-field logic the tool enforces | An hour, or free if a public schema exists |
| Consumer's validator | Everything the tool actually rejects | Runtime behavior | Usually one command |

Run them in that order: the linter's output is readable, the schema's is precise, and the consumer's is authoritative. `schema_gate` (default true) makes the third one mandatory before a file is called done.

## Editor Schema Binding

One comment on line 1 gives autocomplete, hover docs and inline errors in every editor that runs the YAML language server (VS Code's YAML extension, `yaml-language-server` in Neovim, JetBrains):

```yaml
# yaml-language-server: $schema=https://json.schemastore.org/github-workflow.json
```

- Schema Store hosts schemas for GitHub Actions, GitLab CI, Compose, Kubernetes, Renovate, Dependabot, `.golangci.yml`, Ansible, OpenAPI and hundreds more. Its catalog also auto-matches by filename, so `.github/workflows/*.yml` often works with no comment at all.
- Kubernetes manifests: point at the CRD-aware bundle (`kubernetes-json-schema` / `CRDs-catalog`) rather than the built-in, or every custom resource shows as unknown.
- A relative path works for your own schema: `$schema=../schemas/config.schema.json`.
- The same comment is inert to every other tool — it is a comment. Cost is one line.

## JSON Schema Against YAML

JSON Schema validates the loaded data, so it works on YAML unchanged. The subtlety: **the schema sees what the parser resolved**, so `version: 1.0` fails `"type": "string"` — which is exactly the wanted behavior, and the fix is quoting in the YAML, not loosening the schema.

| Tool | Command |
|---|---|
| `check-jsonschema` (Python) | `check-jsonschema --schemafile s.json f.yaml` — also has `--builtin-schema vendor.github-workflows` |
| `ajv-cli` (Node) | `ajv validate -s s.json -d f.yaml` (needs a YAML loader flag or a pre-conversion) |
| `yajsv` (Go) | `yq -o=json f.yaml \| yajsv -s s.json /dev/stdin` |
| Python inline | `jsonschema.validate(yaml.safe_load(f), schema)` |

Settings that make a schema actually catch things:

- `"additionalProperties": false` on every object — without it a typo'd key is simply ignored, and that is the most common silent config bug.
- `"required"` lists, not just property definitions.
- `"type": "string"` plus `"pattern"` for identities (versions, ids, modes) — this is what turns Rule 1 into a machine check.
- `"enum"` for anything with a fixed set of values; the error message names the valid options, which no other layer does.

## yamllint

Default config plus the four rules worth changing:

```yaml
# .yamllint
extends: default
rules:
  line-length: {max: 120, level: warning}   # from max_line_width
  truthy: {check-keys: true}                # catches on:, yes:, no: as keys and values
  key-duplicates: enable                    # error, always
  indentation: {spaces: 2, indent-sequences: true}   # from indent_width / sequence_indent
  document-start: disable                   # or enable, but pick one for the repo
```

- `truthy` with `check-keys: true` is the rule that catches the GitHub Actions `on:` problem and every `yes:`-shaped key.
- `yamllint -s` (strict) makes warnings exit non-zero — the right setting in CI, the wrong one locally.
- Inline suppression: `# yamllint disable-line rule:line-length` on the line above, or `# yamllint disable rule:x` … `# yamllint enable rule:x` around a block. Suppressions need a reason in the comment or they spread.
- yamllint parses with PyYAML, so it reports 1.1 resolution. On a 1.2 consumer some `truthy` hits are false positives — quote anyway, since the quoted form is correct under both.

## Prettier and Formatters

- Prettier formats YAML (indentation, quotes, line width) and is the low-effort way to stop style arguments. It rewrites quote style, which conflicts with `quote_style: minimal` on files where a quote is load-bearing — verify with a load-and-dump diff after the first run.
- `prettier --check` in CI, `--write` in a pre-commit hook. Never both formatters and a formatting linter with different settings — pick one owner for style (`linter`).
- Formatting-only commits go in alone (`editing.md`).

## Per-Tool Validators

| File | Validator | Notes |
|---|---|---|
| Kubernetes manifest | `kubeconform -strict -summary` | Offline, CRD schemas via `-schema-location`; `kubectl apply --dry-run=server` is authoritative but needs a cluster |
| Helm chart | `helm lint` + `helm template \| kubeconform` | Lint alone does not validate rendered manifests |
| kustomize | `kustomize build \| kubeconform` | Build failures are usually patch-target mismatches, not YAML |
| GitHub Actions | `actionlint` | Also checks shell inside `run:` and expression syntax |
| GitLab CI | `glab ci lint`, or the project's CI Lint endpoint | Catches `extends` and `include` resolution, which no schema can |
| Compose | `docker compose config` | Prints the merged, resolved file — also the fastest way to see what an override did |
| Ansible | `ansible-lint`, `ansible-playbook --syntax-check` | Lint knows the module schemas |
| CloudFormation | `cfn-lint` | Understands `!Ref`-style local tags that a generic parser cannot |
| OpenAPI | `spectral lint`, `redocly lint` | Style rules on top of schema validity |
| Anything else | Load it in the consumer with a dry-run flag | If it has no dry run, write the JSON Schema |

## The CI Gate

Minimum viable, in one job, ordered cheapest-first so failures come back fast:

1. `yamllint -s .`
2. Schema validation of every file that has one (`check-jsonschema`)
3. The consumer's validator for each file type present
4. A secret scan over YAML files (`gitleaks detect`, `trufflehog`) — YAML is where secrets get pasted (`security.md`)

Add it as a pre-commit hook too: the hook catches the tab before it becomes a CI run.

## Writing a Schema for Your Own Config

Worth it above roughly three consumers or three environments of the same file — below that, a typed loader in the application does the same job with less machinery.

1. Generate a first draft from a known-good file (`genson`-style tools, or hand-write from the loader's struct/dataclass).
2. Tighten: add `required`, set `additionalProperties: false`, replace `"type": "number"` with `pattern`-constrained strings for identities.
3. Publish it at a stable path inside the repo and reference it from the `# yaml-language-server:` comment in every instance file.
4. Version it alongside the config format; a schema that lags the code teaches people to ignore it.
5. Keep the schema in JSON even when the config is YAML — every validator reads JSON Schema, and the schema itself has no readability problem worth solving.

**When a schema, a lint config, or a CI gate is finally in place**, save the file itself to `~/Clawic/data/yaml/artifacts/<kebab-name>.md` (or its location, if it lives in the repo), add its `## Boxes` line, and update the affected rows of `## Config Files` in `~/Clawic/data/yaml/memory.md` with which validator now guards them (`memory-template.md`). If a re-validation cadence was agreed — after a dependency bump, quarterly, on every schema release — it becomes a row in `## Due`.
