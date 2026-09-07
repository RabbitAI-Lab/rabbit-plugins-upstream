## Description:

按主 ASIN 与已授权竞品的商品字段和评论证据整理可比特性矩阵，标注资料缺口与体验差异；需要 ARI API key，不用于销量、库存、广告、订单或真实退货率推断。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon marketplace operators use this skill to compare their product with authorized competitor ASINs using product fields and review evidence. It produces a static feature matrix with evidence gaps, experience differences, and clear boundaries around unsupported business metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill advertises a narrow competitor feature-matrix workflow while exposing broader ARI account behavior.

Mitigation: Review it as a broad ARI account tool before installation, not only as a static matrix helper.

Risk: The skill requires ARI API-key access and can use account-linked API calls.

Mitigation: Install only if comfortable granting ARI API-key access; do not share the key in chat or reports, and avoid custom ARI_BASE_URL unless you control the endpoint.

Risk: Paid reports or analyses may run under account auto-confirm rules.

Mitigation: Keep auto-confirm off or limited when explicit approval is required, and use quote-only flows before paid actions.

Risk: Monitoring or schedule changes can create recurring collection behavior and future costs.

Mitigation: Confirm the marketplace, ASINs, schedule, and cost before enabling recurring collection or watch behavior.

Risk: Report and review exports may write files locally.

Mitigation: Choose export paths carefully and review generated files before sharing or importing them elsewhere.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/competitor-features)
- [README](README.md)
- [Usage Guide](使用说明.md)
- [Dedicated Operations Workflow](references/operation-workflow.md)
- [ARI CLI and API Reference](references/reference.md)
- [ARI API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Products](https://ari.funewa.com/zh/products)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and concise text guidance, with optional shell commands, JSON API responses, report URLs, and local export files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should distinguish direct data, inference, and recommendations; include data range, sample limitations, report IDs, credit usage, and saved export paths when applicable.]

## Skill Version(s):

1.4.7 (source: evidence release, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
