## Description:

Helps developers plan software implementation, choose an appropriate planning depth, and preserve decisions and next steps when work spans phases or sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to turn software goals into actionable implementation plans, including scope, phased tasks, verification, and recovery state when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Starting a durable plan may create or update .plan/task_plan.md and add .plan/ to .gitignore; an existing plan could be displaced if overwritten.

Mitigation: Review the existing plan before starting a new one, resolve conflicting unfinished work, and use --force only after explicitly deciding which plan to keep.

## Reference(s):

- [ia-planning on ClawHub](https://clawhub.ai/iliaal/skills/compound-eng-planning)
- [Plan format](references/plan-format.md)
- [Goal definition](references/goal-definition.md)
- [Task design](references/task-design.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Files, Shell commands]

**Output Format:** [Inline plan or Markdown planning file with optional setup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A durable plan may be saved to .plan/task_plan.md or a project-specific planning location.]

## Skill Version(s):

5.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
