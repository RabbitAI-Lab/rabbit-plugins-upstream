---
name: implement-pro
description: Execute independent phases with fresh implementation, review and test contexts. Resume from evidence and verify the combined result before closing a large change.
---

# Execute a phase

The coordinator owns the original task list and acceptance. Each phase is one execution unit. Keep existing unit IDs (including U numbers), tasks and evidence. Start from the goal, design, permitted workspace, applicable standards, acceptance conditions and each phase's inputs, write boundaries and dependencies. Fill missing facts in the existing list. Honor narrower user scope.

## Set up the phase

Inspect the worktree, index and existing work. Use entry snapshots to distinguish prior uncommitted changes from this phase, including in repositories without a HEAD. Keep Git publishing and staging outside the workflow unless authorized. Create only artifact directories the phase needs. Store compact receipts under the original tasks or link longer evidence, for example `verification/P001.md`.

Choose a ready phase after checking actual predecessor outputs. Use [the role guide](references/roles.md) to select the material each assignee needs, including applicable current clauses and their exceptions. If installed, `context-handoff` can attach that material to the assignment. Use a fresh context for each implementation, fix, review and test assignment, without full chat history where supported. Serialize writers, including background jobs. Freeze inputs during read-only review. If independent agents are unavailable, preserve progress, give the user a minimal packet for a fresh session and report the blocked role. A change of role inside one chat cannot provide independent evidence.

## Implement, review, test

1. Capture entry state for the allowed paths. Have the implementer deliver the specific tasks and run relevant build or existing checks. Compare actual writes to the snapshot and the authorization. Include applicable [minimal-change criteria](references/minimal-change.md) when the design adds machinery.
2. After the writer and its jobs exit, freeze the changes and relevant requirements, tests and standards. Have an independent reviewer report on both documented standards and required behavior. One reviewer can cover both, or separate read-only reviewers can work in parallel. Record identities, scope, inputs and conclusions in the [review receipt](references/roles.md#review-receipts).
3. Adjudicate each finding. Record a reason for dismissal. Assign accepted issues to a fresh implementer, then re-review affected content. Unresolved behavioral decisions block the affected acceptance.
4. Give an independent tester the real entry point, expected outcomes and risks. Run applicable tests and add missing assertions within the allowed paths. Return product failures with reproduction evidence to the coordinator for repair and affected review. Follow a requested test-first order and keep the final verification independent. Use appropriate checks for a documentation phase.
5. Verify assertion reach, test inputs and actual outcomes. Mark a phase complete only when implementation, review decisions and required tests all hold. Record an implementation without required evidence as unverified, a known failure as incomplete and unavailable prerequisites as blocked with a release condition.

The coordinator handles scope changes. Trace the first failing caller before expanding a fix. Stop affected writers before reassigning narrowed work. A user stop ends dispatch and active writes.

## Resume and close

At interruption, record the last verified role, receipts, findings and next action in the original task. On resumption, confirm writers have exited. Compare the original reviewed inputs, current code, contracts, tests and environment. The bundled [receipt checker](scripts/check_review.py) can compare recorded files. Inspect new or deleted files separately. An update to a progress note should not invalidate unrelated evidence.

Resume at the first missing role. If review is current and only testing is missing, send a tester. Preserve valid conclusions when only part of the input changed. When a receipt or identity cannot be verified, obtain the missing evidence. Give successors and the final phase the revised scope of pending verification.

Exercise the combined feature in the final phase through its actual user entry point. Record when, where and how it ran, the input, actual behavior and limits. Before closing, confirm agents and jobs have finished. Report per-phase status, both review conclusions, test outcomes, outstanding work, evidence and Git state.
