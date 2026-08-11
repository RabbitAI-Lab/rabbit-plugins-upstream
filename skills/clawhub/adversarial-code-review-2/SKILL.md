---
name: adversarial-code-review
description: "Multi-perspective adversarial code review with git-isolated worktrees. Two reviewers (Architect + Inspector), cross-validation, and synthesis report. The synthesis is the final arbiter — its verdict takes priority over individual reviewer outputs."
tags: [adversarial, code-review, multi-model, parallel, review-only, persona, git]
version: 1.10.0
license: 0BSD
---

# adversarial-code-review

Multi-perspective adversarial review of a diff or codebase. Two independent
reviewers (**Architect** + **Inspector**) run concurrently and each produce JSON
findings, two **cross-review** passes (A reviews B's findings, B reviews A's
findings) pressure-test them, and a **synthesis** rapporteur collapses everything
into a single ranked report.

The review engine, subprocess runner, and personas live in the sibling
`adversarial-common` skill — this skill only wires the review flow and the
source-gathering modes.

## Installation

Requires the `adversarial-common` sibling repo (shared engine). One-line install:

curl -fsSL https://raw.githubusercontent.com/chpomob/adversarial-code-review/main/scripts/install.sh | bash

or, from an existing checkout:

bash scripts/install.sh

Both place adversarial-code-review and adversarial-common side by side under `~/.hermes/skills` (override the target with `$1` or `$HERMES_HOME`).

## When to use

- Before merging a feature branch (`--diff-git`).
- On a standalone patch file (`--diff`).
- On a whole directory or single file (`--dir`, `--file`).
- On an existing project in place (`--project-dir`).

## Usage

```bash
python3 scripts/adversarial_review.py <source> [options]
```

The reviewer command defaults to the `claude-tmux` wrapper (no model pinned —
the CLI picks its own best). Override per-run with `--review-cmd` or persistently
with `$ACR_REVIEW_CMD`.

### Sources (mutually exclusive)

| Flag | Argument | Reviews |
|------|----------|---------|
| `--diff-git` | — | `<base>..HEAD` inside an isolated git worktree (dirty tree auto-stashed) |
| `--diff` | `FILE` | a unified-diff file |
| `--dir` | `DIR` | every file under a directory |
| `--file` | `FILE` | a single file |
| `--project-dir` | `DIR` | an existing project directory in place |

### Options

| Flag | Default | Purpose |
|------|---------|---------|
| `--a-cmd` | `--review-cmd` (or `$ACR_A_CMD`) | Architect model command (overrides `--review-cmd`) |
| `--b-cmd` | `--review-cmd` (or `$ACR_B_CMD`) | Inspector model command (overrides `--review-cmd`) |
| `--cross-a-cmd` | `--a-cmd` (or `$ACR_CROSS_A_CMD`) | Cross-review A model — Architect reviews Inspector's findings |
| `--cross-b-cmd` | `--b-cmd` (or `$ACR_CROSS_B_CMD`) | Cross-review B model — Inspector reviews Architect's findings |
| `--synth-cmd` | `--review-cmd` (or `$ACR_SYNTH_CMD`) | Synthesis model command |
| `--base` | `$ACR_BASE`, then `main`, then `master` | base ref for `--diff-git` (tried in that order) |
| `--feature` | current branch name | slug used for the worktree path `/tmp/review-<feature>-<N>` |
| `--allow-fallback` | off | on `--diff-git` worktree failure, review the live workdir instead of exiting 2 |
| `--out` | `.adversarial-review` | artifact directory |
| `--review-cmd` | `$ACR_REVIEW_CMD`, then the claude wrapper | CLI that runs every reviewer pass (fallback for per-role flags) |
| `--delegated` | off | orchestrator/worker pre-review for high-complexity inputs |
| `--orchestrator-cmd` | `--synth-cmd` | delegation/decomposition model command |
| `--worker-cmd` | `--b-cmd` | delegated worker model command |
| `--max-agents` | `6` | cap parallel and delegated fan-out |
| `--show-costs` | off | print per-model token/cost breakdown to stderr |
| `--html` | off | write a self-contained `report.html` |
| `--timeout` | `600` | per-phase timeout (seconds) |

**Env vars:** `ACR_A_CMD`, `ACR_B_CMD`, `ACR_CROSS_A_CMD`, `ACR_CROSS_B_CMD`,
`ACR_SYNTH_CMD`, `ACR_ORCHESTRATOR_CMD`, `ACR_WORKER_CMD` — each falls back to the
resolved `--review-cmd` (or its env var `ACR_REVIEW_CMD`), except
`ACR_CROSS_A_CMD` which falls back to `ACR_A_CMD` and `ACR_CROSS_B_CMD` which
falls back to `ACR_B_CMD`.

### Example: review a single file with Codex Architect + Claude Inspector

```bash
python3 scripts/adversarial_review.py \
  --file /path/to/target.py \
  --a-cmd "codex exec --skip-git-repo-check --sandbox read-only" \
  --b-cmd "python3 /path/to/claude-tmux.py --timeout 600 --hard-timeout 1200 --cwd /path/to/repo" \
  --synth-cmd "python3 /path/to/claude-tmux.py --timeout 600 --hard-timeout 1200 --cwd /path/to/repo" \
  --out /tmp/acr-review
```

