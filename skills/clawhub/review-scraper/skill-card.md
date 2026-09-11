## Description:

采集、筛选、分析并导出美国、英国、德国、日本、加拿大、法国、西班牙和意大利 Amazon 站点的 ASIN 评论，并在付费采集或分析前按 ARI 账户规则报价和确认。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon operators and agents use this skill to collect review samples, inspect review trends and topics, produce VOC or keyword reports, manage monitoring workflows, and export collected reviews or reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits through collection, analysis, leaderboard, or advice workflows.

Mitigation: Use quote-only requests for price checks, set autoconfirm off when confirmation is required, and confirm paid actions before execution.

Risk: The skill can change ongoing account settings such as schedules, watches, competitor tracking, and export workflows.

Mitigation: Confirm the ASIN, site, setting, recurrence, and cost impact before enabling or changing persistent workflows.

Risk: The skill uses a local ARI API key and sends Amazon review data to ARI services.

Mitigation: Install only when ARI is trusted for the relevant review data, keep API keys out of chat and reports, and revoke or recreate exposed keys.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/review-scraper)
- [ARI CLI and API Reference](references/reference.md)
- [ARI Amazon Review Assistant User Guide](使用说明.md)
- [ARI Account and API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing and Credits](https://ari.funewa.com/zh/billing)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown responses with command examples, JSON status summaries, and CSV, Markdown, or HTML export files when supported by the account plan.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Some collection, analysis, monitoring, competitor, leaderboard, and advice workflows can consume ARI credits or change ongoing account settings.]

## Skill Version(s):

1.4.8 (source: frontmatter, _meta.json, CHANGELOG, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
