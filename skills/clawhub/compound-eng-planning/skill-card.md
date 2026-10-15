## Description:

Helps developers plan software implementation, with optional local files to preserve decisions and progress across sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to break software implementation work into verifiable steps and preserve a working plan when decisions or multiple phases make an inline plan insufficient.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Creating a durable plan may replace an existing plan or modify .gitignore.

Mitigation: Review any existing plan and .gitignore before scaffolding; force an overwrite only after deciding which plan to keep.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-planning)
- [Plan format](references/plan-format.md)
- [Task design](references/task-design.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown plan or inline planning guidance; optionally a local plan file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create .plan/task_plan.md and update .gitignore when scaffolding a durable plan.]

## Skill Version(s):

5.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
