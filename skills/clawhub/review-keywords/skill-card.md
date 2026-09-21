## Description:

亚马逊评论关键词提取 Skill 统计 Amazon 评论中的高频词与共现词，并区分正向和负向买家用语，用于 Listing 埋词、广告词筛选和评论洞察。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and operators use this skill to analyze ARI-collected reviews for customer keywords, positive and negative wording, pain points, purchase motivations, trends, competitor comparisons, monitoring signals, and exportable reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI account credits through review collection and paid analysis flows.

Mitigation: Use quote-only requests or set autoconfirm off so credit-spending actions require explicit approval.

Risk: The skill can change ongoing monitoring, competitors, alert or workbench state, exports, and confirmation settings under the connected ARI account.

Mitigation: Review requested account-management actions before confirming them, and keep monitoring or export changes scoped to the intended ASIN and site.

Risk: Reports are based on ARI-collected Amazon review samples and may not cover all reviews, time periods, or variants.

Mitigation: State the sample size, date range, site, and variant limitations when interpreting trends or making Listing recommendations.

Risk: Interrupted paid commands may already have generated a report and consumed credits.

Mitigation: Check existing reports or operation status before retrying a paid command.

## Reference(s):

- [Skill README](artifact/README.md)
- [使用说明](artifact/使用说明.md)
- [ARI CLI 与 API 参考](artifact/references/reference.md)
- [Changelog](artifact/CHANGELOG.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/review-keywords)
- [ARI Account and API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Natural-language responses, Markdown or HTML reports, CSV exports, and JSON CLI responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; review collection and paid AI analysis can consume ARI account credits.]

## Skill Version(s):

1.4.13 (source: SKILL.md frontmatter, _meta.json, CHANGELOG, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
