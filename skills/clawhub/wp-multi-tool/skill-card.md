## Description:

Provides WordPress site-health and performance diagnostics, database cleanup and optimization guidance, and WP Multitool plugin workflows through WP-CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[marcindudekdev](https://clawhub.ai/user/marcindudekdev)

### License/Terms of Use:

MIT-0

## Use Case:

WordPress developers and site administrators use this skill to inspect site health and performance, review database and configuration issues, and apply selected optimizations using WP-CLI. Destructive or configuration-changing operations require explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The manual revision-cleanup fallback may delete more history than its stated retention target and may be difficult to reverse.

Mitigation: Avoid that fallback until it is verified to preserve the intended revisions; before any cleanup, confirm a restorable backup, review the exact deletion scope, and obtain explicit user approval.

Risk: A diagnostic query may return more detail than the skill's stated data limits.

Mitigation: Prefer the minimum necessary read-only checks, review and redact results before presenting them, and do not retain or share diagnostic output. Omit profiler URLs.

Risk: Plugin activation, cleanup, and configuration changes can affect site behavior or remove data.

Mitigation: Get explicit user approval for activation and each write operation, including diagnostic-log deletion, after explaining its scope and confirming a recoverable backup where data may be changed.

## Reference(s):

- [WP Multitool Website](https://wpmultitool.com)
- [ClawHub Skill Release](https://clawhub.ai/marcindudekdev/skills/wp-multi-tool)
- [Publisher Profile](https://clawhub.ai/user/marcindudekdev)
- [Author Website](https://marcindudek.dev)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown diagnostic summaries and recommendations with WP-CLI command examples; commands may return text or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only diagnostics and recommendations, plus user-confirmed write operations.]

## Skill Version(s):

1.9.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
