## Description:

Guides front-line deployment engineers through enterprise AI workflow discovery, deployment planning, audit, and continuous improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kongfangxun](https://clawhub.ai/user/kongfangxun)

### License/Terms of Use:

MIT-0

## Use Case:

Front-line deployment engineers and enterprise IT teams use this skill to map business workflows, identify suitable AI-assisted tasks, plan deployment, and review ongoing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation may change local agent configuration and expose broad enterprise tooling.

Mitigation: Review the installer and tool implementation before use; restrict exposed tools and roles, and keep directory allowlists empty until needed.

Risk: Persistent hooks, scheduled checks, and audit logs may affect ongoing operations.

Mitigation: Confirm enabled hooks and background checks before deployment, and review their audit-log retention.

Risk: Enterprise tasks and knowledge records may contain credentials or sensitive data.

Mitigation: Avoid placing credentials or regulated data in task logs, reflections, and knowledge files.

## Reference(s):

- [FDE Skill on ClawHub](https://clawhub.ai/kongfangxun/skills/sofagent)
- [FDE workflow entry guide](artifact/skills/01-entry.md)
- [FDE workflow delivery guide](artifact/skills/04-deliver.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with workflow plans and inline commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include workflow maps, audit summaries, deployment handoff instructions, and custom skill guidance.]

## Skill Version(s):

1.5.2 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
