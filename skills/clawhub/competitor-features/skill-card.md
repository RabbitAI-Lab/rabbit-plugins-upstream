## Description:

按主 ASIN 与已授权竞品的商品字段和评论证据整理可比特性矩阵，标注资料缺口与体验差异；仅用于静态特性对照，不用于销量、库存、广告、订单或真实退货率推断。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and ecommerce operators use this skill to compare a primary ASIN with authorized competitors using product fields and review evidence. It helps produce feature matrices, evidence gaps, and listing or product-improvement guidance after ARI service checks, quotes, and user-confirmed paid operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access broader ARI seller-account functions than a static competitor matrix, including monitoring, exports, and paid analyses.

Mitigation: Install it only when that broader ARI authority is intended, and review generated monitoring or scheduled collection settings after use.

Risk: ARI API keys and account requests could be exposed if credentials are shared or traffic is redirected to an untrusted base URL.

Mitigation: Use a limited, revocable ARI key; never include the key in reports or examples; and do not set ARI_BASE_URL or ARI_ALLOW_CUSTOM_BASE unless the destination is controlled and trusted.

Risk: Paid or state-changing commands may consume credits or alter account monitoring state.

Mitigation: Require an explicit quote and user confirmation before paid operations, reuse the quoted request ID, and check operation status after interruptions instead of directly retrying.

Risk: Feature comparisons can be misleading if product fields, review counts, or competitor evidence are incomplete.

Mitigation: Report evidence gaps, compare only metrics returned by ARI for both products, and avoid unsupported claims about sales, inventory, ads, orders, compliance certifications, or true return rates.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/competitor-features)
- [ARI CLI and API reference](artifact/references/reference.md)
- [Amazon competitor feature matrix workflow](artifact/references/operation-workflow.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and API-derived evidence summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report URLs, request IDs, credits used, ASIN/site identifiers, sample sizes, statistics windows, and evidence gaps when returned by ARI.]

## Skill Version(s):

1.4.3 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
