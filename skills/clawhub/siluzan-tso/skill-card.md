## Description:

Siluzan TSO guides agents through advertising account operations, campaign planning, keyword research, market and website analysis, and multi-platform reporting for Google, Meta, Bing, Yandex, and TikTok workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sigedev01-bit](https://clawhub.ai/user/sigedev01-bit)

### License/Terms of Use:

MIT-0

## Use Case:

Advertising operators, agency teams, and agents serving Siluzan TSO users use this skill to route account, campaign, reporting, lead, finance, and optimization requests to the appropriate documented workflow. It supports high-impact read and write operations, so users should review account IDs, credentials, budgets, and write confirmations before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide high-impact advertising account, campaign, finance, and lead workflows.

Mitigation: Verify credentials, account IDs, budgets, permissions, and any write confirmations before executing account-changing steps.

Risk: The skill may handle sensitive lead data and local credential storage.

Mitigation: Use trusted environments, limit credential scope, and review raw lead-data outputs before sharing or storing them.

Risk: The security guidance flags one-click installers as risky because they may make global npm changes and cross-assistant registrations.

Mitigation: Prefer scoped or manual installation and inspect installer behavior before running it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sigedev01-bit/skills/siluzan-tso)
- [Publisher profile](https://clawhub.ai/user/sigedev01-bit)
- [Core intent routing](references/core/intent-routing.md)
- [Core playbooks](references/core/playbooks.md)
- [Core workflows](references/core/workflows.md)
- [Agent conventions](references/core/agent-conventions.md)
- [Account balance and stats](references/accounts/accounts-balance-stats.md)
- [Google Ads workflow](references/google-ads/google-ads.md)
- [Google Ads write workflow](references/google-ads/google-ads-write.md)
- [Meta Ads workflow](references/meta-ads/meta-ads.md)
- [Keyword planner workflows](references/analytics/keyword-planner-workflows.md)
- [Account analytics](references/analytics/account-analytics.md)
- [Website diagnosis guide](references/analytics/website-diagnosis-guide.md)
- [Market analysis guide](references/analytics/market-analysis-guide.md)
- [Report workflow](report-templates/REPORT-WORKFLOW.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands, JSON templates, and generated report artifacts such as HTML or XLSX when workflows require them]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and siluzan-tso-cli with authenticated access to the relevant advertising and account systems.]

## Skill Version(s):

1.1.53 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
