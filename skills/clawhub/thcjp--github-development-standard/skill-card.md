## Description:

Provides a GitHub project development standards workflow for code review, project management, and automated development guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to guide GitHub-centered development workflows, including code review, development standards, project management, and local automation tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide broad repository file edits and local command execution.

Mitigation: Use it only in trusted repositories, review proposed file changes, and require explicit confirmation before deployment, CI/CD, or other commands that affect external systems.

Risk: The skill references credential and API-key use.

Mitigation: Provide credentials through environment variables or a secret manager, avoid committing secrets, and redact sensitive values from logs and shared outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/github-development-standard)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown, JSON examples, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include code review findings, workflow steps, configuration guidance, command suggestions, and structured status output.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
