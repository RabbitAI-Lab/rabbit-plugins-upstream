## Description:

Guides WordPress site health and performance diagnostics and recommends WP-CLI maintenance actions, with optional monitoring data from the paid WP Multitool plugin.

This skill is ready for commercial/non-commercial use.

## Publisher:

[marcindudekdev](https://clawhub.ai/user/marcindudekdev)

### License/Terms of Use:

MIT-0

## Use Case:

WordPress site administrators and developers use this skill to audit site health, investigate performance issues, and plan database, configuration, and frontend maintenance. Read-only diagnostics work without the paid plugin; plugin-specific monitoring requires it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cleanup commands can permanently remove WordPress data.

Mitigation: Require an explicit backup and user confirmation before any deletion.

Risk: Configuration changes, table optimization, frontend toggles, or plugin activation can alter site behavior or availability.

Mitigation: Review the proposed change and require explicit user confirmation before executing it.

## Reference(s):

- [WP Multitool skill release](https://clawhub.ai/marcindudekdev/skills/wp-multi-tool)
- [WP Multitool website](https://wpmultitool.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with WP-CLI commands and site-health findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plugin read commands may return JSON; maintenance commands require explicit user confirmation.]

## Skill Version(s):

1.9.12 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
