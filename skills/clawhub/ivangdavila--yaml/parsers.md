# Parsers — Which Library Speaks Which YAML

"Valid YAML" is not a property of a file; it is a relation between a file and a library. Pin the library before arguing about the spec.

**Contents:** [The Matrix](#the-matrix) · [Python](#python) · [Go](#go) · [JavaScript and TypeScript](#javascript-and-typescript) · [Java](#java) · [Ruby, Rust, PHP, .NET](#ruby-rust-php-net) · [CLI Parsers](#cli-parsers) · [Emitter Settings That Change the File](#emitter-settings-that-change-the-file) · [Performance and Size](#performance-and-size) · [Choosing a Library](#choosing-a-library)

**Before writing a file for a specific consumer**, read `## Toolchain` in `~/Clawic/data/yaml/memory.md` — the library, its version and its resolved quirks for this user's projects are recorded there, and re-deriving them costs a test cycle each time.

## The Matrix

| Library | Spec | Bools `yes/no/on/off` | Octal `0644` | Sexagesimal | Merge `<<` | Duplicate keys | Comments on round-trip |
|---|---|---|---|---|---|---|---|
| PyYAML | 1.1 | bool | 420 | yes | yes | last wins | lost |
| ruamel.yaml (default 1.2) | 1.2 | string | 644 | no | yes | error (round-trip) | **preserved** |
| ruamel.yaml (`version=(1,1)`) | 1.1 | bool | 420 | yes | yes | error | preserved |
| go-yaml v2 | 1.1 | bool | 420 | yes | yes | last wins | lost |
| go-yaml v3 | 1.1/1.2 mix | bool | 420 | no | yes | **error** | partially (`yaml.Node`) |
| js-yaml v4 | 1.2 | string | 644 | no | yes | error | lost |
| `yaml` (eemeli, JS) | 1.1/1.2 selectable | per version | per version | per version | yes | configurable | **preserved** (CST) |
| SnakeYAML 1.x | 1.1 | bool | 420 | yes | yes | error (recent) | lost |
| SnakeYAML Engine | 1.2 | string | 644 | no | yes | error | lost |
| Ruby Psych | 1.1 | bool | 420 | yes | yes | last wins | lost |
| serde_yaml / yaml-rust | 1.2-ish | string | 644 | no | yes (serde_yaml) | error | lost |
| YamlDotNet | 1.2-ish | bool (configurable) | varies | no | yes | error | partially |

Treat any cell as a claim to verify on the exact version in use: `python3 -c "import yaml;print(yaml.safe_load(open('f.yaml')))"` settles an argument faster than a changelog.

## Python

- `yaml.safe_load` / `safe_load_all` — the default for everything. `yaml.load(s)` without a `Loader` raises `TypeError` in PyYAML 6.0; older versions warned. `FullLoader` still constructs arbitrary Python types and is not a security boundary.
- `yaml.dump(data, sort_keys=False, default_flow_style=False, width=<max_line_width>, allow_unicode=True)` — the four arguments that stop a dump from mangling a human's file. Default `sort_keys=True` alphabetizes every mapping.
- `CSafeLoader`/`CSafeDumper` (libyaml bindings) are roughly an order of magnitude faster: `from yaml import CSafeLoader as Loader` behind a try/except ImportError.
- `ruamel.yaml` for anything that writes back a file a human owns: `YAML(typ='rt')` preserves comments, key order, quote style, anchors and block-scalar style. Slower and stricter — it errors on duplicate keys.
- PyYAML never emits block scalars for multiline strings unless you register a representer; ruamel does.

## Go

- `sigs.k8s.io/yaml` converts YAML→JSON and then uses `encoding/json`, so **JSON struct tags apply and YAML-only features are dropped**. This is what Kubernetes uses; it explains why `json:"name"` tags work on manifests and why anchors never appear in stored objects.
- `gopkg.in/yaml.v3` is the general-purpose choice: duplicate-key errors, `yaml.Node` for position and comment access, and `KnownFields(true)` on a decoder to reject unknown keys (the schema check most Go configs are missing).
- v3 emits with a line-wrap around 80 columns and there is no exported width setting — long values arrive folded. If byte-stability matters, emit with a literal block or post-process.
- v2 is still widespread in older code; it differs on duplicate keys and on `omitempty` semantics.

## JavaScript and TypeScript

- `js-yaml` v4: `load()` is safe (the `safeLoad` alias was removed, `load` no longer supports arbitrary types by default). `DEFAULT_SCHEMA` covers standard tags; `CORE_SCHEMA` and `JSON_SCHEMA` are stricter. Duplicate keys throw unless `json: true`.
- `yaml` (eemeli): a full CST, so it can edit a document without losing anything, and it lets you select 1.1 or 1.2 explicitly. The right pick for tooling that rewrites user files.
- `js-yaml` `dump()` options that matter: `lineWidth: -1` disables wrapping entirely, `noRefs: true` refuses to emit anchors for shared objects, `quotingType`/`forceQuotes` control style.
- Node's built-in JSON round-trip is not a substitute: it loses comments and reorders nothing but changes everything else.

## Java

- SnakeYAML **≥2.0 defaults to `SafeConstructor`**; 1.x defaulted to a constructor that instantiates arbitrary classes, which is the root of a long CVE list including Spring and Jenkins incidents. `new Yaml()` on 1.x with untrusted input is remote code execution (`security.md`).
- SnakeYAML Engine is the 1.2 implementation and a separate artifact — moving to it changes bool and octal resolution, so it is a data migration, not a dependency bump.
- Jackson's `jackson-dataformat-yaml` wraps SnakeYAML and applies Jackson's binding rules on top; `YAMLGenerator.Feature.MINIMIZE_QUOTES` and `LITERAL_BLOCK_STYLE` control output shape.

## Ruby, Rust, PHP, .NET

- **Psych 4** (Ruby 3.1+) made `YAML.load` safe by default and introduced `YAML.unsafe_load`. Rails apps that broke on upgrade were relying on aliases: `YAML.load(..., aliases: true)` re-enables them.
- **serde_yaml** maps to Rust types with serde; unknown fields are ignored unless `#[serde(deny_unknown_fields)]`.
- **PHP** `yaml_parse` (libyaml ext) vs Symfony's pure-PHP parser: Symfony's is 1.1-ish with its own extensions and its own quirks around `!php/const`.
- **YamlDotNet**: naming conventions are explicit (`CamelCaseNamingConvention`), and the deserializer must be told to ignore unmatched properties or it throws.

## CLI Parsers

| Tool | Engine | Notes |
|---|---|---|
| `yq` (mikefarah, Go) | go-yaml v3 | jq-like syntax, preserves comments and anchors, `-i` in place |
| `yq` (kislyuk, Python) | PyYAML + jq | Wraps jq — **entirely different syntax**, converts through JSON, loses comments |
| `dasel` | multiple | One selector language across YAML/JSON/TOML |
| `yamllint` | PyYAML | Lints style and some semantics; 1.1 resolution (`schemas.md`) |
| `dyff` | go-yaml | Semantic diff for YAML documents |
| `kubectl` | sigs.k8s.io/yaml | YAML→JSON, so schema errors and parse errors read differently (`kubernetes.md`) |

`yq_flavor` in `config.yaml` decides which `yq` examples are written in. Getting this wrong produces commands that fail with confusing syntax errors on the other tool.

## Emitter Settings That Change the File

Every generator ships defaults that rewrite a human's file. Set these explicitly:

| Setting | Bad default | Set to |
|---|---|---|
| Key sorting | PyYAML sorts alphabetically | `sort_keys=False` |
| Line width | ~80 in PyYAML and go-yaml v3 | `max_line_width`, or `-1`/unlimited in js-yaml |
| Flow style | PyYAML emits `{a: 1}` for small maps | `default_flow_style=False` |
| Unicode | escaped as `\uXXXX` | `allow_unicode=True` |
| Anchors | emitted automatically for shared objects | `noRefs`/deep-copy before dumping, unless anchors are wanted |
| Indent | 2, but sequences unindented | Match `indent_width` and `sequence_indent` |
| Explicit start | no `---` | Per the repo convention |
| Multiline strings | one escaped line | Register a literal-block representer |

## Performance and Size

- Pure-Python PyYAML parses roughly 10× slower than the libyaml-backed loader; on a 50 MB file that is minutes versus seconds.
- YAML has no random access. A large file is parsed whole — the only streaming unit is the *document*, so a multi-document stream can be processed with `safe_load_all` one document at a time and constant memory.
- Above roughly 10 MB, or above a few thousand documents, YAML is the wrong container: use NDJSON or a database and generate YAML at the edge (`config-design.md`).
- Anchors expand on serialization, so output size can exceed input size by orders of magnitude (`anchors.md`).

## Choosing a Library

| Job | Pick |
|---|---|
| Read config in an app | The stdlib-adjacent safe loader for the language |
| Edit a file a human owns | ruamel round-trip (Python), `yaml`/eemeli (JS), `yq -i` (CLI) |
| Generate files from data | Any emitter, with the settings table above applied |
| Validate | The consumer's own validator plus a JSON Schema (`schemas.md`) |
| Parse untrusted input | Safe loader + size cap + timeout (`security.md`) |
| Anything Kubernetes-shaped | `sigs.k8s.io/yaml` so struct tags and behavior match the API server |

**After establishing which library and version a project uses** — or after any behavior above turns out to differ on the installed version — write or update its row in `## Toolchain` of `~/Clawic/data/yaml/memory.md`: project, library, version, spec version, and the quirk that was observed (`memory-template.md`). This is the fact that decides every quoting question afterwards, and it is invisible from the YAML file itself.
