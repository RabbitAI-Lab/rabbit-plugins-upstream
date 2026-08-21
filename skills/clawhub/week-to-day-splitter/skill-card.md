## Description:

周计划自动分配日程器 converts a tagged weekly work plan into five Markdown daily plans and supports cron workflows for copying weekly plans, merging checked progress, and sending optional Feishu reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seairteng](https://clawhub.ai/user/seairteng)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and operators use this skill to split a structured Monday-Friday weekly work plan into dated daily Markdown plans, then optionally automate weekly copying, progress merge-back, and Feishu reminders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recurring automation can rewrite weekly and daily planning files.

Mitigation: Review the configured write paths, keep backups or dry-run output before enabling cron jobs, and disable scheduled jobs when automatic edits are not wanted.

Risk: Optional Feishu/private messaging can send full daily-plan contents outside the local workspace.

Mitigation: Use only non-sensitive plans or a trusted internal Feishu setup, protect webhook credentials, and disable push cron jobs if external delivery is unnecessary.

Risk: The security review notes important scope and privacy contradictions.

Mitigation: Treat the security guidance as authoritative during installation and resolve write-scope and privacy wording before operational use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/seairteng/skills/week-to-day-splitter)
- [SKILL.md](artifact/SKILL.md)
- [README.md](artifact/README.md)
- [CHANGELOG.md](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown files with inline shell commands and plain-text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces five daily plan files, updated weekly plan content, and optional scheduled Feishu message content.]

## Skill Version(s):

1.1.0 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
