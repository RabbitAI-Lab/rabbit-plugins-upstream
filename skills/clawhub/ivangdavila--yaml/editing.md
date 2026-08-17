# Editing — Reading, Patching, Merging, Diffing

Editing YAML programmatically has exactly two safe shapes: a round-trip loader that preserves everything it did not change, or a text-level patch. Load-then-dump is neither, and it is what most scripts do.

**Contents:** [The Three Approaches](#the-three-approaches) · [yq](#yq) · [Round-Trip in Python](#round-trip-in-python) · [Inspecting What the Parser Read](#inspecting-what-the-parser-read) · [Merging Files](#merging-files) · [Diffing](#diffing) · [Converting To and From JSON](#converting-to-and-from-json) · [Bulk Edits Across a Repo](#bulk-edits-across-a-repo) · [Sorting and Normalizing](#sorting-and-normalizing)

**Before rewriting a file that is not yours**, read `## Config Files` and `## Repo Style` in `~/Clawic/data/yaml/memory.md` — indent width, sequence style and quoting habits are recorded there, and matching them is the difference between a two-line diff and a whole-file diff.

## The Three Approaches

| Approach | Preserves comments/order/style | Use when |
|---|---|---|
| Round-trip loader (`ruamel` rt, eemeli `yaml`, `yq -i`) | Yes | Editing a file a human maintains |
| Load → dump (PyYAML, go-yaml, js-yaml) | No | The file is generated anyway and nobody reads the source |
| Text patch (sed, a diff, an editor macro) | Yes, trivially | A single unambiguous token, and the risk of matching the wrong line is low |

The failure to avoid: using load→dump on a hand-maintained file. The result is semantically correct and unreviewable — every comment gone, keys alphabetized, quotes normalized, block scalars flattened into escaped one-liners. Reviewers approve it because "the tests pass", and the comments never come back.

## yq

Two unrelated tools share the name. `yq_flavor` picks which one the examples use.

**mikefarah/yq (Go, jq-like, the common one):**

| Task | Command |
|---|---|
| Read a value | `yq '.spec.replicas' f.yaml` |
| Set a value in place | `yq -i '.spec.replicas = 3' f.yaml` |
| Set a string explicitly | `yq -i '.version = "1.10"' f.yaml` — without quotes it writes a float |
| Add to a list | `yq -i '.args += ["--verbose"]' f.yaml` |
| Delete a key | `yq -i 'del(.metadata.annotations)' f.yaml` |
| Only one document of a stream | `yq -i 'select(.kind == "Deployment") \| .spec.replicas = 3' f.yaml` |
| All documents | `yq -i '(.. \| select(has("image"))).image = "x"' f.yaml` |
| Merge two files | `yq eval-all '. as $item ireduce ({}; . * $item)' a.yaml b.yaml` |
| Expand anchors | `yq 'explode(.)' f.yaml` |
| Convert to JSON | `yq -o=json f.yaml` |
| From env var, safely | `yq -i '.token = strenv(TOKEN)' f.yaml` |

- `-i` rewrites in place and **preserves comments and anchors**; it does re-indent to its own settings, so run it once on the whole repo before adopting it, not file by file.
- `*` is a shallow-ish merge with modifiers: `*+` appends arrays, `*d` deep-merges, `*n` only sets null/missing keys.
- Quoting inside the expression is the usual source of bugs: single-quote the whole expression for the shell, double-quote strings inside it.

**kislyuk/yq (Python):** `yq '.spec.replicas' f.yaml` looks identical and is jq operating on JSON converted from YAML — comments and anchors are gone in the output, and `-i` behaves differently. Check which one is installed with `yq --version` before writing a script that others will run.

## Round-Trip in Python

```python
from ruamel.yaml import YAML
yaml = YAML()                 # typ='rt' is the default
yaml.preserve_quotes = True
yaml.indent(mapping=2, sequence=4, offset=2)
with open("f.yaml") as fh:
    data = yaml.load(fh)
data["spec"]["replicas"] = 3
with open("f.yaml", "w") as fh:
    yaml.dump(data, fh)
```

- `preserve_quotes = True` is not the default and its absence rewrites every quoted scalar.
- `yaml.indent(sequence=4, offset=2)` reproduces the indented-dash style; `sequence=2, offset=0` reproduces the flush style. Match the file (`sequence_indent`).
- Attach a comment: `data.yaml_set_comment_before_after_key("key", before="why")`. Reading comments back is possible through `.ca` but is a private-ish API — do not build on it.
- ruamel errors on duplicate keys and on some files PyYAML accepts. That is a feature; fix the file.
- Writing a *new* file needs no round-trip loader — use whatever emitter, with the settings from `parsers.md`.

## Inspecting What the Parser Read

The single most useful debugging move in this domain, because YAML's failures are type failures:

- Python: `python3 -c "import yaml,pprint;pprint.pprint(yaml.safe_load(open('f.yaml')))"` — types are visible (`True` vs `'true'`, `datetime.date` vs `'2026-07-26'`).
- Anything: `yq -o=json f.yaml | jq .` — JSON has no implicit typing, so what you see is what the parser resolved. A quoted `"3"` in the JSON means it stayed a string.
- Types only: `yq '.. | [path | join("."), type] | @tsv' f.yaml` lists every leaf and its type — the fastest audit for a coercion bug in a large manifest.
- Multi-document: `yq '.kind' f.yaml` prints one line per document, confirming the stream split where you thought.

## Merging Files

YAML has no merge operator across files (`<<` is within one document). Merging is the consumer's behavior, and the three strategies differ on lists:

| Strategy | Maps | Lists | Used by |
|---|---|---|---|
| Replace | replaced whole | replaced whole | Simple loaders, `yq '. * $x'` at leaf level |
| Deep merge | merged recursively | **replaced**, not concatenated | Helm values, `yq '. *d $x'`, most config libs |
| Deep merge + append | merged recursively | concatenated | `yq '. *+ $x'`, some CI tools |
| Strategic merge | merged by a key field | merged by `name`/patchMergeKey | Kubernetes (`kubernetes.md`) |

- List replacement is the surprise: an overlay that sets one item in `args` replaces all of them. Design around it (`config-design.md`).
- `null` in an overlay usually *sets* the key to null rather than deleting it; only strategic merge and a few libraries treat null as delete.
- Order matters and is not obvious: for `-f a.yaml -f b.yaml`, later usually wins (Compose, Helm), but for YAML `<<: [*a, *b]`, earlier wins (`anchors.md`).

## Diffing

- Textual `git diff` on YAML is noisy: a re-indent, a re-order, or an emitter width change produces a full-file diff with zero semantic change.
- `dyff between a.yaml b.yaml` compares the loaded structures and reports value changes, ignoring formatting and key order. The right tool for reviewing a regenerated file.
- Normalize-then-diff, portable: `yq -P 'sort_keys(..)' a.yaml > /tmp/a; yq -P 'sort_keys(..)' b.yaml > /tmp/b; diff /tmp/a /tmp/b`.
- For a rendered artifact (Helm output, kustomize build), diff the render, never the source — the source diff cannot show what changed downstream.
- In review: ask for the *semantic* diff whenever a change touches more than about 20% of a file's lines. That is the threshold above which a human stops reading.

## Converting To and From JSON

- YAML 1.2 is designed as a JSON superset, so any JSON file is loadable as YAML. The practical exception is duplicate keys, which JSON tolerates and strict YAML parsers reject.
- YAML → JSON always loses: comments, anchors, key styling, multi-document structure (JSON has one root — a stream becomes an array or an NDJSON file), and non-string keys (JSON keys are strings, so `2026: x` becomes `"2026": x`).
- `yq -o=json`, `yq -P` (JSON→YAML), `python -c "import sys,yaml,json;json.dump(yaml.safe_load(sys.stdin),sys.stdout)"`.
- Round-tripping YAML→JSON→YAML is a reliable way to *strip* a file to its data: useful deliberately, disastrous by accident.

## Bulk Edits Across a Repo

1. Enumerate first: `git ls-files '*.yaml' '*.yml'`, and check `.yamllint`/`.editorconfig` for the style in force.
2. Dry run on one file, diff, and read the whole diff.
3. Apply with the same tool and settings everywhere — mixing `yq -i` and a hand edit produces two indentation styles in one repo.
4. Re-validate every touched file with the consumer's validator (Rule 10), not just with a parser.
5. Commit the formatting-only change separately from the semantic change, or review is impossible.

## Sorting and Normalizing

- Alphabetical key order makes diffs and merges cleaner and destroys the author's grouping. Choose per repo (`Conventions` preference area); never let a tool's default decide it silently.
- Kubernetes manifests have a conventional order (`apiVersion`, `kind`, `metadata`, `spec`) that no sorter respects — do not alphabetize them.
- Normalizing quotes, indentation and line width across a repo is worth one noisy commit and then a lint rule to hold it (`schemas.md`).

**When a non-obvious edit recipe finally works** — a yq expression over a multi-document stream, a ruamel configuration that reproduced the repo's style exactly, a merge order that matched the consumer — save it to `~/Clawic/data/yaml/artifacts/<kebab-name>.md` with the file it applies to and the tool version, and add its `## Boxes` line in the same turn (`memory-template.md`). If the edit revealed a house style, that goes to `## Repo Style` in `memory.md`; if the user declared the style, it goes to `config.yaml`.
