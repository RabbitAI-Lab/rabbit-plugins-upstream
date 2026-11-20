# Stage checks and the synchronization point

Stages describe responsibilities of artifacts. One short document can serve several. A stage is independent of a Phase in the task list.

| Stage | Check before proceeding along an affected dependency |
| --- | --- |
| `requirements` | Every confirmed assertion has an authoritative home. Current contracts and acceptance criteria agree and superseded semantics have left current requirements. |
| `design` | Affected interfaces, architecture, data, state and compatibility choices implement the requirement. Each choice has a source, with one current design. |
| `tasks` | Each affected behavior has executable work, acceptance, valid ownership and dependencies. Apply [task reconciliation](task-rebuild.md). |
| `implementation` | Code, configuration, migrations and tests express the new behavior. Follow shared fields through indirect readers and verify preserved behavior. Run required build, static and behavior checks. Check removed branches and old assertions. |
| `validation` | Current review, traceability and delivery evidence cover the actual inputs, outcomes and limitations. |

`target_stage` limits this execution, including its preceding stages. `completion_stage` sets closure for the whole round. A changed implemented feature needs at least its implementation and required tests reconciled. If existing delivery evidence goes stale, include validation. A documentation-only change without downstream impact can end at requirements or design. Record the actual external verification obligations and their authorization.

A segmented round keeps the same contract. Persist its deepest synchronized stage and identify stale downstream artifacts in the native project status. If none exists, use a short temporary “Reconciliation status” in the main spec. Restore normal current-state reporting after full reconciliation. A later stage may expose a defect upstream: correct it and recheck affected downstream work. A request to stop earlier does not reduce the full completion stage.

Extend the known artifact set directly when the new path is within the existing assertion, stage and writable roots. Changed behavior, new writable roots, deeper execution, new migration/data risk or substantial undisclosed deletion needs a decision.

Record old terms, fields and configuration keys **and** behavioral signatures such as an old fallback, serialization shape or state transition. Inspect live references, generated consumers, tests and code. Exclude caches and VCS internals. Classify each hit as replaced, proven historical, unrelated or explicitly retained by a current requirement. Zero text matches alone cannot demonstrate removal of old behavior.

Run authorized baseline checks with command, environment, exit status and observation. Static evidence has its own scope. A new, related or unattributed failure blocks relevant acceptance. For a pre-existing unrelated failure keep baseline and attribution evidence. A required check that could not run remains blocked. Pause when the current execution limit is reached and retain both the full endpoint and journal.
