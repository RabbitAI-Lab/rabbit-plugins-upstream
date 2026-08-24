## Description:

WP Multitool guides agents through WordPress site health audits, performance diagnostics, database cleanup, autoload tuning, slow query review, wp-config management, image controls, frontend speed fixes, and server diagnostics using WP-CLI and the optional commercial WP Multitool plugin.

This skill is ready for commercial/non-commercial use.

## Publisher:

[marcindudekdev](https://clawhub.ai/user/marcindudekdev)

### License/Terms of Use:

MIT-0

## Use Case:

External WordPress site owners, developers, and operators use this skill to inspect site health, identify performance bottlenecks, read WP Multitool plugin diagnostics, and prepare confirmation-gated cleanup or configuration changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write operations can delete or modify WordPress data, database tables, wp-config.php, or plugin options.

Mitigation: Confirm the target site, backup status, and intended change before allowing write commands such as transient deletion, revision cleanup, table optimization, wp-config edits, or WP Multitool cleanup and frontend toggles.

Risk: Activating the WP Multitool plugin changes the target WordPress site state.

Mitigation: Treat plugin activation as a confirmation-required change and verify that the user intends to activate the plugin on the selected site.

Risk: Diagnostics can expose operational metadata about a WordPress site.

Mitigation: Use only aggregate or non-sensitive diagnostic outputs, avoid secret configuration values, and keep command output for the user's immediate review.

## Reference(s):

- [WP Multitool Homepage](https://wpmultitool.com)
- [ClawHub Skill Page](https://clawhub.ai/marcindudekdev/skills/wp-multi-tool)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash code blocks and WP-CLI command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe JSON output modes for supported WP-CLI commands; write operations require user confirmation.]

## Skill Version(s):

1.9.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
