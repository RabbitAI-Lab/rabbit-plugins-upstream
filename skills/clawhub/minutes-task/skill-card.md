## Description:

Guides an agent to create Windows Task Scheduler jobs and supporting scripts for tasks that must run every N minutes when WorkBuddy's built-in scheduler cannot represent minute-level intervals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eddie4xioshi-netizen](https://clawhub.ai/user/eddie4xioshi-netizen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations users use this skill to set up recurring Windows tasks, generate a runnable script, test it, register it with Task Scheduler, and verify future runs. It is intended for minute-level automation such as polling, notifications, backups, and similar local recurring work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create persistent Windows scheduled tasks that continue running after the agent session ends.

Mitigation: Require the agent to show the task name, script path, command, trigger interval, and first run time before registration, and provide the exact disable and delete commands after creation.

Risk: A generated scheduled script may run unintended local actions repeatedly if the task content, interval, or overwrite behavior is not explicit.

Mitigation: Confirm the task content and interval with the user, test the script once in the foreground, use a unique task name, write logs beside the script, and show any overwrite or delete action before applying it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/eddie4xioshi-netizen/skills/minutes-task)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Python and PowerShell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Windows-oriented task setup instructions, script templates, verification commands, and lifecycle management commands.]

## Skill Version(s):

1.0.0 (source: server release metadata and target metadata; artifact frontmatter/config report 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
