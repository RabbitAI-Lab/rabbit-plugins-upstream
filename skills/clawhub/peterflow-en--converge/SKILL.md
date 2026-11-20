---
name: converge
description: Compare current implementation and test evidence against each goal before closing a phase or feature. Return gaps to the original plan or task list.
---

# Check what remains

Use the current goals, plan or task list, implementation and evidence. Include checked-off tasks. Follow project rules, applicable standards and the user's scope. Future plans are outside this review.

For each goal trace its source → current user entry point → assertion and observed result → status → place to resume. Open the code to confirm the path is connected. Check what the test actually ran, under which version, configuration and environment. If file digests were recorded, recompute them in the recorded working directory. Compare acceptance text separately from progress updates. Identify stale evidence and retain conclusions supported independently.

| Status | When to use it |
| --- | --- |
| Complete | Current behavior meets the goal and required checks have applicable evidence. |
| Incomplete | A specific implementation gap, inconsistency or observed failure remains. |
| Unverified | Implementation appears present but a required check is missing or stale. |
| Blocked | A needed environment, access, decision or executor is unavailable. Give the release condition. |

Report the basis, current evidence and next action. Within authorization, reopen the original task or plan where the gap belongs. For small work that can be a chat plan. For medium work preserve phase and task IDs, completed portions and historical evidence. For large work update the affected unit and the final cumulative check, including any missing independent handoff. Keep older U IDs or flat lists. A repair depends on the artifacts it needs to operate, not a passing check that is waiting for the repair.

Honor report-only requests. Reuse existing pending work, link longer evidence and leave correct records alone. Distinguish missing behavior from missing proof. Keep every unresolved necessary goal visible in the phase and overall conclusion. Return the next executable action and the limits of the evidence.
