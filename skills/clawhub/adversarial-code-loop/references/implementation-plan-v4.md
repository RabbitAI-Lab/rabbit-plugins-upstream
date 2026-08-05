# adversarial-code-loop v4 — Implementation Plan

Status as of 2026-07-06: **partially implemented** (steps 0-4 complete).

## Completed steps

| Step | File(s) | Status | Details |
|------|---------|--------|---------|
| 0 | `scripts/phases/__init__.py` | ✅ | v4 structure created; legacy predecessor entry point was removed before release |
| 1 | `adversarial-common/adversarial_common/gitops.py` | ✅ | 239 lines, 14 integration tests passed |
| 2 | `adversarial-common/personas/{builder,critic,fixer,verifier,judge,builder-pi,fixer-pi}.md` | ✅ | Git-aware header block added to all 7 files |
| 3 | `scripts/phases/phase_{build,review,fix,verify,arbiter,git}.py` | ✅ | 6 modules + test_phases.py (549 lines total) |
| 4 | `scripts/adversarial_loop.py` | ✅ | 475-line orchestrator, GLM-reviewed, 3/4 critical findings fixed |

## Remaining steps

| Step | File(s) | Priority |
|------|---------|----------|
| 5 | SKILL.md (v4 documentation) | Medium — partially done |
| 6 | Integration tests (11 scenarios) | Medium — need scripts in references/ |
| 7 | Finalize v4 as default | Low — v4 needs final testing |

## Known issues

1. Codex-reviewer flakiness: --sandbox read-only conflicts with --dangerously-bypass-approvals-and-sandbox. Fixed in pitfall #1 of v4 pipeline.
2. Codex quota exhaustion: ~Jul 6-7 monthly limit. Fallback: GLM-as-REVIEW or Claude-as-REVIEW.
3. GLM JSON in markdown: outputs wrapped in ```json blocks. v4 must strip before parsing.
4. Claude-as-DEV timeout on large refactors. Mitigation: split specs, timeout 2400+.
5. State.json: v4's optimisitic state writing (before phase) + marking (after) is safer.
