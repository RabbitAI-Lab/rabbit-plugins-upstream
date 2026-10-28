---
name: rms-e2e-demo
description: |
  End-to-end test skill for repo-mirror-sync. It exists solely to exercise the
  multi-repo synchronization chain on a throwaway e2e-* scenario branch: GitCode
  master (squash merge) -> filtered github branch -> GitHub mirror / GitCode
  mirror (rewritten author) -> ClawHub publish. It is created, synced across all
  targets and then soft-deleted. Do not use in production.
---

# rms-e2e-demo

A deliberately minimal but well-documented skill used by `e2e/run_e2e.py` to
verify eventual consistency of the multi-repo sync chain.

## What this skill verifies

- The `master` -> `github` branch step performs file-level filtered cherry-pick
  (paths under `.grape/` must never leak to any downstream).
- The `github` branch is the single source of truth for GitHub, the GitCode
  mirror and ClawHub.
- Commit authors are rewritten to the configured bot identity on git targets.
- Concurrency: two parallel sync instances converge via push CAS retries.

## Usage in the harness

1. The harness seeds an orphan source branch `e2e-<run>-src` containing this
   skill plus a `.grape/secret.txt` file that must be excluded.
2. It runs `pipeline.run_sync` and asserts the github branch tree excludes
   `.grape/` and equals both git targets' trees.
3. It publishes this skill to ClawHub (`rms-e2e-demo`) and soft-deletes it in
   cleanup.

## Acceptance criteria

- github branch tree == GitHub mirror tree == GitCode mirror tree.
- `.grape/secret.txt` absent from every downstream.
- ClawHub shows `rms-e2e-demo` publishable, then removed.

Body revision: v2
