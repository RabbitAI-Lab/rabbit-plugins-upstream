# Anti-Patterns 2.2

Field-derived failure shapes observed repeatedly in real bounded loops. Each entry names the wrong behavior, why it fails, and the replacement. This file is diagnostic: load it when a loop stalls, when a completion claim looks too strong, or before a bulk restructure.

## Execution

| Do not | Why it fails | Do this |
| --- | --- | --- |
| Re-run the same failing command unchanged and call it a retry | Consumes budget without new evidence; the failure signature never changes | Change one variable, form a hypothesis, or stop after two identical signatures |
| Escape a stall by restarting the project | The constraint is usually scope, not the codebase; a restart re-buys the same stall | Cut the Work Order to the smallest publishable increment and ship that |
| Write a manual step as a blocking precondition | A gate the loop cannot execute freezes an otherwise-finished delivery | Mark it `Deferred Owner Verification` with exact repro steps |
| Put a wall-clock budget inside a deterministic algorithm | Same seed yields different output; evidence becomes flaky | Bound deterministic code with deterministic counters; keep time budgets in an outer wrapper |
| Let a diagnostic shard replace the authorized full suite | Narrows coverage without authority | Shard only to diagnose; the original gate still applies |
| Raise `--max-warnings` to make lint green | A raised ceiling is a disabled check, not a result | Lower the ceiling or fix the findings |
| Split a module and leave a larger "God Module" behind | Coupling moved, it did not disappear | Treat any post-split file over roughly 500 lines as an unfinished split; extract the shared abstraction first |

## Duplication And Single Source

Copying a skill, module, or whole project directory "just to try something" is the most common source of later confusion. Three rules:

1. One current fact has one authoritative home; copies are not backups, they are future conflicts.
2. Prefer a worktree, junction, symlink, or branch over a directory copy. If a copy is unavoidable, delete it as soon as the experiment resolves.
3. Before touching a directory, check whether an identical tree already exists elsewhere. Byte-identical siblings mean someone already solved or abandoned this.

## Distributed Artifact Safety

Anything that leaves the machine — a single-file HTML tool, a packaged executable, a published skill, a zip release — carries every literal in it.

- Never hardcode real names, phone numbers, email addresses, customer or counterparty addresses, contract terms, internal pricing, or supplier lists in source, fixtures, tests, templates, or docs.
- Move such values to runtime config or replace them with placeholders. A literal that looks harmless in source becomes a disclosure the moment the artifact ships.
- Treat `AUTH_DISABLED`-style debug switches as release blockers: if a debug bypass is enabled and the service binds a non-local interface, refuse to start rather than warn.

## Before A Bulk Restructure

Any rename, split, migration, or large deletion needs this order:

1. clean commit or verified backup that lives outside the workspace;
2. `git diff > <name>.patch` as a local safety net;
3. the restructure;
4. re-read every file that was touched and verify the documented entry commands actually exist and run.

A README that documents a startup command which does not exist in the tree is a defect, not a doc nit. Verify entrypoints by executing them, not by reading them.

## Claim Upgrades

See `Evidence Downgrade Ban` in `SKILL.md`. The canonical list of forbidden upgrades lives there; do not duplicate or weaken it here.
