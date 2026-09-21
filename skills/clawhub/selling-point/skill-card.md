## Description:

从 Amazon 好评中提炼买家购买动因和高说服力卖点，并通过 ARI 评论数据支持 VOC 报告、趋势、竞品对比、监控和导出工作流。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers, e-commerce operators, and their agents use this skill to turn ARI-collected reviews for an ASIN into selling points, pain points, trend notes, competitor comparisons, and listing or operations recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid ARI review-analysis actions may execute after confirmation or under account autoconfirm rules.

Mitigation: Keep autoconfirm off when every paid action should require approval, and use quote-only requests when the user wants pricing without execution.

Risk: Schedule, competitor, watch, and workbench commands can mutate ARI account state and may affect future credit use.

Mitigation: Run those account-changing commands only after an explicit user request and review the returned cost, cadence, or status change.

Risk: The skill requires connecting an ARI account and storing an ARI API key locally or in ARI_API_KEY.

Mitigation: Use the browser authorization flow where possible, avoid pasting keys into chat, and rotate or rebuild keys if authentication fails.

## Reference(s):

- [ARI CLI and API Reference](artifact/references/reference.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/selling-point)
- [Publisher Profile](https://clawhub.ai/user/funewa)
- [ARI Account and API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Conversational text and Markdown reports, with optional JSON CLI output and CSV, Markdown, or HTML exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; outputs should state data scope and keep direct data, inference, and recommendations distinct.]

## Skill Version(s):

1.4.13 (source: frontmatter, _meta.json, changelog, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
