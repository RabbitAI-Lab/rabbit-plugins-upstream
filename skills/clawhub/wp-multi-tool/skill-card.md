## Description:

Guides WordPress site health checks and performance diagnostics, with optional WP Multitool monitoring and confirmed cleanup or configuration changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[marcindudekdev](https://clawhub.ai/user/marcindudekdev)

### License/Terms of Use:

MIT-0

## Use Case:

WordPress site administrators and developers use this skill to diagnose database and performance issues, review optional plugin monitoring, and plan confirmed optimization steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Activating the plugin changes a live site, although its troubleshooting command does not explicitly request confirmation.

Mitigation: Treat plugin activation as a write action and obtain explicit user confirmation before running it.

Risk: Cleanup and forced revision deletion can permanently remove data; table optimization may briefly lock tables.

Mitigation: Review the target site, make a database backup, and obtain explicit confirmation before cleanup or optimization.

Risk: Changing wp-config.php or enabling frontend optimizations can alter production behavior.

Mitigation: Back up configuration, review the proposed change, and require explicit confirmation before applying it.

## Reference(s):

- [WP Multitool website and documentation](https://wpmultitool.com)
- [WP Multitool ClawHub release](https://clawhub.ai/marcindudekdev/skills/wp-multi-tool)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline WP-CLI and SQL commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only diagnostics work without the paid plugin; plugin monitoring requires installation. Site changes require confirmation.]

## Skill Version(s):

1.9.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
