## Description:

Task Executor gives coding agents a disciplined loop for handling one defined task: understand the request, inspect relevant files, plan, execute incrementally, validate each change, and track progress, risks, and assumptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to keep a single concrete implementation task legible and resumable through structured status updates, inspected context, approval-gated planning, incremental changes, and validation after each change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate for concrete implementation requests even when not explicitly named.

Mitigation: Use it when a stricter execution workflow is desired, and switch to a lighter workflow for small edits, exploratory design, or fuzzy requirements.

Risk: Larger tasks may involve sub-agents or documentation lookups during inspection.

Mitigation: Review the inspection plan and progress sections before approving implementation work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dennisrongo/skills/task-executor)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown status reports with code, shell commands, configuration changes, and guidance as needed for the task.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a fixed Goal, Current understanding, Files to inspect, Plan, Progress, Risks, and Assumptions structure during execution.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
