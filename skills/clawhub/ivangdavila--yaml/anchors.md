# Anchors, Aliases, and Merge Keys

Anchors are the only DRY mechanism YAML has, and they are resolved at parse time — which means they are a property of the *file*, never of the data. Every disappointment with anchors comes from expecting them to survive something that only sees the data.

**Contents:** [Syntax](#syntax) · [Merge Keys](#merge-keys) · [The Five Hard Limits](#the-five-hard-limits) · [Where Anchors Survive](#where-anchors-survive) · [Patterns That Work](#patterns-that-work) · [Alternatives by Ecosystem](#alternatives-by-ecosystem) · [Expansion Cost](#expansion-cost)

**Before adding anchors to a file that other tools touch**, read `## Config Files` in `~/Clawic/data/yaml/memory.md` — the row records what reads that file and whether it rewrites it, which is the whole decision.

## Syntax

```yaml
defaults: &defaults      # anchor: names this node
  adapter: postgres
  pool: 5

development:
  <<: *defaults          # merge key: pull in the mapping's pairs
  database: dev_db

test: *defaults          # alias: this node IS that node
```

- `&name` attaches to the node that follows it — a mapping, a sequence, or a single scalar (`retries: &r 3` then `attempts: *r`).
- `*name` is a reference to the same node, not a copy. In most loaders the two names point at one object in memory; mutating one mutates the other.
- Anchor names are `[A-Za-z0-9_-]`-ish, cannot contain `[ ] { } ,`, and are re-definable: a second `&defaults` later in the file shadows the first from that point on. No warning.
- An alias must appear **after** its anchor in document order. Forward references are illegal: `found undefined alias`.

## Merge Keys

`<<` is a YAML 1.1 type-library extension, not part of the 1.2 core schema. Supported by PyYAML, ruamel, go-yaml v2/v3, Ruby Psych and js-yaml (with the default schema); not guaranteed elsewhere, and a strict 1.2 validator may report `<<` as a literal key.

- Precedence: **keys written in the node win over merged keys.** The override is per key, at the top level of the mapping only.
- Multiple sources: `<<: [*a, *b]` — earlier entries in the list win over later ones. This is the reverse of most people's intuition and the reason a two-source merge silently picks the wrong value.
- **The merge is shallow.** `<<: *defaults` where `defaults.db.pool: 5` and the local node sets `db: {name: x}` produces `db: {name: x}` — `pool` is gone, because the whole `db` map was replaced, not merged. Nesting needs a second anchor at the inner level.
- You cannot merge into a sequence, and you cannot delete a key that came from a merge. Setting it to `null` gives a present-but-null key, which is not the same as absent (`types.md`).

## The Five Hard Limits

1. **File-scoped.** An anchor is invisible across `!include`, GitLab `include:`, kustomize resources, Helm files, or any multi-file assembly. Each document in a multi-doc stream is also its own scope: an anchor defined before the first `---` is not visible after it.
2. **Cannot be partially overridden except through `<<`.** A plain alias `*defaults` is the same node; there is no syntax to alias-and-tweak.
3. **Shallow merge only** (above).
4. **Lost on re-emit.** Anything that loads to plain data and dumps again writes the expanded copy.
5. **Invisible in the rendered artifact.** The reader of the applied config sees duplication, so the DRY-ness helps only the person editing the source file.

## Where Anchors Survive

| Path | Anchors survive? |
|---|---|
| Human reads the file | Yes |
| `yamllint`, schema validation | Yes (validated after expansion) |
| `yq` in-place edit (mikefarah) | Yes, and `yq 'explode(.)'` expands them on purpose |
| `ruamel.yaml` round-trip mode | Yes |
| PyYAML / go-yaml load → dump | No — expanded |
| `yq -o=json`, any YAML→JSON conversion | No |
| `kubectl apply` (server stores the object) | No — `kubectl get -o yaml` returns the expanded form |
| Helm rendering | Yes within one file before templating; the rendered output is expanded |
| GitLab CI, CircleCI, Compose | Yes — these parse the file directly |
| GitHub Actions | Yes as YAML, but Actions offers no way to reuse across files anyway (`pipelines.md`) |

The rule that follows: **use anchors in files a human edits and one parser reads; avoid them in files a controller or a formatter rewrites** (`anchor_policy`).

## Patterns That Work

```yaml
# 1. Base + overrides, one level deep
x-base: &base                 # x- prefix: Compose ignores unknown top-level x- keys
  restart: unless-stopped
  logging:
    driver: json-file

# 2. Scalar anchors for a repeated constant
x-image-tag: &tag "1.24.3"    # quoted: a version is a string (types.md)

# 3. Two-level anchors so the inner map can be merged too
x-logging: &logging
  driver: json-file
  options: {max-size: "10m"}
```

- Name anchors after the *role* (`&base`, `&prod-limits`), not the first place they were used (`&web`), or the second consumer makes the name a lie.
- Keep every anchor definition at the top of the file, in one block. Anchors defined inline halfway down are what makes redefinition accidents happen.
- In Compose, prefix anchor-holding top-level keys with `x-`: the spec reserves `x-` for extensions and validators ignore them. Without the prefix, the anchor block becomes a service named `defaults`.
- If a file needs more than about five anchors or any two-level merge, it has outgrown the mechanism — generate it instead (`config-design.md`).

## Alternatives by Ecosystem

| Need | Instead of anchors |
|---|---|
| Kubernetes manifests | kustomize bases + overlays, or Helm values (`kubernetes.md`) |
| Helm chart internals | `define`/`include` templates, `toYaml` |
| GitLab CI | `extends:` — works across `include:`d files, which anchors cannot; and it deep-merges, unlike `<<` |
| GitHub Actions | Reusable workflows (`workflow_call`) and composite actions; there is no YAML-level reuse |
| Compose | `extends:` for a service, or profiles + multiple `-f` files (later files override) |
| Ansible | Variable precedence and `group_vars`, not YAML reuse |
| App config across environments | Layered files merged by the loader (`config-design.md`) |
| CloudFormation | Nested stacks, `Fn::Transform`, or a generator |

## Expansion Cost

Aliases are shared references on load, but *serialization* expands them, and nesting multiplies: ten anchors each referencing the previous one ten times is 10^10 nodes from a file of a few hundred bytes. That is the billion-laughs bomb, and a safe loader does not stop it (`security.md`, Rule 6).

For legitimate files this matters at a smaller scale too: a Compose or CI file that aliases a large block into forty services costs forty copies in memory and in every rendered diff.

**When an anchor layout is adopted or deliberately rejected for a repo**, record it: the layout itself, if it is a file worth re-reading, goes to `~/Clawic/data/yaml/artifacts/<kebab-name>.md` with its `## Boxes` line; a standing "we do not use anchors here" is a declaration and belongs in `anchor_policy` in `config.yaml`. If the reason was a tool that expanded them, that fact is a row in `## Toolchain` of `memory.md` (`memory-template.md`) — it is the same argument otherwise, every quarter.
