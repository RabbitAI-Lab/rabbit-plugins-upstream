## Description:

WordPress site health audit, performance optimization, database cleanup, autoload tuning, slow query detection, wp-config management, image size control, frontend speed fixes, and server diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[marcindudekdev](https://clawhub.ai/user/marcindudekdev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site maintainers, and WordPress operators use this skill to audit site health, inspect performance bottlenecks, and propose WP-CLI based optimization or cleanup actions. Read-only diagnostics can run on any WordPress site with WP-CLI, while WP Multitool plugin commands require the paid plugin to be installed and active.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes site-changing WordPress actions, including cleanup, wp-config edits, frontend option toggles, plugin activation, and database optimization.

Mitigation: Require explicit user approval before any write operation, and recommend a database export or equivalent backup before actions that modify or delete data.

Risk: Plugin activation is a site-changing action that the security summary flags as not clearly covered by confirmation guidance.

Mitigation: Treat plugin activation like other write operations and ask for explicit confirmation before running it.

## Reference(s):

- [WP Multitool Homepage](https://wpmultitool.com)
- [ClawHub Skill Page](https://clawhub.ai/marcindudekdev/skills/wp-multi-tool)
- [Publisher Profile](https://clawhub.ai/user/marcindudekdev)

## Skill Output:

**Output Type(s):** [Analysis, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash code blocks and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require WP-CLI; write operations require explicit user confirmation and should be preceded by a backup when data may be changed or deleted.]

## Skill Version(s):

1.9.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
