---
name: adversarial-plan
description: "Adversarial implementation planner. Takes a spec.md (from adversarial-spec) and optionally review findings, then produces a plan.md with ordered steps, dependencies, files, tests, and risks. Execute the result through focused per-step specs."
version: 1.0.0
author: Hermes Agent
license: 0BSD
platforms: [linux, macos]
metadata:
  hermes:
    tags: [adversarial, planning, implementation, plan, architecture]
    related_skills: [adversarial-spec, adversarial-code-loop, adversarial-code-review]
---

# Adversarial Plan

**Spec → implementation plan.** Two-role adversarial pipeline that takes a spec.md (from
adversarial-spec) and optionally review findings (from adversarial-code-review), and
produces a plan.md with ordered steps. To implement it with
adversarial-code-loop, convert each step to a focused spec and run the steps in
dependency order; adversarial-code-loop has no functional `--plan` mode.

## Installation

Requires the `adversarial-common` sibling repo (shared engine). One-line install:

curl -fsSL https://raw.githubusercontent.com/chpomob/adversarial-plan/main/scripts/install.sh | bash

or, from an existing checkout:

bash scripts/install.sh

Both place adversarial-plan and adversarial-common side by side under `~/.hermes/skills` (override the target with `$1` or `$HERMES_HOME`).

## Workflow

```text
PREFLIGHT ──→ optional DEEP RESEARCH ──→ GIT SETUP
                                           │
                                           ├─ delegated success ──→ FINALIZE
                                           │
                                           └─ direct/fallback ──→ PLAN ──→ CHALLENGE
                                                                          │
                                               APPROVE + no findings ──────┤
                                                                          │
                                               otherwise ──→ REVISE ──→ VERIFY
                                                                  ↑          │
                                                                  └──────────┘ up to --max-loops
                                                                          │
                                                                      FINALIZE
```

There is one CHALLENGE phase and no `CROSS_2` phase. A successful delegated
run bypasses PLAN/CHALLENGE/REVISE/VERIFY; a delegated fallback enters the
normal adversarial loop. FINALIZE squash-merges an approved plan unless
`--no-merge` is set, or records a rejection marker when findings remain.

## Prompt design

The CHALLENGE prompt references `plan.md` and `spec.md` on disk and instructs
the challenger to read them from the current working directory (the phase
workdir). No document text is embedded in the prompt; the provider runs with
the phase workdir as its cwd, so filesystem-capable providers inspect both
files and the cumulative branch diff directly.

## CLI

<!-- CLI-FLAG-TABLE:START -->

| Flag | Value/default | Purpose |
|------|---------------|---------|
| `--help` | `-h` alias | Show command help and exit. |
| `--spec` | path; `<workdir>/spec.md` | Specification to plan. |
| `--findings` | path; optional | JSON array, or object containing a `findings` array, to incorporate into the plan. |
| `--dev-cmd` | command; `$APLAN_DEV_CMD` or built-in default | Explicit plan-writer command; with a provider registry, bypasses registry selection for writer phases. |
| `--review-cmd` | command; `$APLAN_REVIEW_CMD` or built-in default | Explicit challenger/verifier command; with a provider registry, bypasses registry selection for those phases. |
| `--provider-config` | path; `$ADVERSARIAL_PROVIDER_CONFIG` | Provider registry YAML. |
| `--force` | off | Skip quota checks and select each registry role's primary provider. |
| `--force-provider` | `ROLE:ALIAS`; repeatable | Force one provider alias for `writer`, `challenger`, or `verify`. |
| `--workdir` | directory; `.` | Target Git repository and phase working directory. |
| `--max-loops` | positive integer; `2` | Maximum REVISE/VERIFY rounds after CHALLENGE. |
| `--feature` | name; derived from spec | Branch and artifact name. |
| `--timeout` | positive seconds; `600` | Timeout for each planner/challenger subprocess. |
| `--out` | directory; `.adversarial-plan` | Artifact base directory; relative paths resolve under `--workdir`. |
| `--no-merge` | off | On approval, leave the plan branch unmerged. |
| `--show-costs` | off | Print a per-phase cost breakdown to stderr. |
| `--retries` | positive integer; `3` | Maximum CLI retries for each phase call. |
| `--max-input-chars` | positive integer; unlimited | Cap prompt input characters for each phase call. |
| `--max-output-chars` | positive integer; unlimited | Cap provider output characters for each phase call. |
| `--html` | off; optional mode | Render an HTML report after `final.json`. This does not change the adversarial flow. |
| `--ci` | off; optional mode | Suppress banners, use plain stderr, and return stable CI exit codes. |
| `--fail-on` | selector; optional CI mode | Set CI failure conditions, for example `findings,severity:blocker`; used when `--ci` is active. |
| `--deep-research` | off; optional mode | Run bounded external research after preflight and merge its findings before planning. |
| `--research-cmd` | command; research env/dev/default fallback | Provider command used by `--deep-research`. |
| `--research-max-queries` | positive integer; `5` | Maximum research queries. |
| `--research-max-results` | positive integer; `5` | Maximum results retained per research query. |
| `--research-timeout` | positive seconds; `60` | Timeout for each research query. |
| `--delegated` | off; optional mode | Decompose high-complexity work among workers. A successful delegated run **bypasses the adversarial PLAN/CHALLENGE/REVISE/VERIFY loop**; a direct fallback resumes it. |
| `--delegated-concurrency` | positive integer; complexity recommendation | Maximum concurrent delegated workers. |

