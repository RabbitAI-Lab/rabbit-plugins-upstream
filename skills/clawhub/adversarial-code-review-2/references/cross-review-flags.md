# Cross-review flags — `--cross-a-cmd` and `--cross-b-cmd`

Added 2026-07-17 to enable mutual adversarial cross-validation where
A reviews B's findings and B reviews A's findings.

## Background

Originally the pipeline ran both cross-review passes with `--b-cmd` (the
Inspector's model), so Claude validated its own findings — a self-review
with no genuine adversarial pressure.

## Solution

Two new flags, each defaulting to its corresponding review model:

- `--cross-a-cmd` → defaults to `--a-cmd` (Architect reviews Inspector's work)
- `--cross-b-cmd` → defaults to `--b-cmd` (Inspector reviews Architect's work)

When both are omitted, the defaults already produce mutual cross-review:
the Architect command reviews the Inspector's findings, and the Inspector
command reviews the Architect's findings. Set a cross flag only to override
the provider or settings for that pass; flags select commands, not targets.

## Pipeline flow (with mutual cross-review)

```
Phase 1: Architect  (A cmd)  → produces findings
Phase 2: Inspector  (B cmd)  → produces findings
Phase 3: Cross-1    (cross-a-cmd) → A reviews B's findings
Phase 4: Cross-2    (cross-b-cmd) → B reviews A's findings + sees Cross-1
Phase 5: Synthesis  (synth-cmd) → consolidated report
```

## Validated on (2026-07-17)

chatter-javier review: `--cross-a-cmd="codex ..." --cross-b-cmd="claude-tmux ..."`
Verdict: REQUEST_CHANGES, 1 blocker + 11 major + 3 minor + 1 nit.
Both cross-review passes produced substantive VALIDATE/CHALLENGE/ADD findings
that strengthened the final report. Cross-2 (B reviews A) specifically caught
Docker binding issues and end-to-end failure chains that A's initial review
had flagged at lower confidence.

## Env vars

- `ACR_CROSS_A_CMD` — overrides `--cross-a-cmd`
- `ACR_CROSS_B_CMD` — overrides `--cross-b-cmd`
