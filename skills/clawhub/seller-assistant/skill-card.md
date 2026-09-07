## Description:

亚马逊运营助手 Skill 用评论数据支撑 Amazon 卖家运营决策，包括采集自家与竞品评论、查看评分结构与趋势、生成 VOC 或深度洞察报告，并回答差评增长、卖点排序、产品改进和文案优化等问题。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce operators use this skill to turn collected product reviews into VOC reports, trend summaries, competitor comparisons, keyword guidance, alerts, and practical listing or product-improvement recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: VOC and analysis workflows can consume ARI account credits automatically under server-controlled auto-confirm rules.

Mitigation: Review billing and auto-confirm settings before use; ask the skill to set autoconfirm off or say '只报价，不执行' when only a price preview is desired.

Risk: Interrupted paid operations may already have consumed credits or produced an archived report.

Mitigation: Check the latest report or operation status before retrying a paid command, and only rerun after confirming no result was generated.

Risk: Analysis is limited to ARI-collected Amazon review samples and may not cover every review, variant, or time window.

Mitigation: Present sample size, collection window, and scope limits with conclusions, and verify high-impact business decisions with additional evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/seller-assistant)
- [Publisher profile](https://clawhub.ai/user/funewa)
- [使用说明](使用说明.md)
- [API reference](references/reference.md)
- [ARI account and authorization](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Configuration instructions, Files]

**Output Format:** [Human-facing Markdown reports and summaries, with CLI setup commands and optional exported Markdown, HTML, or CSV files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and uses ARI-collected Amazon review data; some workflows may consume account credits under the account's auto-confirm policy.]

## Skill Version(s):

1.4.7 (source: frontmatter, _meta.json, CHANGELOG, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
