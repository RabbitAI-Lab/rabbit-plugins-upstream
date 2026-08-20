## Description:

Supports Tasker docstore task management for task lists, due and overdue reminders, status updates, and workflow automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and teams use this skill to manage Tasker tasks, including filtering task lists, updating status, tracking due dates, and preparing weekly plans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad local read, write, and command execution tools without tight task-specific scoping.

Mitigation: Review the skill before installing, run it in a constrained agent environment, and approve only user-directed Tasker-specific actions.

Risk: Credentials or local file paths could be exposed if supplied unnecessarily during task-management workflows.

Mitigation: Avoid providing credentials or file paths unless they are required for a clear Tasker-specific action, and prefer environment variables for secrets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/task)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose task-management actions, configuration steps, and structured task summaries.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
