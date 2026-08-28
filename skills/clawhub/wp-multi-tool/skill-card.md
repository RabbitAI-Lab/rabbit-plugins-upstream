## Description:

Provides WordPress site health diagnostics, performance analysis, database cleanup guidance, WP-CLI commands, and plugin-specific checks for WP Multitool-managed sites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[marcindudekdev](https://clawhub.ai/user/marcindudekdev)

### License/Terms of Use:

MIT-0

## Use Case:

External WordPress developers, site administrators, and operations engineers use this skill to audit site health, identify performance bottlenecks, inspect WP Multitool plugin data, and prepare WP-CLI remediation steps. Destructive cleanup or configuration changes require explicit user confirmation and a recent database backup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: WP-CLI cleanup and configuration commands can delete WordPress data, modify wp-config.php, optimize database tables, or change plugin options.

Mitigation: Require explicit user confirmation and a recent database backup before any cleanup, wp-config change, table optimization, frontend toggle, or plugin activation command.

Risk: Plugin-specific diagnostics depend on WP Multitool being installed and active; unavailable modules may leave areas unchecked.

Mitigation: Check plugin availability before using wp multitool commands and treat unavailable module results as not checked rather than healthy.

## Reference(s):

- [WP Multitool Website](https://wpmultitool.com)
- [ClawHub Skill Page](https://clawhub.ai/marcindudekdev/skills/wp-multi-tool)
- [Publisher Profile](https://clawhub.ai/user/marcindudekdev)
- [Author Website](https://marcindudek.dev)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with WP-CLI and SQL command blocks; some commands may produce JSON output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires WP-CLI. Plugin-specific commands require the paid WP Multitool plugin to be installed and active.]

## Skill Version(s):

1.9.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
