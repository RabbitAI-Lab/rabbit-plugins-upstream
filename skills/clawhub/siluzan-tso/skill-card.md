## Description:

Siluzan TSO routes agents through advertising account management, campaign planning, reporting, market analysis, and operations workflows for Google, Meta, Bing, Yandex, TikTok, and related TSO services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sigedev01-bit](https://clawhub.ai/user/sigedev01-bit)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to route TSO advertising tasks to the correct CLI-backed workflow for account operations, Google and Meta campaign work, reporting, website diagnosis, keyword planning, and market analysis. It is intended for users who intentionally want Siluzan TSO to manage advertising accounts and reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill has broad activation rules for advertising accounts, reports, finance, permissions, and operational workflows.

Mitigation: Use it only for intended Siluzan TSO advertising operations, keep workflow routing scoped to the user's request, and require explicit confirmation before write, delete, reauthorization, finance, or permission-changing commands.

Risk: One-click installers can change global AI-client skill registrations, package-manager registry settings, and local CLI configuration.

Mitigation: Prefer a reviewed manual install; if using the installer, review the script first and confirm acceptance of global registration and registry changes.

Risk: Lead exports, account data, and generated HTML or spreadsheet reports can contain sensitive business or personal data.

Mitigation: Keep exports local where possible, avoid pasting raw lead JSON into chat, and handle generated reports as sensitive artifacts.

## Reference(s):

- [Siluzan TSO ClawHub skill page](https://clawhub.ai/sigedev01-bit/skills/siluzan-tso)
- [Skill definition and routing table](SKILL.md)
- [References index](references/README.md)
- [Setup and authentication](references/core/setup.md)
- [Intent routing](references/core/intent-routing.md)
- [Analysis and reporting playbooks](references/core/playbooks.md)
- [Operations workflows](references/core/workflows.md)
- [Account analytics and reporting](references/analytics/account-analytics.md)
- [Google Ads workflow reference](references/google-ads/google-ads.md)
- [Meta Ads workflow reference](references/meta-ads/meta-ads.md)
- [Website diagnosis guide](references/analytics/website-diagnosis-guide.md)
- [Market analysis guide](references/analytics/market-analysis-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands, JSON configuration templates, and generated report files such as HTML or Excel when supported by the CLI workflow.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or update local JSON, Markdown, HTML, and spreadsheet artifacts through scoped workflows; write operations require explicit user confirmation.]

## Skill Version(s):

1.1.52 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
