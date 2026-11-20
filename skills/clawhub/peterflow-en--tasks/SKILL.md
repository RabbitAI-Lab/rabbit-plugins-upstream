---
name: tasks
description: Split an agreed design into phases and executable tasks with explicit dependencies and acceptance checks. Use for medium-sized changes or to update an existing task list.
---

# Turn a plan into tasks

Read the goal, design, current code entry points, applicable project rules and existing task list. Reuse their location and stable IDs. A goal and a short plan can be sufficient input. The default for a new list is `.peterflow/specs/<topic>/tasks.md`.

1. Group work by independently observable phase goals. Within a phase, give each task a deliverable and an entry point that checks it. Put a small change and its direct self-check together. If another task owns independent acceptance, name the input it needs. An implementation task must be finishable before the downstream check starts.
2. Give each phase a basis in the request, its immediate prerequisites and phase acceptance. A task belongs to one phase, has an ID unique across the list, and inherits the prerequisites of its phase. Record additional task dependencies explicitly. Parallel work also needs disjoint writes and compatible interfaces.
3. Walk forward from every requirement to a task and acceptance. Walk back from each task to its scope and owner. A phase finishes when its tasks and its own acceptance criteria hold. Record the particular dependency or decision blocking any other work.
4. Use [the task template](assets/tasks.md) for new lists. On the standard format run `python3 <skill-dir>/scripts/check_dependencies.py <tasks.md>`. [The checker](scripts/check_dependencies.py) finds duplicated IDs, missing ownership, unresolved references and cycles in the combined graph. Then read the prose for hidden waits between delivery and acceptance. Review legacy lists or custom formats in place and identify any limits of that check.

Keep completed work, old evidence and identifiers when regrouping tasks. Mark invalidated checks and say what must be rerun. Link long verification records from the task. Name a new design, reference, verification, delivery or shared-contract file only when the task actually needs it.

Report the list path, phase goals, dependency order, first ready task and unresolved decisions. Planning produces a checkable list. Record actual test results during implementation.
