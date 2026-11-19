# vibecheck

**Audit AI-generated code before it ships.**

`vibecheck` scores a codebase from 0 to 100 for "vibe": it finds security holes, common anti-patterns, and the kind of AI slop that passes review because it looks plausible. Zero dependencies, plain Python 3.8+.

> Anyone can vibe code. Shipping vibe-coded code without an audit is a different sport.

## Why

- AI-generated code is full of hardcoded secrets, `eval()`, swallowed exceptions, and string-built SQL.
- Experienced reviewers rarely complain that AI "gets algorithms wrong" — they complain about **security and quality**.
- `vibecheck` is one command, a few seconds, and an answer to "is this shippable?".

## Install

### ClawHub

```bash
clawhub install thiennhant95/vibecheck
```

### From source

Nothing to install — only Python 3.8+:

```bash
git clone https://github.com/thiennhant95/vibecheck && cd vibecheck
python3 vibecheck.py --help
```

Or copy the single `vibecheck.py` file into your project.

## Usage

```bash
python3 vibecheck.py ./src                              # scan a directory
python3 vibecheck.py app.py                             # scan one file
python3 vibecheck.py ./src --format md > report.md      # Markdown (PR comment)
python3 vibecheck.py ./src --format json                # JSON
python3 vibecheck.py ./src --format sarif > out.sarif   # GitHub code scanning
python3 vibecheck.py ./src --min-score 80 --fail-on high  # CI gate
python3 vibecheck.py . --exclude "tests" --exclude "generated"

# Legacy adoption: record known findings, fail only on new ones
python3 vibecheck.py ./src --write-baseline .vibecheck-baseline.json
python3 vibecheck.py ./src --baseline .vibecheck-baseline.json
```

**Exit codes:** `0` pass · `1` fail (below `--min-score` or a blocking finding) · `2` bad input.

### Scoring caps

A good score can never hide a security finding:

| Open finding | Score capped at | Verdict |
|---|---|---|
| CRITICAL | 30 | DANGER — do not ship |
| HIGH | 69 | RISKY — fix before merge |

So a single disabled TLS check or SQL injection can never be reported as "production ready".

### Verdicts

| Score | Verdict |
|---|---|
| 90–100 | CLEAN — production ready |
| 70–89 | OK — minor cleanup needed |
| 50–69 | RISKY — fix before merge |
| < 50 | DANGER — do not ship |

## Rules

18 rules across three scopes. `raw` rules inspect the whole text (secrets and SQL live inside strings), `code` rules inspect code only (strings and comments are masked), and `comment` rules inspect comments only.

| Rule | Severity | Detects |
|---|---|---|
| `private-key` | critical | Private key committed in source |
| `secret-aws` | critical | AWS access key id in source |
| `secret-token` | high | OpenAI/GitHub/Slack/Google token in source |
| `secret-assignment` | high | Hardcoded password/secret assignment |
| `env-secret` | high | Real secret in a `.env` file (quoted or not) |
| `sql-injection` | high | SQL built by f-string, `.format`, `%`, or concatenation |
| `eval-exec` | high | `eval`/`exec` calls (direct, aliased, or `builtins.*`) |
| `js-eval` | high | `eval` / `new Function` in JS/TS |
| `shell-true` | high | `subprocess` with `shell=True` (including via a boolean variable) |
| `os-shell` | high | `os.system` / `os.popen` |
| `verify-false` | high | TLS verification disabled (including via a variable) |
| `cors-wildcard` | medium | CORS allows every origin |
| `weak-hash` | medium | MD5/SHA1 used for security |
| `pickle-load` | medium | Unsafe deserialization via `pickle` |
| `yaml-unsafe-load` | medium | `yaml.load` without a safe loader |
| `except-pass` | low | Swallowed exception |
| `debug-log` | low | `console.log` left in code |
| `todo-fixme` | info | TODO/FIXME markers |

Additional info-level structure checks: `file-too-long`, `long-lines`, `long-function`.

### Beyond regex

