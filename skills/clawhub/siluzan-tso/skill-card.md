## Description:

Siluzan TSO routes agents through advertising account operations, campaign workflows, market and website analysis, and report generation for Google, Bing, Yandex, TikTok, and Meta Ads using the Siluzan TSO CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sigedev01-bit](https://clawhub.ai/user/sigedev01-bit)

### License/Terms of Use:

MIT-0

## Use Case:

External users and advertising operators use this skill to manage Siluzan TSO advertising accounts, prepare supported Google Search, Google PMax, and Meta lead-generation workflows, analyze markets or websites, and generate platform reports through CLI-backed steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer, persistent registration, and credential-handling behavior are broad enough to require review before installation.

Mitigation: Install only from a trusted publisher and prefer a manual, single-client or workspace-local install over a one-click global installer.

Risk: The skill can guide campaign, finance, permission, and deletion operations that may affect live advertising accounts.

Mitigation: Review every proposed action, configuration file, and CLI command before confirming any write or deletion operation.

Risk: Authentication may involve SMS codes, API keys, or JWTs.

Mitigation: Do not paste SMS codes, API keys, or JWTs into chat; use local configuration or environment variables where possible.

Risk: Lead exports and advertising reports may contain sensitive business or personal data.

Mitigation: Handle raw exports as sensitive data and avoid unnecessary sharing in chat transcripts, logs, or generated reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sigedev01-bit/skills/siluzan-tso)
- [Skill definition](artifact/SKILL.md)
- [Documentation directory](artifact/AGENTS.md)
- [Intent routing](artifact/references/core/intent-routing.md)
- [Core playbooks](artifact/references/core/playbooks.md)
- [Core workflows](artifact/references/core/workflows.md)
- [Setup and authentication](artifact/references/core/setup.md)
- [Account operations](artifact/references/accounts/accounts.md)
- [Google Ads workflows](artifact/references/google-ads/google-ads.md)
- [Meta Ads workflows](artifact/references/meta-ads/meta-ads.md)
- [Market analysis guide](artifact/references/analytics/market-analysis-guide.md)
- [Website diagnosis guide](artifact/references/analytics/website-diagnosis-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON, HTML, XLSX, and shell command guidance depending on the routed workflow]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to produce reports, templates, campaign configuration files, and CLI execution steps; write operations require explicit user review and confirmation.]

## Skill Version(s):

1.1.52 (source: server release evidence and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
