## Description:

使用极鲸云查询和分析 AliExpress 商品、销量与销售额、价格、评分、评论数、点赞、库存、上架时间、SKU 和历史趋势。

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce analysts use this skill to search AliExpress products with GeekBI data, compare candidates by sales, revenue, price, ratings, reviews, likes, stock, listing time, SKU, and recent history, and prepare product-research findings with explicit data limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authentication state is stored locally and may be mirrored across user, skill, and workspace locations.

Mitigation: Install only when the publisher is trusted, avoid shared or synced workspaces for authenticated use, and clear GeekBI auth state after use on shared machines.

Risk: Custom base URLs can redirect API and authentication traffic away from the default GeekBI endpoint.

Mitigation: Use the default GeekBI endpoint and avoid custom --base-url values unless the destination has been independently approved.

Risk: Login continuation links are provided by the service and could expose users to authorization-flow confusion.

Mitigation: Check login links before authorizing, do not rewrite service-provided jumpUrl values, and never expose access tokens, device codes, request headers, or internal authentication objects.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-aliexpress-product-search-skill)
- [Server-resolved GitHub provenance](https://github.com/geekbi/geekbi-aliexpress-product-search-skill)
- [AliExpress 商品接口](references/AliExpress商品接口.md)
- [AliExpress 商品研究](references/AliExpress商品研究.md)
- [AliExpress 运营与政策口径](references/AliExpress运营与政策口径.md)
- [查询暂停与恢复流程](references/查询暂停与恢复流程.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with concise findings, query criteria, candidate evidence, risks, and next-step validation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should hide raw JSON and internal authentication objects from business users.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
