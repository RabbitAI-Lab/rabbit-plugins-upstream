---
name: foreman
description: Dispatch-and-acceptance control desk for farming coding work out to background agents. Sends executable tasks to worker agents via the handoff CLI, takes delivery against a path whitelist, then gates the merge behind an acceptance protocol whose core rule is that the builder may never touch the tests, assertions, or CI config that judge it. Use it when batching implementation work out to background agents, or when accepting code that someone else — human or agent — built.
---

# foreman — thin router

## What this skill touches (trust boundary)

Farming work out to another agent necessarily means handing something a credential, so here is exactly what that involves:

- **Writes** `.foreman/` inside your repo (task and batch state) and expects it to be gitignored.
- **Reads** `~/.handoff/` — the dispatcher's own task directory — to locate what a worker delivered.
- **`foreman-cworker.sh` passes `$DEEPSEEK_API_KEY` into a container** as that worker's own API credential. That is the entire point of the caged worker: it receives one key and one mounted worktree, and nothing else — not your home directory, not your other repos, not your primary agent login. The key is read from your environment at call time, is never stored in this skill, is visible only to the process inside the cage, and is gone when that container exits.
- **Runs the verification commands you wrote** in each work order. This skill never invents commands; what you put in a work order is what runs.
- **Sends nothing anywhere else.** No telemetry, no phone-home. Repository content reaches only the backend you configured in `~/.handoff/config.yaml`.

## Entry decision (settle this first, then read the matching chapter)

- **Default (there is work to farm out)**: read `dispatch.md` in this directory and run the dispatch chapter. Once every delivery has passed intake, **automatically** read `verify.md` and enter the acceptance chapter — do not wait to be asked again.
- **User says "just dispatch, skip acceptance for now"**: run `dispatch.md` only and stop at intake.
- **`/foreman verify`, or acceptance only** (including code somebody else handed you): read `verify.md` directly.

## Global invariants (both chapters, ahead of any playbook)

1. **State goes to disk.** Always under `.foreman/` — one `<task_id>.json` per task, one `batch.json` per batch. First action on every entry into foreman: scan `.foreman/` for overdue and unsettled tasks and reconcile them before starting anything new.
2. **One shared escalation budget.** The same `error_fingerprint` showing up a second time → escalate immediately. Dispatch reworks plus acceptance repairs reaching **4 rounds combined** → circuit-break and report to the user.
3. **The measuring instruments are protected.** If a builder's diff touches tests, assertions, or CI config → reject the delivery. No exceptions. This is the only mechanism in the entire scheme that prevents a *consistent* false green: a builder that can edit the ruler can always make the work measure up.
4. **Judge on data, not exit codes.** Acceptance tooling routinely exits 0 no matter what it found. Read only the manifest/findings that *this* run newly generated.
5. **The main session only judges and merges.** Executable work gets farmed out — keep the expensive model's budget for decisions.