- **AST layer** for Python: alias tracking, one-hop constant propagation, `builtins.eval`, aliased `pickle`, `shell=True`/`verify=False` hidden behind variables, and unsafe YAML loaders (`UnsafeLoader`/`Loader` rejected; `SafeLoader`/`FullLoader` allowed).
- **Secret redaction**: credential values are masked in every output format (text, Markdown, JSON, SARIF, baselines, and autofix previews).
- **Windows-safe**: ignore paths use POSIX separators; stdout is forced to UTF-8 so reports never crash on legacy consoles.

## Suppression

```python
# vibecheck: disable=eval-exec      # next line is skipped for this rule
dangerous_call(trusted_input)

risky_call(arg)  # vibecheck: disable=eval-exec

# vibecheck: ignore   (first line of a file = skip the whole file)
```

Project-wide: create `.vibecheckignore` with one regex per line (POSIX paths on every OS).

```text
# generated code
^generated/
legacy_.*
```

## Autofix

`--fix` writes files in place. Every current fix changes behavior, so it requires the explicit `--fix-unsafe` opt-in:

```bash
python3 vibecheck.py ./src --fix-dry-run --fix-unsafe   # preview, write nothing
python3 vibecheck.py ./src --fix --fix-unsafe           # apply
```

| Tier | Rule | Fix |
|---|---|---|
| unsafe | `yaml-unsafe-load` | `yaml.load` → `yaml.safe_load` (skipped when `Loader=` is present) |
| unsafe | `verify-false` | Remove the TLS opt-out |
| unsafe | `debug-log` | Remove the `console.log` line |

Autofix never edits outside the scanned root and skips symlinks. Always review the diff; do not run autofix in CI without committing the result.

## Tested with evidence

- **44 automated tests** (`python tests/test_vibecheck.py`): exact-line detection, dogfood regressions, false-positive guarantees, baseline, SARIF, 1 MB minified files, binaries, Unicode, v1.0 hardening (aliases, constant propagation, `.env`, scoring caps, Windows-safe ignores), redaction, and autofix confinement.
- **Benchmark**: `benchmark.py` runs a 9-file ground-truth corpus (15 expected pairs) as a regression gate — not an industry-wide benchmark.
- **Dogfood**: scanning `vibecheck.py` itself scores 100 with info-level structure notes only.
- Real-world spot checks: `pallets/click` → 84 OK (only low `except-pass`, test-only `pickle`, info notes); `python-dotenv` → 100 CLEAN.

## Limitations

- Static analysis with one-hop alias/AST resolution; no cross-file data-flow or taint tracking.
- Unquoted `KEY=value` secrets are checked only in `.env*` files; split or concatenated secrets can evade.
- SQL injection is pattern-based; dynamically composed queries may evade.
- Not a replacement for Semgrep, Bandit, or CodeQL — it is a fast pre-merge gate.

## Privacy

`vibecheck` never calls the network and never executes scanned code. It reads the files you point it at and writes only the output you request (reports, baselines, autofixes). Reports may contain source context; credential values are redacted, but treat reports as internal documents.

## Integrations

- `examples/github-action.yml` — SARIF upload for GitHub code scanning
- `examples/pre-commit-config.yaml` — pre-commit hook

## Related skills

- **vibegit** — estimate how much of a repository is AI-assisted (slop score, badge, CI gate): [ClawHub](https://clawhub.ai/thiennhant95/vibegit) · [GitHub](https://github.com/thiennhant95/vibegit)
- **skill-firewall** — scan third-party agent skills before installing them: [ClawHub](https://clawhub.ai/thiennhant95/skill-firewall) · [GitHub](https://github.com/thiennhant95/agent-skills)
- **undo-first** — reversible-action guard with snapshots, risk gate, and verified restore: [ClawHub](https://clawhub.ai/thiennhant95/undo-first) · [GitHub](https://github.com/thiennhant95/agent-skills)

## License

MIT. See [LICENSE](LICENSE).

---

Vietnamese documentation: [README.vi.md](README.vi.md).
