## Description:

Helps agents analyze advertising accounts across Google, Bing, Yandex, TikTok, and Meta, manage supported account and campaign workflows, and create campaign plans, market analyses, and performance reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sigedev01-bit](https://clawhub.ai/user/sigedev01-bit)

### License/Terms of Use:

MIT-0

## Use Case:

Advertising teams and agents use this skill to review account performance, manage supported advertising workflows, and prepare campaign plans, market analyses, and client reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled one-click installers can make broad, persistent system, registry, and cross-assistant changes.

Mitigation: Prefer installation into one chosen skill directory; use the bundled one-click installers only when those broader changes are acceptable.

Risk: Account and campaign workflows can affect live advertising settings and spend.

Mitigation: Review account IDs, budgets, targeting, enabled status, and cleanup permissions before writes.

Risk: Login codes and identity, banking, or customer records require careful handling.

Mitigation: Enter login codes locally where possible and use protected handling for sensitive records.

Risk: The external CLI and downloaded installers were not audited by the supplied security review.

Mitigation: Apply appropriate review to the external CLI and any downloaded installers before relying on them.

## Reference(s):

- [Siluzan TSO on ClawHub](https://clawhub.ai/sigedev01-bit/skills/siluzan-tso)
- [Account analytics guide](references/analytics/account-analytics.md)
- [Google Ads workflows](references/google-ads/google-ads.md)
- [Meta Ads workflows](references/meta-ads/meta-ads.md)
- [Market analysis guide](references/analytics/market-analysis-guide.md)
- [Setup guide](references/core/setup.md)
- [Report templates index](report-templates/README.md)

## Skill Output:

**Output Type(s):** [Analysis, API calls, Code, Configuration, Shell commands, Guidance, Markdown, HTML reports, Excel workbooks]

**Output Format:** [CLI interactions, structured JSON, Markdown, HTML, and Excel reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18+, siluzan-tso-cli, and authentication; outputs depend on the selected workflow and report template.]

## Skill Version(s):

1.1.63 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
