# Product UX Loop

## Contents

- [Outcome](#outcome)
- [Before implementation: experience contract](#before-implementation-experience-contract)
- [Flow design principles](#flow-design-principles)
- [Decision audit](#decision-audit)
- [Agent-mediated flows](#agent-mediated-flows)
- [After implementation: scenario verification](#after-implementation-scenario-verification)
- [Findings format](#findings-format)
- [Return criteria](#return-criteria)


## Outcome

Define and validate a coherent user journey in which the intended user can complete the contracted job in the intended context. The user should understand where they are, what they can do, what will happen, and how to recover.

This loop begins before implementation and returns after implementation for behavioral verification.

## Before implementation: experience contract

Identify:

- primary user
- user job and desired outcome
- entry point and prior context
- primary path
- decisions the user must make
- information required at each decision
- assumptions the product currently makes
- completion signal
- failure and recovery paths
- permissions and trust boundaries
- mobile constraints
- existing product language and conventions

Write a compact experience contract:

```text
Primary user:
Job to complete:
Entry point:
Primary path:
Primary action:
Required decisions:
Information required before each decision:
Loading state:
Empty state:
Validation state:
Error and recovery:
Permission state:
Success state:
Destructive action and undo:
Mobile behavior:
Accessibility expectations:
Must preserve:
Must avoid:
```

## Flow design principles

- Optimize for the user's goal, not the database schema.
- Make the primary action clear.
- Delay secondary configuration until it is needed.
- Use familiar interaction patterns unless a new pattern solves a real problem.
- Explain consequences before consequential actions.
- Preserve context across errors.
- Make success observable.
- Make incomplete or pending work visible.
- Avoid forcing users to infer system state.
- Avoid a step merely because the backend has a separate endpoint.
- Avoid dashboards when the user needs a guided action.
- Avoid modals for complex or recoverable workflows.

## Decision audit

For every user decision, ask:

- Does the user have enough information?
- Is the decision necessary now?
- Can the system choose a safe default?
- Is the consequence reversible?
- Does the label describe the consequence?
- Does the user know what happens next?

Remove decisions that do not materially help the user's goal.

## Agent-mediated flows

When an agent performs work for the user, define:

- what the agent may decide
- what requires confirmation
- what evidence the user sees
- how changes are explained
- how the user can inspect, edit, undo, or retry
- how uncertainty and partial completion are shown
- what remains owned by the user

Do not optimize only for agent execution. Preserve human understanding, verification, and control.

## After implementation: scenario verification

Exercise the real flow from a fresh or realistic state.

Verify:

- first-view comprehension
- entry and exit points
- primary action visibility
- decision ordering
- labels and consequences
- progress and system status
- error recovery without lost work
- success confirmation
- back, cancel, retry, and undo behavior
- mobile path
- consistency with the experience contract

Use representative scenarios:

1. New user with no data
2. Returning user with existing data
3. Invalid input
4. Network or server failure
5. Permission failure
6. Partial or delayed completion
7. Destructive action

Use only scenarios relevant to the feature.

## Findings format

Report concrete failures:

```text
Scenario:
Observed user state:
Expected understanding or action:
Observed friction:
Evidence:
Impact:
Recommended correction:
```

Avoid vague findings such as `make it intuitive`.

## Return criteria

Return `PASS` when the experience contract is implemented and representative scenarios show the intended user can understand, complete, and recover from the job. Report `OUTCOME VALIDATED` only when that behavior is observed; otherwise report `ARTIFACT VERIFIED` with the validation gap.

Return `REWORK_REQUIRED` when a material flow or state fails.
Return `BLOCKED` when the running product cannot be exercised.
Return `NEEDS_HUMAN_JUDGMENT` when product priorities or audience assumptions remain unresolved.
