## Description:

Queries GeekBI Shopee product, shop, category, and history data to support cross-border ecommerce product research, market sizing, trend analysis, competitor review, and category opportunity assessment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, analysts, and agent users use this skill to query GeekBI Shopee data and produce concise market research on products, shops, categories, sales trends, price bands, competition, and validation risks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local login token state may be written to multiple locations.

Mitigation: Install and run the skill only from a private local workspace; clear auth state before moving, sharing, or synchronizing the workspace.

Risk: Requests and action links can be influenced by configurable destinations or server responses.

Mitigation: Use the default GeekBI endpoint, avoid custom base URLs, and independently verify that login or recovery links belong to GeekBI before opening them.

Risk: Shopee data does not include cost, ad spend, commissions, fulfillment fees, returns, taxes, traffic, conversion, orders, or comment text.

Mitigation: Present findings as data-backed research, not profit, compliance, or Seller Centre account advice; require manual validation before listing, promotion, or operational decisions.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/geekbi/geekbi-shopee-research-skill)
- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-shopee-research-skill)
- [Shopee interface overview](references/接口总览.md)
- [Shopee product research](references/Shopee商品研究.md)
- [Shopee product interfaces](references/Shopee商品接口.md)
- [Shopee shop research](references/Shopee店铺研究.md)
- [Shopee shop interface](references/Shopee店铺接口.md)
- [Shopee category research](references/Shopee类目研究.md)
- [Shopee category interfaces](references/Shopee类目接口.md)
- [Shopee operations and policy scope](references/Shopee运营与政策口径.md)
- [Query pause and recovery flow](references/查询暂停与恢复流程.md)
- [GeekBI OpenAPI endpoint](https://openapi.geekbi.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Chinese Markdown with data scope, key evidence, opportunity and risk notes, and next validation steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve site, currency, filters, page range, sample size, update time, and missing-field caveats.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