<!-- CLI-FLAG-TABLE:END -->

## Output format

plan.md with YAML frontmatter + ordered steps:

```yaml
---
spec: "feature-name"
version: "1.0"
author: "adversarial-plan"
based-on: "adversarial-spec"
findings-input: false
---

## Steps

### P1: First task
- **Files:** [path/to/file.rs]
- **Description:** What changes in this file
- **Dependencies:** []
- **Tests:** What tests to write
- **Risks:** What could go wrong

### P2: Second task
- **Files:** [path/to/another.rs]
- **Description:** What changes
- **Dependencies:** [P1]
- **Tests:** Integration test
- **Risks:** Deadlock risk
```

## Personas

Loaded from adversarial-common/personas/:
- plan-writer.md — reads spec.md + optional findings, writes plan.md
- plan-challenger.md — reads plan.md, outputs JSON findings (risks, order, gaps)

## Exit codes

| Code | Meaning |
|------|---------|
| 0 | APPROVED — plan squash-merged |
| 1 | Infrastructure failure |
| 2 | Usage error |
| 3 | REJECT |

## Integration with dev loop

**IMPORTANT: `--plan` mode is not wired in `adversarial-code-loop`.** Its
parser accepts `--spec`, not a plan file.

Instead, execute each plan step as a separate code loop with a focused per-step
spec. See [Running plan steps without plan mode](references/run-plan-steps-without-plan-mode.md)
for the step-to-spec template, launch pattern, and pre-flight checklist.

```bash
# Example: running P1 of a plan
python3 ~/.hermes/skills/adversarial-code-loop/scripts/adversarial_loop.py \
  --spec /path/to/step-P1-spec.md \
  --workdir /path/to/target-repo \
  --dev-cmd "codex exec --dangerously-bypass-approvals-and-sandbox --skip-git-repo-check --sandbox workspace-write" \
  --review-cmd "python3 .../claude-tmux.py --timeout 900 --hard-timeout 1800 --cwd /path/to/target-repo" \
  --timeout 1800 --max-loops 3 --no-arbiter
```

Steps without dependencies targeting different repos can run in parallel (safe).
Parallel on the same repo is forbidden (adversarial-code-loop pitfall #8).

## Plan format constraints

- **Plan validation is partial.** It checks frontmatter, at least one step,
  contiguous step IDs, and requirement-ID coverage in the spec. It does NOT
  enforce step field schemas, parse dependency lists, detect cycles,
  topologically sort, validate file paths, or verify that review findings
  are addressed. Most semantic correctness is delegated to the challenger model.

## Pitfalls

- **The `--findings` flag does NOT accept adversarial-review's `final.json` as-is.** That file contains finding *counts* (`{blocker: 1, major: 2}`), not finding objects. You must extract structured findings from the review synthesis report and craft a findings.json manually.
- Each step must have explicit dependencies (or empty list). Circular deps cause validation failure.
- If review findings are provided via --findings, the plan must address each finding in at least one step.
- Step order should respect dependencies (enforced manually; no automatic topological sort).
- The same code patterns as adversarial-code-loop v4: git branch isolation, phase modules, squash merge.
- **For implementation, treat one plan step as one code-loop spec.** Run steps in
  dependency order. Independent steps may run concurrently only when their
  code loops use different repositories.
- **Plan parser is strict about bullet format.** Files and Dependencies must be on a single
  line: `- **Files:** /path1, /path2`. Indented sub-lists are NOT parsed.
- **CHALLENGE reads plan.md and spec.md from disk** (provider file tools). The
  orchestrator validates both files are regular files and are UTF-8 decodable
  before running the phase (fail-fast on FIFOs, device nodes, or binary content).
- **Stash pop may conflict** if untracked files (e.g. `findings.json`) exist in
  the workdir at pipeline end. Fix: `git add` the file before launching, or
  pass `--findings` from outside the workdir.
- **`write_final_json()` may crash** if stash state is inconsistent at finish
  time. The squash-merge already succeeded; only the artifact write is lost.
