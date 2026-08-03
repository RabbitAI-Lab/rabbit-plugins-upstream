# Working File Templates — YAML

Read this file only when WRITING. `config.yaml` is what the user **declared**; `memory.md` and everything it indexes is what you **observed** or produced. An observation never overwrites a declaration.

## Where each thing goes

| Data | Home | How it grows |
|---|---|---|
| Declared preferences — table keys and preference areas alike | `~/Clawic/data/yaml/config.yaml` | Key by key, read-modify-write |
| Current state, how they work, box index, due dates | `~/Clawic/data/yaml/memory.md` | Rewritten in place; stays small |
| Which parser, version and spec each project uses, and its observed quirks | `## Toolchain` in `memory.md`; `~/Clawic/data/yaml/toolchain.md` past the split threshold | One row per project or library |
| YAML files that matter: path, consumer, validator, templated or not | `## Config Files` in `memory.md`; `~/Clawic/data/yaml/configs.md` past the threshold | One row per file |
| Traps that actually bit, with the verbatim error and the fix | `## Gotchas Hit` in `memory.md`; `~/Clawic/data/yaml/gotchas.md` past the threshold | One row per incident, newest last |
| The formatting habits observed in an existing repo (not declared by the user) | `## Repo Style` in `memory.md` | One short block per repo |
| Things you produced that get re-read — a schema, a lint config, a working block-scalar or anchor layout, a yq recipe, a config-layout decision, a migration runbook | `~/Clawic/data/yaml/artifacts/<kebab-name>.md` | Born as its own file, from the first one |
| A device configured through YAML (Home Assistant, ESPHome, netplan, cloud-init) | `~/Clawic/data/devices/devices.md` (**shared**) | One row per device, every skill in one inventory |
| A decision that belongs to tracked work | `~/Clawic/data/projects/<project>.md` (**shared**); only the project name stays here | One file per project |
| **Anything durable this table does not name** | `~/Clawic/data/yaml/<plural-noun>.md`, or `artifacts/<kebab-name>.md` if it is a long text read whole | Name the file after what it holds, never after when it was made; add its `## Boxes` line in the same turn |
| Credentials of any kind | Nowhere under `~/Clawic/data/` | Pointer only — see Secrets |

## When to write

No permission needed; every write is announced in one line that names the file. Writes and deletions stay inside the paths declared in this skill's `configPaths`. A deletion is named in that same line, and in a shared box only rows this skill itself wrote are ever updated or removed.

| It happened | Write |
|---|---|
| A project's YAML library, version or spec version was established or corrected | `## Toolchain` |
| A YAML file was created, adopted, or gained a validator | `## Config Files` |
| A coercion, indentation, anchor or dialect trap bit and was fixed | `## Gotchas Hit` |
| An existing repo's indent, sequence or quote style was observed | `## Repo Style` |
| A schema, lint config, layout decision or reusable recipe came out of the session | `artifacts/` |
| A device was configured through a YAML file | Its row in `devices.md` |
| The decision belongs to tracked work | `projects/<project>.md`, name only here |
| The user declared a preference (quote style, indent, linter, spec, safety posture) | Its key in `config.yaml` |
| Recurring work was scheduled or run | `## Due` |

## Start flat, split only when it hurts

Everything except artifacts and the shared boxes begins inside `memory.md`. Splitting is a procedure, not a suggestion:

1. Before appending to a section, count its entries.
2. If the append would take it past **~15 entries or ~40 lines of real content** — scaffolding, headings and comments do not count — then, in the same turn: create the new file in `~/Clawic/data/yaml/`, move the whole section into it, **delete the section from `memory.md`**, add its line to `## Boxes`, and append the new entry to the new file.
3. Keep the headings identical on both sides of the move, so the split is a copy-paste and never a rewrite.
4. Never leave a copy behind. If the same data ever appears in both places, the extracted file wins and the `memory.md` copy is deleted.

Artifacts are the exception: a schema, a decision or a recipe is born as its own file whatever its size, because it is read whole and only when its subject comes up.

## Secrets

Nothing under `~/Clawic/data/` ever holds a secret value — not the files named here, not files you create, not text the user pastes in and asks you to keep. Store the pointer in its place, in this shape: `<kind>:<locator>`.

`env:DB_PASSWORD` · `keychain:prod-tls` · `1password:Work/Cluster/kubeconfig` · `vault:secret/data/prod#password` · `ssm:/prod/db/password` · `sops:secrets/prod.enc.yaml` · `profile:prod` · `file:~/.ssh/id_ed25519`

When the user pastes YAML to save, replace each secret value before writing and leave the pointer visible: `password: <ssm:/prod/db/password>`. Say in one line that you did it. The specific hazard here is a PEM key or a Kubernetes Secret pasted inside a `|` block while asking why it will not parse — the answer is about chomping, and the payload is never written down.

