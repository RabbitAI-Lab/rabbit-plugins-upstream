# Phase Challenge Prompt Reduction

## Problem

The `phase_challenge.py` in `adversarial-plan/scripts/phases/` embedded the full plan.md and spec.md text directly into the challenge prompt:

```python
f"--- plan.md ---\n{plan_text}\n\n"
f"--- spec.md ---\n{spec_text}"
```

With a plan of 761 lines and a spec of 240 lines, this created a ~1000-line prompt. Models with file-access tools (Claude via tmux, pi, Codex) already have access to these files on disk via `--cwd` and `git diff`. The embedding was redundant.

## Impact

| Metric | Before | After | 
|--------|--------|-------|
| Prompt length | ~1000+ lines | 724 chars (~40 lines) |
| Claude Fable 5 challenge time | ~25+ min (extended thinking on massive prompt) | ~2-3 min (Sonnet, reads files from disk) |
| Failure rate | High (timeout on extended thinking) | Low (fast, reliable) |

## Fix

Remove the embedded text from `_build_prompt()` in `adversarial-plan/scripts/phases/phase_challenge.py`:

```python
def _build_prompt(branch_point=""):
    diff_base = branch_point or "<branch-point>"
    return (
        "Challenge the implementation plan at `plan.md` against its "
        "specification at `spec.md` (both are in the current directory). "
        f"The branch-point SHA is `{diff_base}`. Inspect the cumulative "
        f"change with `git diff {diff_base}..HEAD`.\n"
        ...
        '\"summary\": \"counts by severity\"}\n'
    )
```

The model reads `plan.md` and `spec.md` directly from the filesystem via its shell tools (cat, git, grep). The prompt is just instructions + schema.

## Validation

- **Before (2026-07-14):** Challenge with embedded plan+spec → timeout after 1800s (Fable 5 extended thinking)
- **After (2026-07-15):** Challenge without embedding → Claude Sonnet completes in ~2 min with valid JSON findings
- **Exit codes unchanged:** REVIEW still returns exit 0 (success) or exit 1 (failure/malformed JSON)
- **Backward compatible:** models that cannot read files (pure API models without shell access) lose context; but the adversarial pipeline always runs models with `--cwd` pointing to the workdir, so all supported models (Claude tmux, pi, Codex, DeepSeek) have file access.

## Apply to other pipelines

The same pattern applies to `adversarial-spec`'s `phase_challenge.py` and any phase that embeds large files into prompts when the model can read them directly from disk. Check `--cwd` is set before relying on file-access; without it, models may look in the wrong directory.
