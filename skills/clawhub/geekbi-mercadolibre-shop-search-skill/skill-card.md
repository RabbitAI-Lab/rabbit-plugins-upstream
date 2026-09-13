## Description:

查询和分析 Mercado Libre（美客多）店铺、卖家规模、信誉、销量、粉丝数、商品数和推算开店时间，并基于极鲸云返回数据给出可验证结论。

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators, analysts, and agents use this skill to search Mercado Libre shops by site, shop name or ID, product count, followers, sales, reputation, and opening-time filters, then summarize evidence, risks, and next validation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The authentication helper can be directed to user-supplied API origins through the base URL option.

Mitigation: Use the default GeekBI endpoint and do not pass untrusted --base-url values.

Risk: Login tokens may be stored in multiple local state files.

Mitigation: Install only after review and prefer a release that stores credentials in one protected per-user location or an operating system credential manager.

Risk: Shop metrics are based on GeekBI snapshots and may not match a seller's complete Mercado Libre back-office data.

Mitigation: Treat results as directional research and verify reputation, fulfillment, policy, and business decisions against official Mercado Libre sources and the target marketplace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-mercadolibre-shop-search-skill)
- [GitHub provenance](https://github.com/geekbi/geekbi-mercadolibre-shop-search-skill)
- [MercadoLibre店铺接口](references/MercadoLibre店铺接口.md)
- [MercadoLibre店铺研究](references/MercadoLibre店铺研究.md)
- [MercadoLibre运营与政策口径](references/MercadoLibre运营与政策口径.md)
- [查询暂停与恢复流程](references/查询暂停与恢复流程.md)
- [Mercado Libre Seller Reputation](https://global-selling.mercadolibre.com/devsite/en_us/price-per-variation-cbt/seller-reputation-global-selling)
- [Mercado Libre User Products](https://global-selling.mercadolibre.com/devsite/en_us/deals-gs/user-products-cbt)
- [Mercado Libre Global Listing](https://global-selling.mercadolibre.com/devsite/en_us/sync-and-modify-listings-gs/global-listing)
- [Mercado Libre Fully Managed](https://global-selling.mercadolibre.com/devsite/en_us/manage-claims/fully-managed-product-publishing)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown narrative with shell command usage and JSON-derived evidence summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default responses include conclusion, query scope, shop evidence, risks, and next validation steps.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
