## Description:

Provides WordPress site diagnostics, performance analysis, and optional database cleanup and configuration changes through WP-CLI, with plugin-specific monitoring available when WP Multitool is installed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[marcindudekdev](https://clawhub.ai/user/marcindudekdev)

### License/Terms of Use:

MIT-0

## Use Case:

WordPress administrators and developers use this skill to inspect site health, database and performance indicators, then plan or apply explicitly confirmed cleanup and configuration changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Revision cleanup can erase history beyond the five-revision threshold, especially in the plugin-free cleanup workflow.

Mitigation: Do not use plugin-free revision cleanup until it preserves five revisions per post and previews the exact deletions; verify a restorable database backup before cleanup.

Risk: Cleanup and configuration commands can delete or modify site data.

Mitigation: Start with diagnostics, require explicit user approval for write operations, and verify a restorable backup before cleanup.

## Reference(s):

- [WP Multitool website](https://wpmultitool.com)
- [ClawHub release](https://clawhub.ai/marcindudekdev/skills/wp-multi-tool)

## Skill Output:

**Output Type(s):** [Analysis, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline WP-CLI and SQL code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Combines read-only diagnostics with write commands that require user confirmation.]

## Skill Version(s):

1.9.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
