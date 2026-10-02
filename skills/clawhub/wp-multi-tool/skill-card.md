## Description:

Guides WordPress site health checks and performance diagnostics, with optional WP-CLI cleanup and configuration changes requiring user confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[marcindudekdev](https://clawhub.ai/user/marcindudekdev)

### License/Terms of Use:

MIT-0

## Use Case:

WordPress site administrators and developers use this skill to audit site health, investigate performance problems, and plan or perform confirmed maintenance with WP-CLI. Plugin-specific monitoring commands require the paid WP Multitool plugin; basic diagnostics do not.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cleanup commands can permanently delete site data.

Mitigation: Confirm each write action with the user and export the database before cleanup.

Risk: Optimization and configuration changes can affect site availability or behavior.

Mitigation: Review the intended change and confirm it before running table optimization, wp-config edits, or plugin option changes.

## Reference(s):

- [WP Multitool skill listing](https://clawhub.ai/marcindudekdev/skills/wp-multi-tool)
- [WP Multitool website and documentation](https://wpmultitool.com)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Text or Markdown with WP-CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only diagnostics work without the paid plugin; plugin-specific monitoring requires it.]

## Skill Version(s):

1.9.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
