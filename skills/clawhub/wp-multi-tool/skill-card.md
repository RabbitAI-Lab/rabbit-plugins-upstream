## Description:

Guides WordPress site diagnostics and performance optimization through WP-CLI, with optional plugin-assisted monitoring and cleanup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[marcindudekdev](https://clawhub.ai/user/marcindudekdev)

### License/Terms of Use:

MIT-0

## Use Case:

WordPress administrators and developers use this skill to audit site health, investigate database and frontend performance, and plan or run approved maintenance actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A troubleshooting command may activate the plugin and change live site behavior without explicit approval.

Mitigation: Require user approval before plugin activation and confirm the intended site and expected effects.

Risk: Cleanup and configuration commands can delete data or alter live site behavior.

Mitigation: Require approval for every write action and confirm a current backup before deletions or configuration changes.

## Reference(s):

- [WP Multitool skill on ClawHub](https://clawhub.ai/marcindudekdev/skills/wp-multi-tool)
- [WP Multitool website](https://wpmultitool.com)

## Skill Output:

**Output Type(s):** [Analysis, Shell commands, Configuration guidance]

**Output Format:** [Markdown with WP-CLI commands and site-health findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some plugin monitoring commands require the paid plugin; read-only diagnostics work without it.]

## Skill Version(s):

1.9.13 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
