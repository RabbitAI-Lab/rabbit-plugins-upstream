## Description:

Siluzan TSO helps agents route and execute advertising account operations, campaign planning, market analysis, website diagnosis, and reporting workflows across Google, Meta, Bing, Yandex, TikTok, and related Siluzan tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sigedev01-bit](https://clawhub.ai/user/sigedev01-bit)

### License/Terms of Use:

MIT-0

## Use Case:

External users and advertising operations teams use this skill to manage Siluzan TSO account, finance, permission, campaign, optimization, and reporting workflows. It is intended for agents that can run the Siluzan CLI, read the bundled routing references, and produce reports or controlled advertising actions from verified CLI output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide actions that affect real advertising accounts, budgets, finance records, permissions, and account status.

Mitigation: Require explicit user confirmation and review command intent before any live write, finance, permission, or account-closing action.

Risk: The installer can change the npm registry and register the skill globally across multiple AI client directories.

Mitigation: Review the installer before running it, install only where intended, and restore npm registry settings if they were changed.

Risk: The skill relies on persistent Siluzan CLI credentials or environment variables for authenticated account access.

Mitigation: Use scoped or short-lived credentials where possible, avoid exposing credentials in logs, and clear or rotate credentials when access is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sigedev01-bit/skills/siluzan-tso)
- [Installation and configuration](artifact/references/core/setup.md)
- [Intent routing](artifact/references/core/intent-routing.md)
- [Analysis and reporting playbooks](artifact/references/core/playbooks.md)
- [Operations workflows](artifact/references/core/workflows.md)
- [Account, balance, and stats workflows](artifact/references/accounts/accounts-balance-stats.md)
- [Google Ads workflows](artifact/references/google-ads/google-ads.md)
- [Meta Ads workflows](artifact/references/meta-ads/meta-ads.md)
- [Report templates](artifact/report-templates/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown, JSON, HTML, Excel, shell commands, and concise user-facing guidance depending on the routed workflow]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce files and reports through the Siluzan CLI; live account, finance, permission, and advertising write operations require user confirmation.]

## Skill Version(s):

1.1.50 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
