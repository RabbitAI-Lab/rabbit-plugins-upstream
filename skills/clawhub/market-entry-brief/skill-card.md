## Description:

根据主 ASIN 与已授权竞品的商品页和评论证据，整理市场进入前的页面差异、用户疑问和验证清单。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to compare a primary ASIN with authorized competitors before market entry, using product-page and review evidence to identify page gaps, buyer questions, and validation checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is flagged suspicious because it advertises a narrow market-entry brief while also enabling broader ARI operations such as paid reports, account setting changes, monitoring, alerts, and exports.

Mitigation: Review the skill before installing, use it only when those ARI account-connected capabilities are acceptable, and set autoconfirm to always ask when per-charge control is required.

Risk: Ambiguous requests could trigger workflows involving charges or account-changing actions.

Mitigation: Confirm before enabling schedules, watches, exports, or other account-changing workflows, and avoid ambiguous requests when paid actions may be available.

## Reference(s):

- [ARI CLI 与 API 参考](artifact/references/reference.md)
- [Amazon 市场进入对照简报 专属运营工作流](artifact/references/operation-workflow.md)
- [ClawHub skill listing](https://clawhub.ai/funewa/skills/market-entry-brief)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Conversational guidance and Markdown briefs, with optional shell commands and JSON responses for advanced use.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and sufficient authorized product, review, and competitor evidence; excludes market-size, sales, profit, advertising, inventory, order, and true return-rate predictions.]

## Skill Version(s):

1.4.7 (source: frontmatter, changelog, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
