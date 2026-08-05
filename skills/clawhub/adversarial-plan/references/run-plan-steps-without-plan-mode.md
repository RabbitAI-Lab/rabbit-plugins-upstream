# Running plan steps without `--plan` mode

**`--plan` mode is NOT wired in `adversarial-code-loop`** (pitfall #1, validated
2026-07-15). The `adversarial_loop.py` argparse only accepts `--spec`, not `--plan`.
This reference documents the working workflow: execute each plan step as a separate
code loop with a focused per-step spec.

## Workflow

1. **Extract one step from the plan** — copy its Files, Description, Tests, and Risks
   into a standalone spec.md with YAML frontmatter.
2. **Launch a code loop** on that spec using the target repo as `--workdir`.
3. **Repeat for each step**, respecting dependency order.

## Step → spec pattern

Given a plan step like:

```
### P3: Implement the model-agnostic quota resolver
- **Files:** [adversarial_common/quota.py, adversarial_common/__init__.py, adversarial_common/tests/test_quota.py]
- **Dependencies:** [P1, P2]
- **Description:** Create QuotaResolver with TTL cache, state machine, thresholds...
- **Tests:** Add tests for ordered fallback, cache, force modes, thresholds...
- **Risks:** Cache sync, partial checker data...
```

Create a spec:

```yaml
---
name: "quota-resolver"
version: "1.0"
author: "adversarial-plan"
status: "draft"
targets:
  - file: adversarial_common/quota.py
    description: "QuotaResolver with cache, state machine, thresholds, force modes."
  - file: adversarial_common/__init__.py
    description: "Export resolver symbols."
  - file: adversarial_common/tests/test_quota.py
    description: "Tests for resolver, cache, fallback, force."
---

# Quota Resolver

## Problem
...

## Requirements
- R1: ...
```

## Launch pattern

```bash
python3 ~/.hermes/skills/adversarial-code-loop/scripts/adversarial_loop.py \
  --spec /path/to/step-spec.md \
  --feature short-descriptive-name \
  --dev-cmd "codex exec --dangerously-bypass-approvals-and-sandbox --skip-git-repo-check --sandbox workspace-write" \
  --review-cmd "python3 /path/to/claude-tmux.py --timeout 900 --hard-timeout 1800 --cwd /path/to/target-repo" \
  --workdir /path/to/target-repo \
  --timeout 1800 \
  --max-loops 3 \
  --no-arbiter
```

## Key decisions

| Decision | Rule |
|----------|------|
| `--workdir` | Point to the **repo** containing the step's files (e.g. adversarial-common for quota.py) |
| `--cwd` for claude-tmux | Always set to the same `--workdir` so reviewer finds the right git repo |
| Parallel steps | Safe ONLY when steps target different repos (different `--workdir`). Never parallel on same repo (pitfall #8) |
| File paths in spec | Relative to `--workdir` (e.g. `adversarial_common/quota.py` not `../adversarial-common/...`) |
| `--no-arbiter` | Recommended for atomic steps — single model review is sufficient |
| `--feature` | Short slug matching the step purpose, avoids branch collisions |

## Pre-flight checklist

- [ ] Target repo is on `main` with clean `git status`
- [ ] `--workdir` is an individual skill repo (NOT `~/.hermes/skills/`)
- [ ] claude-tmux `--cwd` matches `--workdir`
- [ ] No `--yolo` in claude-tmux command (flag doesn't exist in v1)
- [ ] No `--model` in claude-tmux command (use wrapper default)
- [ ] Spec targets use paths relative to `--workdir`
- [ ] Timeout is generous (1800+ for Claude extended thinking)
