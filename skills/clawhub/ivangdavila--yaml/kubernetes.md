# Kubernetes YAML — Manifests, Helm, kustomize

The YAML layer under Kubernetes has its own rules because the API server does not read YAML: `sigs.k8s.io/yaml` converts the document to JSON and unmarshals it with `encoding/json` struct tags. Everything odd about manifests follows from that one fact. What the fields *mean* once they parse is `k8s`; this file is the parsing and templating layer.

**Contents:** [The YAML→JSON Consequence](#the-yamljson-consequence) · [Fields That Must Be Strings](#fields-that-must-be-strings) · [Multi-Document Files](#multi-document-files) · [Quantities and Modes](#quantities-and-modes) · [Helm Templating](#helm-templating) · [Helm Values](#helm-values) · [kustomize](#kustomize) · [Validation Chain](#validation-chain) · [Reading What the Cluster Stored](#reading-what-the-cluster-stored)

**Before editing manifests for an existing setup**, read `## Config Files` in `~/Clawic/data/yaml/memory.md` — which files are rendered vs hand-written, and which are rewritten by a controller, decides whether anchors and comments will survive at all.

## The YAML→JSON Consequence

- **Anchors and merge keys never reach the cluster.** They are expanded during conversion; `kubectl get -o yaml` returns fully expanded objects. Reuse must happen before the API call (kustomize, Helm), not inside the manifest (`anchors.md`).
- **Duplicate keys** are an error in the Go decoder, but the message points at the JSON conversion, not the YAML line.
- **Unknown fields** are dropped silently by default and rejected with `--validate=strict` (the default for `kubectl apply` since v1.25 against a server that supports it). A typo'd `imagePullPolicty` used to be invisible; now it errors — but only against the server.
- **JSON is valid input** anywhere YAML is, including inline: `command: ["sh","-c","echo hi"]` is idiomatic and unambiguous.
- Comments are lost the moment the object is stored, so a comment in a manifest documents the *source file*, not the running object.

## Fields That Must Be Strings

Type coercion (`types.md`) hits Kubernetes constantly because so many fields are string-typed:

| Field | Wrong | Right | Error if wrong |
|---|---|---|---|
| `env[].value` | `value: 8080` | `value: "8080"` | `cannot unmarshal number into Go struct field EnvVar.value of type string` |
| `env[].value` for a bool | `value: true` | `value: "true"` | Same, with `bool` |
| Image tag | `image: app:1.10` | fine — the whole ref is a string | — |
| `nodeSelector` / label values | `tier: 1` | `tier: "1"` | Label values must be strings |
| Annotations | any non-string | quote everything | Annotations are `map[string]string` |
| ConfigMap `data` values | `port: 8080` | `port: "8080"` | Same unmarshal error; use `binaryData` for bytes |
| `args` | `- --replicas=3` fine; `- -1` | `- "-1"` | Leading `-` inside a plain scalar is fine, but a bare negative number becomes an int |
| Version-like values | `version: 1.10` | `version: "1.10"` | Silently becomes 1.1 |

Rule: **inside `env`, `data`, `annotations`, `labels` and `nodeSelector`, quote every value, without exception.** It costs nothing and removes the entire class.

## Multi-Document Files

- `---` separates documents; the API applies them in file order. Order matters for Namespace → everything else, and for CRD → custom resource (a CR applied before its CRD fails).
- `...` (end of document) is legal and rarely used; `kubectl` handles it, some naive splitters do not.
- **Never split a manifest file on `---` with a text tool**: a `---` inside a literal block scalar (a ConfigMap holding another YAML document) is content, not a separator. Use `yq -s` or the parser.
- An empty document between two separators loads as `null`; `kubectl` skips it, some other tools error. A trailing `---` at end of file is the usual source.
- A leading `---` on the first document is optional and conventional in this ecosystem.

## Quantities and Modes

- Resource quantities are strings with suffixes: `memory: 512Mi`, `cpu: 500m`. Unquoted they are strings anyway (letters present), but `cpu: 1` is an int and legal, while `cpu: 0.5` is a float and also legal — prefer `500m` because the decimal form re-serializes unpredictably.
- **`Mi` vs `M`**: `512Mi` is 536,870,912 bytes; `512M` is 512,000,000 — 4.9% less. The gap widens per power: `Gi` vs `G` is 7.4% (1,073,741,824 vs 1,000,000,000), `Ti` vs `T` is 10%. It shows up as an OOM kill only under load.
- `defaultMode`/`fileMode` in volumes takes a *decimal* integer. `0644` in a 1.1 parser resolves to 420, which is what the API wants; `0644` under a strict 1.2 parser is 644, which sets the wrong bits. Write `0644` and confirm with `kubectl get -o yaml` that the stored value is 420, or write `420` with a comment (`types.md`).
- Durations are strings: `terminationGracePeriodSeconds: 30` is an int; `activeDeadlineSeconds` too; but `timeoutSeconds` in a probe is an int and `sleep: "30s"` in a script is a string. Follow the schema, not the shape.

## Helm Templating

A Helm template is **not YAML until it is rendered** — never lint or parse the template as YAML.

| Problem | Cause | Fix |
|---|---|---|
| Indentation collapses after an inserted block | `indent` used where `nindent` was needed | `{{- toYaml .Values.x \| nindent 8 }}` — `nindent` adds the leading newline, `indent` does not |
| Rendered value becomes a bool/number | Unquoted template output | `{{ .Values.tag \| quote }}`, or wrap in `"{{ }}"` |
| A missing value produces `key:` → null | No default | `{{ .Values.x \| default "y" }}`, or wrap the whole block in `{{- if }}` |
| Whitespace and blank lines everywhere | Missing chomping in the action delimiters | `{{-` strips preceding whitespace, `-}}` strips following |
| A multiline value breaks the document | Raw insertion | `{{ .Values.script \| toYaml \| nindent 4 }}`, or `\| b64enc` for Secret data |
| `error converting YAML to JSON` at line N | The *rendered* output, not the template | `helm template . > /tmp/out.yaml` and read line N there |
| Values from `--set` typed wrong | `--set` infers types | `--set-string key=1.10` |

- Debug loop, always: `helm template . -f values.yaml | yq -o=json | head`. If it renders, it is a schema problem; if it does not, it is an indentation or quoting problem in the template.
- `helm lint` checks the chart's structure, not the rendered manifests — pipe the render into `kubeconform` for that (`schemas.md`).
- `.Values` keys are case-sensitive and `camelCase` by convention; a `snake_case` key that never matches produces a silently empty render.

## Helm Values

- `values.yaml` is merged with `-f` overlays and `--set` flags. Later `-f` wins; `--set` beats every file.
- **Maps deep-merge, lists replace.** Overriding one element of a list means restating the whole list — the single most common Helm surprise. Design values as maps keyed by name when items must be individually overridable (`config-design.md`).
- `null` in an overlay *removes* the key in Helm's merge (unlike most other mergers) — one of the few places where null-as-delete is the actual semantics.
- Ship a `values.schema.json`: Helm validates against it automatically on install and template, giving typed errors instead of a broken render.
- Document every value in `values.yaml` with a comment — it is the chart's API, and the comment is the only documentation that stays in sync.

## kustomize

- Every file is a plain manifest, so it lints and validates normally. That is the point of the tool.
- **Anchors do not cross files**, and a base's anchor is invisible to an overlay (`anchors.md`).
- Strategic merge patches merge lists **by key** (`name` for containers, `containerPort` for ports) rather than replacing them; JSON 6902 patches address by index and break when the order changes. Prefer strategic merge; use 6902 when the target has no merge key.
- A patch whose target does not exist is a silent no-op in some versions and an error in others — verify with `kustomize build` and diff, never assume.
- `configMapGenerator` appends a content hash to the name and rewrites references; hand-written references to the un-hashed name break.

## Validation Chain

Cheapest to most authoritative — run in this order:

1. `yamllint -s` on hand-written manifests (not on templates)
2. `kustomize build` / `helm template` to get real YAML
3. `kubeconform -strict -summary` against that output, with CRD schemas loaded
4. `kubectl apply --dry-run=server` for admission webhooks and defaults
5. `kubectl diff -f` against the live cluster before applying

Steps 3 and 4 catch different things: kubeconform catches shape offline, dry-run-server catches policy, quotas, and mutating webhooks.

## Reading What the Cluster Stored

- `kubectl get <kind> <name> -o yaml` shows the object after defaulting and mutation, which is what actually runs — compare it against the source file when behavior does not match.
- `kubectl get ... -o yaml --show-managed-fields=false` removes the `managedFields` noise that makes the output unreadable.
- `metadata.annotations["kubectl.kubernetes.io/last-applied-configuration"]` holds the last client-side-applied JSON — useful history, and a place secrets leak into.
- Server-side apply conflicts (`field is managed by …`) are about ownership, not YAML.

**When something durable comes out of this work** — a manifest layout that finally validated, a Helm values structure worth reusing, a kustomize overlay pattern, the discovery that a controller rewrites a given file — save it to `~/Clawic/data/yaml/artifacts/<kebab-name>.md` with its `## Boxes` line, and update the file's row in `## Config Files` of `~/Clawic/data/yaml/memory.md` (`memory-template.md`). Never copy Secret payloads or kubeconfig material into either: pointer only (`security.md`).