In this domain — **not secrets, keep them**: file paths, key names, environment variable *names*, schema URLs, image and chart names, namespaces, cluster and context names, hostnames, port numbers, anchor names, library and spec versions, yamllint rule ids, public certificates and CA bundles. **Secrets, strip them**: passwords, API keys and tokens, private keys, PEM blocks and passphrases, kubeconfig `client-key-data` and `token`, Kubernetes Secret `data:`/`stringData:` values, `.dockerconfigjson`, connection strings containing a password, Ansible Vault plaintext, `!secret` resolved values, webhook URLs with a token.

**Contents:** [config.yaml](#configyaml) · [memory.md](#memorymd) · [artifacts/](#artifacts) · [shared devices inventory](#shared-devices-inventory) · [shared projects box](#shared-projects-box) · [split-out files](#split-out-files)

## config.yaml

Keys come from the Configuration table in `SKILL.md`, plus free-form keys nested under a preference area. Write a key only when the user states the preference.

**Writing is read-modify-write**: load the existing file, set or replace only the key just declared, keep every other key byte for byte. Never emit a `config.yaml` from this template — the template shows shape, not content. Create `~/Clawic/data/yaml/` if it does not exist.

```yaml
spec_version: 1.2
indent_width: 2
sequence_indent: 2
quote_style: minimal
max_line_width: 120
yq_flavor: go
linter: yamllint
loader_policy: safe-only
anchor_policy: avoid
schema_gate: true

# Preference areas — free-form keys added as the user reveals them.
# A preference the user states is a declaration and belongs here, never in memory.md.
conventions:
  key_order: source
  document_start: true          # every file opens with ---
  empty_value: omit             # rather than `null` or `~`
platform:
  primary_consumer: kubernetes
safety_posture:
  secrets_in_repo: sops-only
```

If you find a preference recorded in `memory.md`, move it here and note the move.

## memory.md

Write only the sections you have content for — a heading with nothing under it is noise, and it inflates the line count that decides a split. Never copy these hints into the user's file. `## Boxes` is the one section that is never dropped when `memory.md` is rewritten: deleting a line there orphans a file forever. This is what a populated file looks like:

```markdown
# YAML Memory

## Status
status: ongoing
last: 2026-07-26

## Boxes
- Config file inventory (22 files) → `configs.md`; read before editing any YAML in these repos
- Values-layout decision for the platform chart → `artifacts/decision-values-layout.md`; read before changing chart values
- Repo yamllint config → `artifacts/yamllint-platform.md`; read before adding a lint rule

## Due
| What | Every | Last run | Next due |
|------|-------|----------|----------|
| Re-validate schemas after dependency bumps | quarter | 2026-04-10 | 2026-07-10 |
| Secret scan over YAML in all repos | month | 2026-07-02 | 2026-08-02 |

## Toolchain
| Project | Library | Version | Spec | Quirks observed |
|---|---|---|---|---|
| platform-api | PyYAML | 6.0.1 | 1.1 | `no`/`on` resolve to bool; dump sorts keys |
| deploy-charts | go-yaml v3 (via helm) | 3.0.1 | 1.1/1.2 mix | errors on duplicate keys; wraps output at 80 |

## Config Files
| Path | Consumer | Templated | Validator | Notes |
|---|---|---|---|---|
| charts/platform/values.yaml | helm | no | values.schema.json | lists replace on override |
| .github/workflows/ci.yml | GitHub Actions | no | actionlint | `on:` quoted for yq |
| infra/cloud-init.yaml | cloud-init | no | cloud-init schema | `#cloud-config` must stay line 1 |

## Gotchas Hit
| Date | File | Symptom | Cause | Fix |
|---|---|---|---|---|
| 2026-06-18 | values.yaml | image pulled tag 3.1 | `3.10` resolved as float | quoted the tag |
| 2026-07-02 | ci.yml | `yq '.on'` returned nothing | 1.1 read the key as `true` | quoted `"on":` |

## Repo Style
platform-api: 2-space indent, sequences indented, minimal quoting, no anchors, `---` at top of every file.

## How They Work
Reads YAML mostly for Kubernetes. Wants the corrected file, not the explanation of the rule.

---
*Updated: 2026-07-26*
```

Rules that keep this readable next month:

- **`## Boxes`**: one line per file that exists — `<what> (<volume>) → <file>; read when <condition>`. Written in the same turn the file is created. Never delete a line without deleting the file it points to. A box with no index line does not exist.
- **`## Due`**: check it against today's date at the start of a session and state any overdue item in one line — a statement, not a question. Every recurring thing this skill schedules belongs here.
- **`## Toolchain`**: one row per project, not per library. `Spec` is what the *installed version* resolves, not what the docs claim — it is the fact every quoting decision depends on, so record how it was verified when it was surprising.
- **`## Config Files`**: one row per file that someone will edit again. `Templated: yes` means it is not YAML until rendered, which changes every piece of advice given about it.
- **`## Gotchas Hit`**: keep the symptom in the user's words and the error verbatim — six months later that string is what gets searched for. Never delete a row because the bug is fixed; the row is the reason it stays fixed.
- These headings are exactly the ones the split-out files get, so a split stays a copy-paste.

| Status | Meaning |
|-------|---------|
| `ongoing` | Still learning their stack and conventions |
| `complete` | Know their parsers, files and house style |

## artifacts/

One file per thing, at `~/Clawic/data/yaml/artifacts/<kebab-name>.md`, created the first time it exists. Canonical types here: **a schema or lint config that finally passed**, **a config-layout or merge-policy decision**, **a block-scalar or anchor layout that was hard to get right**, **a yq/ruamel recipe**, **a format migration runbook**. Every artifact opens with when to read it, and gets its `## Boxes` line in the same turn.

```markdown
# Decision — values keyed by name, not a list
*Read before changing the chart's values structure. 2026-07-26.*

Decision: plugins are a map keyed by name, so an overlay can change one without restating all.
Rejected: list of maps — Helm's merge replaces lists, so every overlay had to repeat the collection.
Applies to: charts/platform/values.yaml, charts/worker/values.yaml.
Enforced by: values.schema.json (additionalProperties false).
```

```markdown
# Recipe — bump the image tag across a multi-document stream
*Read when a release needs the same tag in every manifest. yq v4 (go). 2026-07-26.*

...the expression, with the file it was verified against...
```

If the user tracks this work as a project, the decision summary also belongs in the shared `~/Clawic/data/projects/<project>.md`, with the detail staying here and referenced by name.

## Shared devices inventory

Lives at `~/Clawic/data/devices/devices.md` and is shared with every other skill that touches hardware — the user may not have any of them installed, so the format travels with this skill. A device configured through a YAML file (Home Assistant, ESPHome, netplan, cloud-init) belongs here, never in the YAML box.

```markdown
# Devices

| Name | Type | Model | Location | Network | Config file | Notes |
|------|------|-------|----------|---------|-------------|-------|
| living-room-thermostat | thermostat | Tado V3+ | living room | wifi-iot / aa:bb:cc:dd:ee:01 | ha/configuration.yaml | climate.living_room |
```

- **Identity is the network name or MAC.** Read the file before adding and look for that key. If it is there, update the row in place — never append a second row for the same device.
- **Retirement is part of the inventory.** When a device is removed, delete its row and note the date in `memory.md`. An inventory that only grows stops being an inventory.
- **Units and currency go inside the value** (`24 C`, `62 EUR`), because rows written by other skills use other systems and someone will compare them.
- **Scale cut**: one row per device while there are ≤15. Past that, one file per device at `~/Clawic/data/devices/<name>.md` with the same fields, and `devices.md` becomes the index (`Name | Type | Location | → file`). If the folder already looks like that, follow it — do not start a parallel `devices.md`.
- **Foreign columns win.** If `devices.md` already exists with a different column set, match its columns and add anything missing as a trailing note. Never rewrite its header.
- Credentials for a device are a pointer only: `!secret`-backed values become `<file:secrets.yaml>`, never the value.

## Shared projects box

Lives at `~/Clawic/data/projects/<project>.md`, one file per project, shared with every skill that touches the same work.

- **Identity is the project name** (the file's slug). Read the folder before creating a file: if the project already has one, append your section to it rather than creating `project-2.md`.
- Write only what this skill owns: the config-format decision, the schema it introduced, the migration it planned — under a heading of its own so another skill's section stays untouched.
- **Never duplicate the project's own record** (goal, status, milestones); those belong to whichever skill owns the project. Here the YAML box keeps only the project name as a pointer.
- **Retirement**: a finished project keeps its file with `status: done — <date>` inside; never delete it, it is the record of what was delivered. Past ~20 closed projects, move them to `projects/archive/<project>.md` without renaming.
- Amounts carry their currency, dates are ISO, and no credential appears anywhere in the file.

## Split-out files

Created only by the split procedure above, never on day one. Each keeps the exact headings it had inside `memory.md`.

`configs.md` — `## Config Files`, one `### <repo>` heading per repository once more than one is tracked. The reason this file exists: knowing which files are templated and which are rewritten by their tool is what stops a session from proposing anchors or comments into a file that destroys them.

`toolchain.md` — `## Toolchain`, plus a `## Verified` line per row recording how a surprising resolution was confirmed. Without it the same PyYAML-versus-go-yaml argument is re-run every quarter.

`gotchas.md` — `## Gotchas Hit`, newest last, error strings verbatim. This is the file that makes the second occurrence of a trap a ten-second fix.
