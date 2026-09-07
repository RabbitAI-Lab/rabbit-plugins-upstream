## Description:

基于 Amazon 商品字段和评论反馈，识别商品描述的信息缺口并给出改写建议；仅用于商品描述诊断和建议，不用于五点描述、广告投放或自动发布。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to evaluate product-detail fields against review feedback and receive evidence-based description optimization guidance. It checks required data, quotes ARI operations costs, and runs the fixed listing/description workflow only after the required confirmation path.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires ARI API access to Amazon review and product data.

Mitigation: Install only if comfortable granting ARI API access, keep credentials out of reports and command examples, and revoke or rotate keys from the ARI account page when needed.

Risk: ARI account credits can be spent when paid operations are confirmed or when account auto-confirm rules apply.

Mitigation: Use quote-only requests for exploration, set auto-confirm off when per-action approval is required, and verify generated reports before retrying interrupted paid operations.

Risk: Outputs are recommendations based on available product fields and review samples and may be incomplete when data is sparse.

Mitigation: Review the cited data range, sample size, and returned evidence before applying listing changes, and do not treat the skill as an automatic Amazon page publisher.

## Reference(s):

- [Amazon 商品描述优化 专属运营工作流](references/operation-workflow.md)
- [ARI CLI 与 API 参考](references/reference.md)
- [ARI Amazon 评论智能助手使用指南](使用说明.md)
- [ClawHub skill page](https://clawhub.ai/funewa/skills/description-writer)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Natural-language guidance and Markdown-style reports, with occasional ARI CLI commands for setup, quoting, status checks, and confirmed execution.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ASIN, site, sample size, report ID, report URL, credits used, balance, and data-source notes when returned by ARI.]

## Skill Version(s):

1.4.7 (source: SKILL.md frontmatter, CHANGELOG, evidence release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
