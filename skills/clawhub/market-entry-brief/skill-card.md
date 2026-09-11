## Description:

根据主 ASIN 与已授权竞品的商品页和评论证据，生成市场进入前的页面差异、用户疑问和验证清单，并明确不用于销量、利润、广告、库存、订单或退货率预测。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon operators and product researchers use this skill to compare a main ASIN with authorized competitors before market entry, focusing on page differences, user questions, review-backed risks, and validation checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security verdict is suspicious because the skill can exercise broader ARI account powers than the advertised market-entry brief, including spending credits, changing monitoring settings, and exporting data.

Mitigation: Review the skill carefully before installing, use quote-only flows when per-action approval is needed, and prefer disabling auto-confirm for paid actions unless the account owner accepts the billing behavior.

Risk: Using the required ARI API key can affect the user's ARI account, credits, monitoring state, and local exports.

Mitigation: Keep the API key out of reports and chat transcripts, authorize only through the documented ARI flow, and confirm paid or account-changing actions before execution when auto-confirm is not desired.

## Reference(s):

- [ARI CLI 与 API 参考](artifact/references/reference.md)
- [Amazon 市场进入对照简报 专属运营工作流](artifact/references/operation-workflow.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/market-entry-brief)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown brief with concise evidence summaries and optional ARI CLI command output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ARI report URLs, ASIN/site identifiers, sample counts, credit usage, and data-window notes when returned by ARI.]

## Skill Version(s):

1.4.8 (source: frontmatter, changelog, _meta.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
