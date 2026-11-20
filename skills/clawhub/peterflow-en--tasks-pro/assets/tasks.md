# Feature execution plan

## Shared context

- Workspace and documents: Specify paths and their working directories.
- Goal, source decisions and scope: Link existing sections.
- Rules and constraints: Include applicable standards, allowed writes and test conditions.
- Final Phase: P002

## Phase P001: First independent result

- Goal and basis: Name the behavior and requirement.
- Dependencies: none
- Status: incomplete
- Read now: Existing files and sections.
- Deliver to successors: Artifact, public entry point and evidence location.
- Implementer may write: List existing and new files separately.
- Acceptance: Observable behavior including relevant boundaries.
- Check: Working directory, operation and expected result.
- Record: Coordinator updates this list from actual receipts. Link longer evidence if needed.

### Tasks

- [ ] T001 Implement the named behavior.
  - Dependencies: none
- [ ] T002 Obtain independent review and required tests.
  - Dependencies: T001

## Phase P002: Integration and cumulative acceptance

- Goal and basis: Downstream behavior and complete user outcome.
- Dependencies: P001
- Status: incomplete
- Read now and at handoff: Name the P001 artifact, how to use it and where its evidence lives.
- Implementer may write: Include the integration point.
- Acceptance: Exercise the user entry point through both phases and observe the expected result.
- Check: Working directory, input, operation and expected end result.
- Record: Coordinator links the review, tests and cumulative result here.

### Tasks

- [ ] T003 Connect the downstream behavior.
  - Dependencies: none
- [ ] T004 Run independent review, tests and cumulative acceptance.
  - Dependencies: T003
