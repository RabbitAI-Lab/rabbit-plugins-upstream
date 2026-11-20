---
name: tasks-pro
description: Split a large change into phases that fresh implementers, reviewers and testers can pick up independently. Include ownership, handoff inputs and cumulative acceptance.
---

# Design independently executable phases

A phase is the execution unit. Keep its tasks, status and evidence in the original task list. Work from the existing goal, design, code, applicable project rules, `.peterflow/standards/` and prior verification. Use an existing equivalent location or a new `.peterflow/specs/<topic>/tasks.md`. Fill in only missing decisions that affect the split. Record the effect of an unresolved product decision.

1. Map behaviors, external contracts and checks to requirements. Cut by observable outcome. Split off a shared prerequisite only when it has a deliverable and a check of its own.
2. Give each phase its stable ID, scope, immediate dependencies, requirement, acceptance and assigned tasks. Distinguish files available to read now, outputs promised by predecessors and files this phase may create. Open the required inputs before handoff. State exactly where the next executor can consume a predecessor's output and find its acceptance evidence.
3. Name the allowed writes for each implementer. Only the coordinator updates the original task list. Budget for reading, diagnosing, review and testing. Where several systems are unknown, define a bounded investigation with a deliverable or split the phase.
4. Assign one final phase that depends transitively on all necessary phases. Include a task that exercises their integration through a user entry point. Specify the input, predecessor capabilities it traverses and the observable outcome.
5. Preserve existing unit IDs (including U numbers), task IDs, evidence and completed work. Replan only what remains. Reopen affected verification explicitly. A repair can depend on an implementable artifact, never on the acceptance check waiting for the repair.

Use [the phase template](assets/tasks.md) when starting fresh. A task belongs to one phase and inherits that phase's prerequisites. The coordinator distinguishes **incomplete**, **unverified**, **blocked** (state the release condition), and **complete** (tasks, independent review and required tests supported by current evidence).

Run `python3 <skill-dir>/scripts/check_dependencies.py --require-final <tasks.md>` on the standard format. [The checker](scripts/check_dependencies.py) checks task dependencies, treats a dependency on another phase’s task as a dependency on that phase, and verifies that the final phase depends on every other phase. Read the integration task to verify that it actually tests the combined behavior. Inspect legacy formats in place. List the first ready phase, prerequisite artifacts and blockers. Create resource directories only when saving a real file.
