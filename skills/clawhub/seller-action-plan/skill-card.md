## Description:

Amazon 卖家行动计划综合 Amazon 商品详情与评论，为单个 ASIN 生成数据支持的运营行动优先级和检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to turn a single ASIN's product details and review evidence into an operations audit, Listing checks, and prioritized next actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an ARI API key and can access seller product and review data.

Mitigation: Use the documented ARI authorization flow, do not expose the API key in reports or examples, and review data access expectations before installation.

Risk: Some analyses can spend account credits under quote, confirmation, or server-side auto-confirmation rules.

Mitigation: Use quote-only flows when only pricing is requested, set auto-confirmation to ask every time when per-charge control is needed, and do not retry interrupted paid operations until checking status or existing reports.

Risk: The release includes broader monitoring, export, and account-state capabilities than a narrow action-plan helper may imply.

Mitigation: Review the documented capabilities before deployment, avoid unsupported workflow or focus overrides, and treat local exports as sensitive business files.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/seller-action-plan)
- [Amazon 卖家行动计划 专属运营工作流](references/operation-workflow.md)
- [ARI CLI 与 API 参考](references/reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with optional inline shell commands and API-derived summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid operations require quote and explicit confirmation unless the account's server-side auto-confirmation rules apply.]

## Skill Version(s):

1.4.7 (source: frontmatter, changelog, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
