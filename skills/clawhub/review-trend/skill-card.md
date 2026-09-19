## Description:

亚马逊评论趋势监控 Skill 按时间轴追踪 Amazon 评论量、评分与情绪变化，识别口碑拐点、抱怨主题以及竞品或批次质量信号，并可生成评论分析、趋势、VOC、对标、预警和导出结果。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, brand operators, and marketplace teams use this skill to monitor review trends, detect rating or sentiment changes, inspect complaint themes, compare competitors, and generate operational review reports from ARI-collected data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI account credits or perform paid review analysis under service auto-confirm rules.

Mitigation: Use quote-only language or require approval before paid actions, and review credit cost and balance before allowing collection, VOC, analyze, leaderboard, operations, or advise actions.

Risk: Schedule, watch, competitor, and autoconfirm changes can affect future account behavior or recurring costs.

Mitigation: Confirm these account changes explicitly, review the returned cost or policy details, and avoid enabling ongoing monitoring unless the user asked for it.

Risk: The skill requires ARI account authorization and local API-key access.

Mitigation: Authorize only through the official https://ari.funewa.com flow, do not share passwords or expose API keys in reports, and recreate the key if authentication fails.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/review-trend)
- [ARI CLI and API Reference](references/reference.md)
- [ARI Account and API Key Management](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text summaries with optional compact JSON, CSV, Markdown, and HTML export outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and ARI-collected Amazon review data; paid analysis or collection may consume account credits under server confirmation rules.]

## Skill Version(s):

1.4.13 (source: frontmatter, changelog, server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
