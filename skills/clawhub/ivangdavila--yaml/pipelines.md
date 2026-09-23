# CI Pipelines — Workflow Files That Parse and Mean What You Wrote

CI files are the densest concentration of YAML traps in practice: every one of them mixes a templating language, embedded shell, and implicit typing, and the feedback loop is a push. What the pipelines *do* belongs to `github-actions`, `gitlab` and `ci-cd`; this is the YAML underneath.

**Contents:** [GitHub Actions](#github-actions) · [GitLab CI](#gitlab-ci) · [CircleCI](#circleci) · [Azure Pipelines](#azure-pipelines) · [Argo, Tekton, Jenkins](#argo-tekton-jenkins) · [Embedded Shell in Every Provider](#embedded-shell-in-every-provider) · [Validate Before Pushing](#validate-before-pushing)

**Before editing a pipeline that already runs**, read `## Config Files` and `## Gotchas Hit` in `~/Clawic/data/yaml/memory.md` — a workflow that once broke on a quoting rule usually breaks on it again, and the row says which one.

## GitHub Actions

| Trap | What happens | Fix |
|---|---|---|
| `on:` as a key | A YAML 1.1 parser resolves the key to boolean `true`, so `yq '.on'` returns nothing and yamllint's `truthy` rule flags it. GitHub's own parser keeps it as the string `on`, which is why the workflow runs anyway | Quote it (`"on":`) if any of your tooling reads the file, and enable `truthy: {check-keys: true}` to be told |
| `${{ }}` at the start of a value | `{` opens a flow mapping → `could not find expected ':'` | Quote the whole value: `if: ${{ … }}` is legal because `if:` values are expressions, but any other field needs `key: "${{ … }}"` |
| A string `false` reaching `if:` | `if:` is evaluated as an expression even without `${{ }}`, so `if: false` and `if: "false"` both skip — the YAML quotes change nothing. What is truthy is a *string* inside the expression: `if: ${{ 'false' }}` and `if: ${{ inputs.enabled }}` with a string input `'false'` both run | Compare explicitly: `if: inputs.enabled == 'true'`, and declare the input `type: boolean` |
| Multiline `run:` with `>` | Commands joined by spaces; a `#` comment then swallows the rest of the line | `run: \|` always |
| Cron schedule unquoted | `- cron: 0 3 * * *` parses fine (a `*` mid-scalar is ordinary text), but `- cron: */5 * * * *` does not: a leading `*` is the alias indicator → `while scanning an alias`. The schedule that breaks is the one you edit it into | Quote every cron unconditionally: `- cron: "0 3 * * *"` |
| Version numbers in `with:` | `node-version: 18.10` → 18.1 | `node-version: "18.10"` |
| `env:` values | Numbers and bools become non-strings, then get stringified inconsistently | Quote every `env` value |
| Matrix values like `3.10` | Float 3.1 — Python 3.10 becomes Python 3.1 | `"3.10"`, always quoted |
| Empty `with:` or `env:` | Renders as `null`, and the action receives nothing rather than defaults | Omit the key entirely |

- Reuse: YAML anchors are legal in the file but GitHub gives no cross-file YAML mechanism. Use reusable workflows (`workflow_call`) or composite actions; a matrix replaces most copy-paste.
- `actionlint` validates expressions, shell inside `run:`, and action inputs — the only tool that checks all three.
- Bind the Schema Store schema for editor errors: `# yaml-language-server: $schema=https://json.schemastore.org/github-workflow.json` (`schemas.md`).

## GitLab CI

| Trap | What happens | Fix |
|---|---|---|
| Anchors across `include:` | Anchors are file-scoped; an anchor in an included file is invisible | `extends:` — it resolves after includes and deep-merges |
| `extends` vs `<<:` | `<<` is a shallow YAML merge; `extends` merges recursively and understands job semantics | Prefer `extends` for jobs, anchors only for small scalar reuse |
| `script:` entries with a colon | `- echo Note: this` → mapping-values error | Quote the whole command |
| `rules:` `if:` expressions | Contain `$VAR == "x"` — the `"` inside an unquoted scalar is fine, but `$VAR` at the start of a value with `{` is not | Quote the expression |
| `variables:` typed | Values must be strings; GitLab coerces, other tools do not | Quote everything |
| `only`/`except` vs `rules` | Mixing both in one job is a config error | Migrate to `rules` |
| Hidden jobs | A job key not starting with `.` is a real job — a template job must be `.template` | Prefix with `.` |
| `!reference [.job, script]` | GitLab-specific local tag; a generic YAML parser cannot construct it | Lint with GitLab's own CI Lint, not a plain parser (`dialects.md`) |

`glab ci lint` (or the project's CI Lint page) is authoritative because it resolves `include:`, `extends:` and `!reference` — no offline parser can.

## CircleCI

- Anchors and merge keys work and are idiomatic here: one file, one parser, no includes.
- `circleci config validate` resolves orbs and expands the config; `circleci config process` prints the expanded result, which is what actually runs.
- Parameters are typed (`type: string|integer|boolean|enum`), so a quoting mistake gives a real error at validate time rather than at runtime.
- Version pinning: orb versions are strings — `circleci/node@5.0` is fine inside the reference, but a bare `5.0` value elsewhere is a float.

## Azure Pipelines

- Two expression syntaxes with different timing: `${{ }}` at compile time, `$[ ]` at runtime, `$( )` in scripts. Any of them at the start of a value needs quotes.
- `${{ if … }}` blocks are template directives that generate YAML — the file is a template first and YAML second, like Helm (`kubernetes.md`).
- Templates are included with `template:` and parameters are typed; that typing is the only validation available offline.
- Preview the expansion: the "Validate and preview YAML" endpoint or the pipeline run's expanded YAML tab.

## Argo, Tekton, Jenkins

- **Argo Workflows / Argo CD**: Kubernetes CRDs, so everything in `kubernetes.md` applies. Argo's `{{workflow.parameters.x}}` templating is resolved by the controller *after* the YAML parses, so it must survive as a quoted string.
- **Tekton**: same shape; `$(params.foo)` is a string, and the `script:` field is a literal block whose first line should be a shebang.
- **Jenkins**: `Jenkinsfile` is Groovy, not YAML; JCasC (`jenkins.yaml`) is YAML and takes plain configuration — its trap is that a wrong key is silently ignored, so schema-validate it.
- **Drone, Woodpecker, Buildkite**: multi-document YAML pipelines; the `---` separator rules from `kubernetes.md` apply, including the block-scalar hazard.

## Embedded Shell in Every Provider

The shared failure across all of them: a shell script inside YAML inside a runner.

- Always `|` (literal), never `>` — folding turns a script into one line and any `#` comment eats the remainder (Rule 5).
- Start with `set -euo pipefail`. YAML has nothing to do with it, and it is why half of "the pipeline passed but did nothing" reports exist.
- Two levels of variable expansion: the CI's templating runs first and the shell's second. `$VAR` may be substituted before the shell ever sees it — escape per the provider (`$$VAR`, `\$VAR`, or single quotes) when the shell should own it.
- Secrets in `run:` blocks end up in logs unless the provider masks them; masking works on exact values, not on values that were transformed (base64'd, echoed in parts).
- Long one-liners: prefer a checked-in script file called from the workflow. It is testable locally, lintable with shellcheck, and diffable.

## Validate Before Pushing

1. `yamllint -s .github/ .gitlab-ci.yml` — catches tabs, duplicates, truthy keys
2. The provider's own linter: `actionlint`, `glab ci lint`, `circleci config validate`, Azure's preview endpoint
3. Schema binding in the editor so the next edit is checked as it is typed
4. For anything with includes or templates, print the **expanded** config and read it — that is the file that runs

**When a pipeline trap is diagnosed or a workflow layout is settled**, write it down: the trap goes as one row in `## Gotchas Hit` of `~/Clawic/data/yaml/memory.md` with the verbatim error, the workflow file gets or updates its row in `## Config Files` (provider, validator, whether it is templated), and a reusable layout worth copying goes to `~/Clawic/data/yaml/artifacts/<kebab-name>.md` with its `## Boxes` line (`memory-template.md`). Never copy a workflow's secret values or masked variables into either.
