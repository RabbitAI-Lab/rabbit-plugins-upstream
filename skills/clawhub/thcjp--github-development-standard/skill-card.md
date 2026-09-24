## Description:

Provides a Chinese-language workflow for GitHub project development standards, including code review, development norms, project management, and automation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to guide GitHub project workflows, code review, development standards, project management, and automation planning. It is intended for repositories or tasks with a clear technical stack.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may propose shell commands or repository file changes with broad impact.

Mitigation: Run it only on trusted repositories, review each command and file change before execution, and use a sandbox or disposable branch for higher-risk changes.

Risk: The skill requests read, execute, and write capabilities without detailed operational limits in the artifact.

Mitigation: Grant the minimum permissions needed for the current task and require explicit approval before write or execute actions.

Risk: API keys or credentials may be involved in setup or troubleshooting workflows.

Mitigation: Avoid sharing credentials unless the exact operation and destination are clear, prefer environment variables, and verify that generated logs or outputs do not expose secrets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/github-development-standard)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose repository file changes, Git operations, code review findings, quality scores, and configuration steps.]

## Skill Version(s):

1.0.2 (source: server release evidence and target metadata; artifact frontmatter lists 2.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
