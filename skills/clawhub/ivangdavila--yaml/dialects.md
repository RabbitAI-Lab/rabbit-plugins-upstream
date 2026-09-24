# Dialects — Tool-Specific YAML

Several ecosystems layer local tags, a templating language, or their own merge semantics on top of YAML. A generic parser is *wrong* about these files, and so is a generic linter. This file is the per-tool delta. Kubernetes and CI have their own files (`kubernetes.md`, `pipelines.md`).

**Contents:** [Ansible](#ansible) · [Docker Compose](#docker-compose) · [CloudFormation and SAM](#cloudformation-and-sam) · [OpenAPI](#openapi) · [Home Assistant](#home-assistant) · [cloud-init and netplan](#cloud-init-and-netplan) · [Rails, Symfony, Spring](#rails-symfony-spring) · [Others Worth Recognizing](#others-worth-recognizing) · [Handling Local Tags Generically](#handling-local-tags-generically)

**Before touching a tool-specific file**, read `## Config Files` in `~/Clawic/data/yaml/memory.md` — the row names the consumer and its validator, which is the only way to know whether the file's odd syntax is a bug or the dialect.

## Ansible

- **Jinja at the start of a value must be quoted**: `msg: {{ var }}` is a flow mapping and a parse error; `msg: "{{ var }}"` is correct. Mid-value (`msg: hello {{ var }}`) parses, and Ansible still recommends quoting for consistency.
- Templating happens after YAML parsing, so `when: ansible_os_family == "Debian"` is a *string* that Ansible evaluates — quoting the whole thing is safe, and `when: "{{ x }}"` is redundant (`when` is already an expression context).
- Booleans: Ansible accepts `yes/no/true/false`; the project's style guide standardizes on `true`/`false` since ansible-lint 6. `mode: 0644` must be `"0644"` or symbolic `u=rw,g=r,o=r` — unquoted it is octal-resolved and lands as 420, which happens to be right on a 1.1 parser and wrong everywhere else (`types.md`).
- Vault: `!vault |` is a local tag holding ciphertext. Never decrypt into a file, never store the plaintext (`security.md`).
- `ansible-lint` knows every module's argument schema — it is a schema validator, not just a style linter. What the playbook *means* is the `ansible` skill.

## Docker Compose

- **Ports must be quoted**: `- 22:22` is sexagesimal 1342 on a 1.1 parser. `- "22:22"` always (Rule 2). Long syntax (`- {target: 22, published: 22}`) sidesteps it entirely.
- Environment values: both `KEY=value` list form and `KEY: value` map form are accepted; the map form coerces `true`, `no` and numbers, and Compose then requires strings — quote them.
- `x-` prefixed top-level keys are reserved for extensions and ignored by the validator: the correct home for anchor blocks (`anchors.md`).
- Multiple `-f` files merge with later winning; lists are replaced, not appended, except a few documented fields. `docker compose config` prints the merged result and is the fastest debugging tool in this dialect.
- `${VAR}` and `${VAR:-default}` are Compose's own interpolation, resolved after parsing; `$$` escapes a literal `$` for the container's shell.
- Version-like values (`image: postgres:16.1`) are inside a string already; a bare `16.1` anywhere else is a float.

## CloudFormation and SAM

- Short-form intrinsics are **local tags**: `!Ref`, `!GetAtt`, `!Sub`, `!If`, `!Join`, `!FindInMap`. A generic parser raises `could not determine a constructor for the tag '!Ref'`.
- They cannot nest directly: two short forms in a row is a tag applied to a tag. The inner one takes its long form — `Ref:` for `!Ref` (there is no `Fn::Ref`; only `Fn::GetAtt`, `Fn::Sub`, `Fn::Join`, `Fn::If`, `Fn::FindInMap` carry the prefix). Inside `!Sub` the idiomatic move is neither: interpolate with `${Resource}` and `${Resource.Attribute}` directly in the string.
- `!Sub "${AWS::Region}"` needs quotes — `${` at the start would be fine, but `{` inside an unquoted scalar in flow context is not, and consistency beats memorizing the exception.
- `cfn-lint` registers the tags and validates resource properties. `yamllint` on a template flags nothing useful and misses everything important.
- JSON and YAML templates are interchangeable; the YAML form exists mainly for comments and short-form tags.

## OpenAPI

- The spec mandates YAML 1.2 for OpenAPI 3.x documents, so `yes`/`no` stay strings and `0644` is decimal — one of the few ecosystems where the 1.2 column is guaranteed.
- Keys that bite: `in: query`, `on` is not used, but `true`/`false` as *example values* need care — an example for a string field written as `example: yes` becomes a bool and fails schema validation.
- `$ref` is JSON Reference, not YAML: `$ref: '#/components/schemas/User'` must be quoted because it starts with `#` (comment) or `'#/...'`. External refs (`./common.yaml#/X`) are resolved by the tool, not the parser.
- Multi-file specs are assembled by the tooling (`redocly bundle`, `swagger-cli bundle`); anchors do not cross files.
- Validate with `spectral lint` (style + schema) or `redocly lint`.

## Home Assistant

- Local tags everywhere: `!include`, `!include_dir_merge_list`, `!include_dir_named`, `!secret`, `!env_var`. Only Home Assistant's own loader implements them; `yamllint` handles them (it does not construct) but a generic `safe_load` fails.
- `!secret name` reads from `secrets.yaml`, which stays out of version control. That file is the credential store — never copy its values anywhere (`security.md`).
- Entity ids are strings with dots (`sensor.living_room_temp`) and are safe unquoted; times (`06:30`) are not — quote them.
- `automation.yaml` and friends are rewritten by the UI editor, which strips every comment. Files edited in the UI must not carry comments you care about; keep hand-written config in `!include`d files the UI does not touch.
- A device configured this way belongs in the shared box: write its row to `~/Clawic/data/devices/devices.md` (protocol in `memory-template.md`), not into this skill's memory.

## cloud-init and netplan

- **cloud-init**: the first line must be exactly `#cloud-config`. It looks like a comment and is a required magic header — a blank line or a BOM before it silently disables the whole file (`strings.md`).
- `write_files.permissions` takes a *string*: `'0644'`. `content` uses a `|` block; a trailing-newline mistake corrupts scripts (`multiline.md`).
- `runcmd` entries are either a string (shell) or a list (exec form) — the list form avoids shell quoting entirely.
- **netplan**: strictly indentation-sensitive, and `dhcp4: no` is a bool that works on its 1.1 parser. Apply with `netplan try` (auto-reverts) rather than `netplan apply` on a remote host — a YAML mistake here removes your network.
- Both are consumed once at boot; the failure mode is a machine that came up wrong, with the error only in the instance log. Validate before the instance exists (`cloud-init schema --config-file`).

## Rails, Symfony, Spring

- **Rails** `database.yml`, `secrets.yml`, locale files: ERB is allowed inside (`<%= ENV['X'] %>`) and is processed before YAML, so the file is a template. Aliases are disabled by default since Psych 4 — `YAML.load(..., aliases: true)` or `ActiveSupport`'s loader (`parsers.md`).
- Rails locale files are deep-nested maps where a missing key silently falls back — schema validation is worth it above a few hundred keys.
- **Symfony**: its own parser with `!php/const`, `!php/enum` tags and a documented subset of YAML; `%parameter%` and `@service` references are Symfony's, not YAML's — `@` at the start of a value needs quotes.
- **Spring Boot** `application.yml`: relaxed binding maps `my-prop`, `myProp` and `MY_PROP` to the same property, profiles are separated by `---` inside one file with `spring.config.activate.on-profile`, and a duplicated key across profile documents is legal and intentional. Unquoted `on`/`off` values resolve to booleans through SnakeYAML 1.1.

## Others Worth Recognizing

| Tool | Dialect note |
|---|---|
| Swagger 2.0 | Predates the 1.2 mandate; treat as 1.1 and quote defensively |
| Prometheus / Alertmanager | Durations are strings (`5m`); PromQL in `expr:` needs `\|` blocks or quoting for `{`, and `$labels` templating survives as text |
| Grafana provisioning | JSON dashboards embedded as strings — use `\|` blocks |
| Serverless Framework | `${self:…}`, `${env:…}` interpolation; `{` at value start needs quotes |
| Renovate / Dependabot | Schema Store schemas exist; bind them and let the editor validate |
| ESPHome | Local tags plus substitutions; devices belong in the shared `devices/` box |
| OpenAPI-adjacent (AsyncAPI, JSON Schema in YAML) | Same `$ref` quoting rule |
| SnakeYAML-based Java apps generally | 1.1 resolution, so `no` is false in every `application.yml` |

## Handling Local Tags Generically

When you must parse a dialect file with a generic parser — for a bulk edit, a grep, a migration:

1. Best: use the tool's own parser or CLI (`cfn-lint`, `docker compose config`, `helm template`, `ansible-inventory --list`). It is always available and always correct.
2. `yq` handles unknown tags by preserving them as-is in place, which makes it safe for in-place edits of CloudFormation and Home Assistant files.
3. Python fallback: register a catch-all so the tags survive as opaque nodes —
   `SafeLoader.add_multi_constructor("!", lambda loader, suffix, node: None)` — this loses the values, so use it only for structural checks, never to rewrite the file.
4. Never strip a tag to make a parser happy: the tag is the semantics.

**When a dialect quirk is diagnosed or a tool-specific file becomes part of the user's setup**, add or update its row in `## Config Files` of `~/Clawic/data/yaml/memory.md` (path, tool, spec version, validator, whether it is templated or rewritten by the tool), and put the trap itself in `## Gotchas Hit` with the verbatim error (`memory-template.md`). Devices configured through these files go to the shared `~/Clawic/data/devices/devices.md`, one row per device, updated in place — never duplicated here.