### Example: review the current branch against `main`

```bash
python3 scripts/adversarial_review.py --diff-git --base main --out .adversarial-review
```

### Example: review a full project directory — Codex + Claude with mutual cross-review

```bash
python3 scripts/adversarial_review.py \
  --project-dir /path/to/repo \
  --a-cmd "codex exec --skip-git-repo-check --sandbox read-only" \
  --b-cmd "python3 /path/to/claude-tmux.py --timeout 600 --hard-timeout 1200 --cwd /path/to/repo" \
  --cross-a-cmd "codex exec --skip-git-repo-check --sandbox read-only" \
  --cross-b-cmd "python3 /path/to/claude-tmux.py --timeout 600 --hard-timeout 1200 --cwd /path/to/repo" \
  --synth-cmd "python3 /path/to/claude-tmux.py --timeout 600 --hard-timeout 1200 --cwd /path/to/repo" \
  --out .adversarial-review --html --show-costs
```

When `--cross-a-cmd` and `--cross-b-cmd` are omitted, they default to `--a-cmd`
and `--b-cmd` respectively. The targets remain symmetric: cross-review A uses
the Architect command to review the Inspector's findings, and cross-review B
uses the Inspector command to review the Architect's findings. Override the
cross commands only when those passes need different providers or settings.

## Output

Artifacts land under `--out` (default `.adversarial-review`):

- `01_architect.txt`, `02_inspector.txt` — raw reviewer JSON
- `03_cross_1.txt` — cross-review: A reviews B's (Inspector) findings
- `04_cross_2.txt` — cross-review: B reviews A's (Architect) findings
- `05_synthesis.txt` + `review.md` — the consolidated ranked report
- `final.json` — machine-readable verdict, complexity, parallel mode, and cost ledger for CI/cron
- `report.html` — optional self-contained report produced by `--html`

`final.json` shape:

```json
{
  "verdict": "APPROVE|REQUEST_CHANGES|REJECT",
  "summary": "first lines of the synthesis report",
  "findings": {"blocker": 1, "major": 2, "minor": 4},
  "report": ".adversarial-review/review.md",
  "source_diff": true
}
```

## Exit codes

| Code | Meaning |
|------|---------|
| `0` | review complete |
| `1` | pipeline / infrastructure failure (reviewer CLI crashed, git error) |
| `2` | nothing to review or review setup cannot proceed (no files, missing base, `--diff-git` setup failure) |
| `5` | `EXIT_CONTEXT_BLOCKED`: the preflight context gate rejected empty or insufficient input |

## Personas

Loaded from `../adversarial-common/personas/` — the single source of truth,
now **100% generic** (no embedded/hardware-specific references):

- `architect.md` — architecture, security, concurrency, design
- `inspector.md` — bugs, edge cases, error handling, quality
- `cross_review.md` — devil's advocate: VALIDATE / CHALLENGE / ADD
- `synthesis.md` — rapporteur: cross-validated / consensus / disputed

## Model pairing rules

- **Architect and Inspector MUST be different models** (never the same model for
  both roles). The cross-reviews each default to one of the two (cross-A → A,
  cross-B → B), while their targets are the other reviewer's findings: A reviews
  B and B reviews A. The default is therefore a symmetric mutual cross-review.
- **Never pin a specific Claude model** (`--model sonnet`, `--model best`, etc.)
  unless the user explicitly asks for one — let the claude-tmux wrapper use its
  default.
- **Preferred pairing:** Codex (Architect) + Claude (Inspector + cross-B +
  Synthesis). Codex does the structural/design analysis; Claude produces reliable
  JSON output in the exact schema the pipeline expects.
- **Alternative for Inspector:** GLM-5.2 — works but may output different JSON
  keys (`category` instead of `file`, `issue` instead of `summary`).
  See GLM-5.2 pitfall below.
- **Synthesis should use the same model as Inspector** to avoid schema conflicts.

## Pitfalls

- **GLM-5.2 inspector may output a different JSON schema than expected in `--file` mode.** The pipeline expects findings with keys `{id, severity, file, line, summary, evidence}` plus a top-level `verdict`. GLM-5.2 may write prose with different keys like `{id, severity, category, location, issue, fix}` — a structural schema mismatch that `strip_json_wrapper` cannot fix. **Symptom:** `02_inspector.txt` exists but `Phase 'inspector' failed (exit 1)` with `invalid reviewer JSON: expected findings with id, severity, file, line, summary, and evidence`. **Diagnosis:** check `02_inspector.txt` — if the JSON keys don't match the pipeline schema, it's a schema mismatch, not a formatting issue. **Fix:** either (a) add the missing keys to the persona prompt in `personas/inspector.md`, or (b) switch the inspector to a model that reliably outputs the exact schema (Codex works; DeepSeek V4 Pro usually works). Validated 2026-07-14 on claude-tmux.py review.

