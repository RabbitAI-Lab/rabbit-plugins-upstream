## Description:

使用极鲸云查询和分析 Mercado Libre（美客多）商品搜索、详情、价格、销量、销售额、评分、评论数、上架时间、店铺指标、跨境和 FULL 履约标记。

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External business users and agents use this skill to screen Mercado Libre products by market, keyword, category, price, sales, rating, cross-border status, and FULL fulfillment, then compare candidate details and recent history for product research decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Login tokens may be stored in local JSON state files in user configuration, skill, and workspace locations.

Mitigation: Install only if GeekBI is trusted, keep access to those directories restricted, and clear local authentication state when access is no longer needed.

Risk: Custom API origins may route authentication or query traffic outside the default GeekBI service.

Mitigation: Use the default GeekBI API origin unless the publisher provides a trusted alternative and the deployment owner has reviewed it.

Risk: Server-provided login or action links may pause the workflow and redirect the user for account actions.

Mitigation: Show the server-provided message and link as-is, stop further data queries until the user completes the action, and do not expose tokens, device codes, request headers, or authentication objects.

Risk: Product metrics are GeekBI-collected snapshots and may not represent official seller-center data or the full Mercado Libre market.

Mitigation: Use the results for screening and comparison, then verify policy, listing, cost, logistics, and seller-center data before operational decisions.

## Reference(s):

- [Server-resolved source repository](https://github.com/geekbi/geekbi-mercadolibre-product-search-skill)
- [ClawHub skill listing](https://clawhub.ai/geekbi/skills/geekbi-mercadolibre-product-search-skill)
- [Mercado Libre 商品接口](references/MercadoLibre商品接口.md)
- [Mercado Libre 商品研究](references/MercadoLibre商品研究.md)
- [Mercado Libre 运营与政策口径](references/MercadoLibre运营与政策口径.md)
- [查询暂停与恢复流程](references/查询暂停与恢复流程.md)
- [Mercado Libre Seller Reputation](https://global-selling.mercadolibre.com/devsite/en_us/price-per-variation-cbt/seller-reputation-global-selling)
- [Mercado Libre User Products](https://global-selling.mercadolibre.com/devsite/en_us/deals-gs/user-products-cbt)
- [Mercado Libre Global Listing](https://global-selling.mercadolibre.com/devsite/en_us/sync-and-modify-listings-gs/global-listing)
- [Mercado Libre Fully Managed](https://global-selling.mercadolibre.com/devsite/en_us/manage-claims/fully-managed-product-publishing)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown business analysis; helper scripts emit JSON for agent processing.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default user-facing output includes conclusion, query scope, candidate evidence, risks, and next validation steps; business users should not receive raw tokens, headers, or internal authentication objects.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
