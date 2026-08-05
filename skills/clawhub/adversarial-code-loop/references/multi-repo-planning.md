# Historical multi-repo planning prototype

> **HISTORICAL ONLY — NOT IMPLEMENTED.** The released orchestrator has no `--plan`
> argument. `phase_plan.py` contains prototype helpers but is not imported or wired to
> the CLI. Run each plan step separately with `--spec` in the target repository.

## Intended design

The prototype would have executed each step on its own git branch and used
`_resolve_step_workdir()` to find the repository enclosing each listed file. This
design was never connected to the command-line entry point.

## Prototype issues observed (2026-07-07)

1. **Plan-level git lifecycle stays in `--workdir`.** The stash, parent branch detection,
   and .gitignore setup all run in the original `--workdir`, not the resolved repo.
   This means dirty-tree handling is per-workdir, not per-repo.

2. **Already-done steps produce empty squash.** If BUILD produces no changes (task
   already applied), `git merge --squash` finds nothing to commit. The `squash_merge()`
   fallback to `git merge --ff-only` handles this in most cases.

3. **File paths must be absolute.** `_resolve_step_workdir()` calls
   `gitops.detect_enclosing_repo()` which needs an absolute path. Relative paths are
   resolved against `--workdir`.

4. **Plan format is fragile.** Files and dependencies must be on a single comma-separated
   line. Multi-line bullet lists are NOT parsed by the prototype helper.

## Historical experiment

2026-07-07: 8-step cross-skill refactoring across 5 repos:
- P2 (jsonio helpers) → adversarial-common: passed
- P3 (fail_phase alias) → adversarial-common: passed
- P4 (run_arbiter params) → adversarial-code-loop: passed
- P5 (gitops consolidate) → adversarial-code-loop: passed
- P6 (try_parse_json) → adversarial-code-loop: rejected (GLM quota)
- P7-P9: skipped

4/8 prototype steps succeeded when helpers were exercised during development. This did
not validate a released plan-mode CLI; no such CLI was shipped.
