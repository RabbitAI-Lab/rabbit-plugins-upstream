## Description:

WP Multitool supports WordPress site health audits, performance optimization, database cleanup, autoload tuning, slow query detection, wp-config management, image size control, frontend speed fixes, and server diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[marcindudekdev](https://clawhub.ai/user/marcindudekdev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and WordPress site operators use this skill to audit site health, inspect performance bottlenecks, and apply confirmed WP-CLI cleanup or configuration actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Production WordPress operations may delete database rows, optimize tables, modify wp-config.php, or change plugin options.

Mitigation: Require explicit user approval before every write operation and recommend a database export before destructive cleanup.

Risk: Plugin activation changes site state and may affect production behavior.

Mitigation: Treat plugin activation as a state-changing action that requires explicit user approval before execution.

Risk: Diagnostics depend on WP-CLI access and may behave differently on sites with custom database prefixes or missing paid-plugin commands.

Mitigation: Start with read-only checks, detect the database prefix with WP-CLI before SQL queries, and treat unavailable plugin modules as not checked.

## Reference(s):

- [WP Multitool homepage](https://wpmultitool.com)
- [ClawHub skill page](https://clawhub.ai/marcindudekdev/skills/wp-multi-tool)
- [Publisher profile](https://clawhub.ai/user/marcindudekdev)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with WP-CLI and SQL command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only diagnostics may include JSON output from WP-CLI; write operations require explicit user confirmation.]

## Skill Version(s):

1.9.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
