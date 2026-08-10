## Description:

Manage Jira issues from the command line: read issues, run JQL searches, create issues, comment, assign owners, and transition workflow states for Jira Cloud, Server, or Data Center.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weiguang1017](https://clawhub.ai/user/weiguang1017)

### License/Terms of Use:

MIT

## Use Case:

Developers, engineers, and operations teams use this skill to query Jira tickets, run JQL searches, create bugs or tasks, add comments, assign owners, and move issues through workflows from an agent-driven CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create issues, add comments, assign owners, and transition Jira workflow states.

Mitigation: Require confirmation before write actions and grant the Jira token only the project permissions needed for the intended tasks.

Risk: A Jira token can expose or modify project data available to the configured account.

Mitigation: Use a least-privilege token, keep config files outside version control with restrictive permissions, and avoid placing tokens on the command line.

Risk: Implicit invocation is enabled, which can make write-capable Jira actions easier to trigger accidentally.

Mitigation: Disable implicit invocation or require explicit approval for create, comment, assign, and transition commands.

Risk: The dependency floor for requests may be stale for production environments.

Mitigation: Update and review the requests dependency range before production deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weiguang1017/skills/jira-devops-skill)
- [Server-resolved source repository](https://github.com/weiguang1017/jira-devops-skill)
- [Agent instructions](artifact/SKILL.md)
- [README](artifact/README.md)
- [Chinese user manual](artifact/使用手册.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON from the Jira CLI with agent-facing Markdown guidance and shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON on stdout and non-zero exit codes on failure.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
