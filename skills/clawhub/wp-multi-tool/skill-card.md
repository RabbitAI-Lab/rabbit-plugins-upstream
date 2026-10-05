## Description:

Guides WordPress site health audits, performance diagnostics, and approved optimization through WP-CLI, with optional WP Multitool plugin commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[marcindudekdev](https://clawhub.ai/user/marcindudekdev)

### License/Terms of Use:

MIT-0

## Use Case:

WordPress developers and site administrators use this skill to diagnose performance, inspect database health, and propose or perform approved cleanup and configuration changes. Its read-only diagnostics work without the optional paid plugin.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Activating the plugin without approval can change a live WordPress site.

Mitigation: Check plugin status first and request explicit user approval before running activation.

Risk: Cleanup and configuration commands can delete site data or alter frontend behavior.

Mitigation: Present proposed changes, obtain explicit approval, and back up the site before destructive operations.

## Reference(s):

- [WP Multitool website and documentation](https://wpmultitool.com)
- [WP Multitool skill on ClawHub](https://clawhub.ai/marcindudekdev/skills/wp-multi-tool)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with WP-CLI commands and diagnostic findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some plugin commands support JSON output; write operations require user confirmation.]

## Skill Version(s):

1.9.11 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
