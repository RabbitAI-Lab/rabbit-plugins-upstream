# Security — Untrusted Input, Deserialization, and Secrets in Files

Two independent risks. Parsing a file someone else wrote can execute code or exhaust memory. Writing a file yourself can leak a credential into version control. The mitigations share nothing.

**Contents:** [Deserialization: the Loader Is the Vulnerability](#deserialization-the-loader-is-the-vulnerability) · [Alias Expansion Bombs](#alias-expansion-bombs) · [Other Resource Attacks](#other-resource-attacks) · [Hardening a Parser](#hardening-a-parser) · [Secrets in YAML Files](#secrets-in-yaml-files) · [Base64 Is Not Encryption](#base64-is-not-encryption) · [Encrypted-at-Rest Options](#encrypted-at-rest-options) · [Leak Response](#leak-response) · [What Never Goes Into the Data Folder](#what-never-goes-into-the-data-folder)

**Before choosing a loader policy or an encryption approach**, read `## Config Files`, `## Due` and `## Boxes` in `~/Clawic/data/yaml/memory.md`, and `loader_policy` in `config.yaml` — the file rows say how secrets are already handled where you are about to edit, and a second encryption scheme in the same repo is how a key ends up unrotatable.

## Deserialization: the Loader Is the Vulnerability

YAML's tag mechanism lets a document name a type to construct. A loader that honors arbitrary tags will instantiate arbitrary classes — that is remote code execution from a config file.

| Runtime | Unsafe | Safe | Notes |
|---|---|---|---|
| Python | `yaml.load(s, Loader=yaml.UnsafeLoader\|FullLoader)` | `yaml.safe_load(s)` | `yaml.load` without `Loader=` raises in PyYAML 6.0; `FullLoader` is not a security boundary |
| Java | `new Yaml()` on SnakeYAML 1.x | SnakeYAML ≥2.0 default, or `new Yaml(new SafeConstructor())` | The 1.x default has driven a long CVE list across Spring, Jenkins and Kafka Connect |
| JavaScript | `js-yaml` v3 `load` | `js-yaml` v4 `load` (safe by default) | v3's `safeLoad` was the safe one; v4 renamed it and removed the unsafe default |
| Ruby | `YAML.unsafe_load`, Psych <4 `YAML.load` | Psych 4 `YAML.load` | Aliases are also off by default in Psych 4: `aliases: true` to re-enable |
| Go | — | `gopkg.in/yaml.v3` | No object construction from tags; Go's exposure is resource exhaustion, not RCE |
| PHP | `yaml_parse` with `!php/object` support | Disable the object callback | Symfony: `Yaml::parse` without `PARSE_OBJECT` flags |

The payload shapes to recognize in a file review: `!!python/object/apply:os.system`, `!!python/name:`, `!!javax.script.ScriptEngineManager`, `!ruby/object:`, `!php/object`. Any of them in a file from outside means the file is an exploit attempt, not a config.

`loader_policy: safe-only` (the default) means no full-tag loader is ever emitted, including in examples, and a request to parse `!!python/`-tagged content gets the unsafe-by-design answer plus this file's alternative: a schema and a plain-data parse.

## Alias Expansion Bombs

A safe loader still expands aliases. Nested anchors multiply:

```yaml
a: &a ["x","x","x","x","x","x","x","x","x"]
b: &b [*a,*a,*a,*a,*a,*a,*a,*a,*a]
c: &c [*b,*b,*b,*b,*b,*b,*b,*b,*b]
# nine levels ≈ 9^9 ≈ 387 million leaf nodes from a few hundred bytes
```

- Formula: with a branching factor `k` and `n` levels, the expansion is `k^n` nodes. At `k=9`, level 8 is 43 million and level 9 is 387 million — the cliff between "slow" and "the process dies" is one line of text.
- This is the shape behind CVE-2019-11253 (Kubernetes API server). Some parsers now bound it — go-yaml v3 limits alias expansion, and js-yaml has depth protections. PyYAML does not.
- `safe_load` does **not** protect against it. Nothing in the "safe loader" concept addresses size.

## Other Resource Attacks

- **Deep nesting**: thousands of nested `[[[[…]]]]` can blow the parser's recursion stack; some parsers segfault rather than raise.
- **Huge scalars**: a single 500 MB block scalar is legal YAML and is loaded into memory whole.
- **Enormous key counts**: a mapping with millions of keys costs the language's dict overhead, not the file size.
- **Timestamp/regex resolution** is linear and not an attack surface; the resolver is not backtracking.

## Hardening a Parser

For any input the user did not write, in order of value:

1. Safe loader (table above). Non-negotiable.
2. **Size cap before parsing**: read at most N bytes and reject a larger input. A 1 MB cap covers every legitimate config and stops most bombs.
3. **Timeout / memory limit** around the parse call — a subprocess with `RLIMIT_AS`, a worker with a deadline. This is what actually catches expansion bombs on parsers that do not bound aliases.
4. **Reject aliases entirely** where the input format does not need them: pre-scan for `*` anchors references, or use a parser flag (Psych `aliases: false`, js-yaml custom schema).
5. **Schema validation immediately after parse** (`schemas.md`) — a bomb-free document with unexpected keys is still hostile input.
6. Never `eval`, `!include`, or path-resolve anything the document names: a `!include /etc/passwd`-style custom tag is a file-read primitive.

## Secrets in YAML Files

YAML is where secrets get pasted, because it is where configuration lives and because a `|` block accepts a PEM key without complaint.

**Is a secret — never in a file that is committed, never in `~/Clawic/data/`:** passwords, API keys and tokens, private keys and their passphrases, PEM blocks, `.pem`/`.p12` contents, connection strings containing a password, kubeconfig `client-key-data` and `token`, Kubernetes Secret `data:`/`stringData:` values, `.dockerconfigjson`, webhook URLs with an embedded token, session cookies, TLS certificate *keys* (the certificate itself is public), `sts:ExternalId`, signing keys.

**Is not a secret — keep it, redacting it makes the file useless:** file paths, key names, environment variable *names*, schema URLs, image and chart names, namespaces, cluster and context names, account ids and ARNs, hostnames, port numbers, anchor names, parser and library versions, yamllint rule ids, public certificates and CA bundles, base64 of *non-secret* data.

The pointer scheme, used in the exact position the value would occupy: `env:DB_PASSWORD` · `keychain:prod-tls` · `1password:Work/Cluster/kubeconfig` · `vault:secret/data/prod#password` · `sops:secrets/prod.enc.yaml` · `ssm:/prod/db/password` · `file:~/.ssh/id_ed25519` · `profile:prod`. In a document: `password: <ssm:/prod/db/password>`.

When the user pastes YAML to be saved, replace every secret value with its pointer **before** writing anything, and say in one line that you did.

## Base64 Is Not Encryption

A Kubernetes Secret's `data:` is base64. `base64 -d` reverses it in one command with no key. Consequences:

- A Secret manifest in git is a plaintext credential in git, forever, including in every fork and every CI cache.
- `stringData:` is the same thing without the encoding step — more honest, equally exposed.
- Secrets are stored base64 in etcd too; encryption at rest is a separate cluster setting (`EncryptionConfiguration`).
- The only safe forms in a repo are encrypted or referenced, below.

## Encrypted-at-Rest Options

| Approach | How it works | Fits |
|---|---|---|
| **sops** | Encrypts *values*, leaves keys and structure readable; keys from age, KMS, GCP KMS, Vault | Any YAML in git; diffs stay meaningful because only values change |
| **Sealed Secrets** | Controller-decryptable ciphertext, one-way from the developer's side | Kubernetes only |
| **External Secrets Operator / CSI driver** | Manifest holds a *reference*; the value never enters git | Kubernetes, when a secret manager already exists |
| **git-crypt / transparent encryption** | Whole-file encryption on commit | Small teams; whole-file diffs become opaque |
| **Env var at deploy time** | The YAML holds `${VAR}` and the platform substitutes | Simplest; the value lives in the platform's secret store |
| **Plain, gitignored** | `.env`, `values.local.yaml` in `.gitignore` | Local development only, and one `git add -f` from disaster |

sops is the default recommendation for YAML specifically: it is format-aware, so a review still shows which keys changed.

## Leak Response

When a secret is found committed in a YAML file:

1. **Rotate first.** The credential is compromised from the moment it was pushed; history rewriting is cleanup, not containment.
2. Remove it from the current file and replace with a reference.
3. Purge history only if the repository is private and small enough to force-push safely (`git filter-repo`); assume public history is permanently public.
4. Check the derived copies: CI caches, container images that COPYed the file, backups, the pasted copy in chat.
5. Add the secret scanner to CI so the next one fails the build (`schemas.md`).

## What Never Goes Into the Data Folder

Nothing under `~/Clawic/data/` ever holds a secret value — not the files this skill names, not files created later, not text the user pastes in and asks to keep. This applies to the whole folder, permanently, and it is enforced at write time: strip, then store the pointer.

The domain-specific hazard: **a PEM key or a Kubernetes Secret pasted as a block scalar while asking "why does this not parse?"**. The answer is about chomping (`multiline.md`); the payload never gets written down. Store the shape with `<file:~/.ssh/id_ed25519>` in place of the body.

**After hardening a parse path, adopting an encryption approach, or responding to a leak**, write it down: the approach and its key-management shape go to `~/Clawic/data/yaml/artifacts/<kebab-name>.md` with its `## Boxes` line (references only, never material), the affected files get their `## Config Files` rows updated with how secrets are handled there, and a scanning or rotation cadence becomes a row in `## Due` of `memory.md` (`memory-template.md`).