- **`_valid_line()` now accepts free-form string markers, not just integers.** Models sometimes emit non-numeric line markers like `"(review request)"` or `"(global)"` for findings that don't map to a specific line. Previously `_valid_line()` required `isinstance(line, int) or line.isdigit()`, which rejected these strings and caused the entire phase to fail with `invalid reviewer JSON`. **Fixed 2026-07-15:** `_valid_line()` now returns `True` for any non-empty string, preserving the original intent (integer preferred) while tolerating model-generated location markers. Validation still rejects empty strings and `None`. See `git log -1 -- scripts/adversarial_review.py` for the commit change.

- **Full-project reviews (`--project-dir`, `--dir`) exceed the foreground timeout cap.** The
  5-phase pipeline (Architect + Inspector + 2 cross-reviews + Synthesis) on a multi-file
  codebase takes 5–30 minutes depending on model speed and file count. On Hermes CLI, the
  foreground terminal timeout caps at 600s. **Always run `--project-dir` or `--dir` reviews
  in background mode with `notify_on_complete=true`.** See example above.

- **Synthesis phase times out when Claude quota is exhausted.**

- **Cross-review is symmetric even when the cross command flags are omitted.**
  Cross-review 1 runs the Architect command on the Inspector's findings;
  cross-review 2 runs the Inspector command on the Architect's findings and
  receives round 1 as additional context. The flags select commands, not review
  targets.

- **The `claude-tmux` wrapper rejects `--yolo`.** Do not add that option to
  reviewer, cross-review, or synthesis commands.

- **`~` in `--a-cmd`/`--b-cmd`/`--synth-cmd` mid-command breaks `resolve_role_cmd`.** `providers.resolve_role_cmd()` only calls `os.path.expanduser()` when the entire command starts with `~`. A command like `python3 ~/.hermes/skills/...` (tilde mid-string) never gets expanded, so the subprocess runner receives a literal `~` and fails with `Command not found`. **Fix (applied 2026-07-14):** split the command per-token with `shlex.split()`, expand each token, and re-join with `shlex.join()` before returning. This ensures `~` is resolved regardless of position in the command string. The fix lives in `adversarial_common/adversarial_common/providers.py:resolve_role_cmd`.

- **Pre-publication reviews need a cleanup sweep, not just code defects.** Before publishing
  any Hermes skill, run the full checklist in `references/pre-publication-cleanup.md`:
  privacy scan, tracking audit (French files, pipeline artifacts, backup copies, personal
  notes, OAuth bypass docs), .gitignore hygiene, and SKILL.md reference de-dangling.
  The adversarial review finds code defects but does NOT check for leaked config,
  language-mismatched content, or missing metadata — the orchestrator must run those
  separately. **Validated 2026-07-16:** adversarial-code-loop had 9 French-language files
  and 52 personal workflow references committed; adversarial-plan had pipeline artifacts
  from 2 separate loop runs. All were git rm --cached + push-removed.

- **Personas historically contained hardcoded hardware references (ESP32-S3, CC1101 at 433 MHz, BLE) that biased reviews of pure-software projects.** This was fixed 2026-07-17: all 4 persona files in `../adversarial-common/personas/` were rewritten to be generic. The old `architect.md` asked about DSP on ESP32-S3, noise floor, antenna gain, IRAM usage; the old `inspector.md` asked about CC1101 RSSI quantization, SPI bus speed, and BLE spectral scans. If you encounter any remaining hardware-specific language in the personas, patch `../adversarial-common/personas/<file>.md` to remove it.

- **`--diff-git` needs git ≥ 2.5** (worktree support). `gitops.ensure_git_available()`
  guards git presence; older hosts should use `--diff` or `--project-dir`.
- **Worktrees are created under `/tmp/review-<feature>-<N>`** and force-removed in a
  `try/finally`, even when the applied patch leaves them dirty. A crash mid-review
  can leave one behind — `git worktree prune` cleans stale metadata.
- **A dirty working tree is auto-stashed and restored.** If `git stash pop` hits a
  conflict (rare — the review does not touch the main workdir), the stash is kept and
  a warning is printed; resolve and `git stash pop` manually.
- **Base resolution is a fallback chain**, not strict: `--base` that does not resolve
  keeps trying `$ACR_BASE` → `main` → `master`. Set `ACR_BASE` in CI to make the base
  explicit and stable.
- **An empty or insufficient diff exits 5 (`EXIT_CONTEXT_BLOCKED`)**, not 0 —
  configure CI to handle a blocked preflight explicitly.
- **Worktree creation failure exits 2 by default** (no silent fallback to the live
  workdir, which could review the wrong tree). Pass `--allow-fallback` to instead
  review the current working directory with a prominent stderr warning.
- **`--diff-git` never moves the main workdir's branch** — the worktree is a separate
  checkout at the merge-base. The original branch is restored defensively in cleanup.
- The reviewer CLIs are invoked through `adversarial_common.runner.run_cli` (temp-file
  IO, `start_new_session`, killpg on timeout) — a hung sandbox grandchild cannot
  deadlock the pipeline.
