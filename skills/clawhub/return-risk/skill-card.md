## Description:

从 Amazon 评论和商品详情中识别可能导致退货的体验与期望落差线索，并给出改进方向；仅用于评论证据线索，不宣称真实退货率，也不用于库存、退款或客服执行。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and ecommerce operators use this skill to analyze collected Amazon reviews and product details for return-risk clues, pain points, trend signals, and product or listing improvement directions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an ARI API key and can access ARI account data or save credentials locally.

Mitigation: Install only when the ARI service is trusted, keep the API key out of chat and reports, and review the skill before deployment.

Risk: The skill can trigger paid ARI actions and may use account auto-confirm behavior for some spending.

Mitigation: Use quote-only flows when pricing is needed, disable auto-confirm if every paid action should require approval, and confirm costs before paid runs.

Risk: The skill can change persistent account behavior such as spending confirmation, monitoring, or competitor collection.

Mitigation: Verify the ASIN, site, schedule, and stated cost before making account changes, and periodically review ARI account settings.

Risk: The skill can export local files containing review or report data.

Mitigation: Review exported contents and storage location before sharing files outside the account or organization.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/return-risk)
- [README](README.md)
- [ARI Amazon 评论智能助手使用指南](使用说明.md)
- [Amazon 退货风险线索 专属运营工作流](references/operation-workflow.md)
- [ARI CLI 与 API 参考](references/reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports and concise chat summaries, with shell commands or JSON snippets only for setup and troubleshooting.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links, review evidence, credit usage, and cost confirmations when paid ARI actions are required.]

## Skill Version(s):

1.4.8 (source: server release, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
