## Description:

Software implementation planning with optional file-based persistence for requests that need a plan, unresolved architecture or scope decisions, or multi-phase recovery state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this workflow to decide when a durable implementation plan is needed, define concrete scope and acceptance criteria, and preserve planning state across multi-phase work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Durable planning can create or update local planning files, including .plan/task_plan.md and .gitignore.

Mitigation: Review any existing .plan/task_plan.md before forcing a new plan, and preserve unfinished work unless the user has resolved which plan wins.

Risk: A plan can introduce incorrect scope, weak acceptance criteria, or misleading implementation guidance.

Mitigation: Verify the plan against the user's requirements, keep acceptance criteria concrete, and review proposed tasks before implementation.

## Reference(s):

- [Execution & Decomposition Patterns](references/execution-and-methodology.md)
- [execution handoff](references/execution-handoff.md)
- [goal definition](references/goal-definition.md)
- [Operational Patterns](references/operational-patterns.md)
- [Plan Deepening](references/plan-deepening.md)
- [plan format](references/plan-format.md)
- [task design](references/task-design.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown plans and concise chat guidance with optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local planning files such as .plan/task_plan.md when durable state is appropriate.]

## Skill Version(s):

4.5.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
