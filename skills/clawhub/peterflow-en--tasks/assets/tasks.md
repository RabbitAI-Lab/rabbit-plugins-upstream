# Feature tasks

Link the plan and requirement. Edit the phases around the outcomes of this change. In a Dependencies field use `none` or comma-separated IDs. Task IDs are unique across phases.

## Phase P001: First observable capability

- Goal: Deliver the first usable behavior.
- Basis: Requirement and section.
- Dependencies: none
- Acceptance: An observable result from its public entry point.

### Tasks

- [ ] T001 Implement that behavior and run its direct self-check.
  - Dependencies: none
  - Acceptance: Give an input and the result to expect.
- [ ] T002 Run independent acceptance if it needs a separate task.
  - Dependencies: T001
  - Acceptance: Specify where to run it and what to observe.

## Phase P002: Connect the next capability

- Goal: Deliver the downstream behavior.
- Basis: Remaining requirement and combined outcome.
- Dependencies: P001
- Acceptance: A user sees the combined result.

### Tasks

- [ ] T003 Add the downstream behavior.
  - Dependencies: none
  - Acceptance: Specify its observable result.
- [ ] T004 Exercise the full entry point and relevant regressions.
  - Dependencies: T003
  - Acceptance: Record the operation, input and expected output.

## Results and remaining work

Record actual results under the original phase/task IDs. Identify failures, skipped checks and missing environments. Reopen the relevant task for remaining work.
