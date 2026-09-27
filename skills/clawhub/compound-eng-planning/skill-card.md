## Description:

Helps developers plan software implementation, with optional file-based state for complex or multi-phase work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to define verifiable goals, break implementation into testable phases, and preserve decisions and next steps when work spans sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scaffolding a durable plan can change repository-local plan files and .gitignore.

Mitigation: Review proposed file changes and inspect existing plans before replacing or forcing an overwrite.

Risk: An unverified plan can omit requirements or present proposed checks as completed.

Mitigation: Confirm scope and acceptance criteria against the request, and record verification results only after running the checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-planning)
- [Goal definition](references/goal-definition.md)
- [Plan format](references/plan-format.md)
- [Task design](references/task-design.md)

## Skill Output:

**Output Type(s):** [Planning guidance, Markdown plans, Shell commands]

**Output Format:** [Markdown text or repository-local Markdown files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create .plan/task_plan.md and add .plan/ to .gitignore; formal plans may be placed in docs/plans/.]

## Skill Version(s):

5.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
