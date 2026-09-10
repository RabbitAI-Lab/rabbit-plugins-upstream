## Description:

使用极鲸云查询 Mercado Libre（美客多）当前商品样本中真实出现的类目列表和类目父链，并结合商品样本分析销量、价格带、口碑和品类机会。

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and category researchers use this skill to inspect observed Mercado Libre category paths and sampled listings, then compare prices, sales, reputation signals, and category opportunities. It supports category research and selection workflows, not full-market measurement or listing execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles login tokens and may write bearer-token auth state into GeekBI auth files in the skill, user config, and current working directories.

Mitigation: Use the skill only in trusted workspaces, keep auth state files out of shared artifacts, and clear the auth state when access is no longer needed.

Risk: Custom API origins can redirect queries or authentication flows away from the default trusted GeekBI HTTPS endpoint.

Mitigation: Use the default https://openapi.geekbi.com endpoint and do not pass custom --base-url values unless the endpoint has been reviewed.

Risk: Authentication links returned by the service can be opened by the user during paused query flows.

Mitigation: Verify login links before opening them, present only the service-returned jumpUrl unchanged, and never expose access tokens, device codes, request headers, or internal auth objects.

Risk: Sample-based category and product data can be mistaken for complete Mercado Libre market coverage.

Mitigation: State the site, filters, sample coverage, page, sample count, and update time; avoid claiming official category GMV, traffic, search volume, advertising, commissions, or full-market competition data.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/geekbi/geekbi-mercadolibre-category-search-skill)
- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-mercadolibre-category-search-skill)
- [Mercado Libre 商品接口](references/MercadoLibre商品接口.md)
- [Mercado Libre 类目接口](references/MercadoLibre类目接口.md)
- [Mercado Libre 类目研究](references/MercadoLibre类目研究.md)
- [Mercado Libre 运营与政策口径](references/MercadoLibre运营与政策口径.md)
- [查询暂停与恢复流程](references/查询暂停与恢复流程.md)
- [Mercado Libre Seller Reputation](https://global-selling.mercadolibre.com/devsite/en_us/price-per-variation-cbt/seller-reputation-global-selling)
- [Mercado Libre User Products](https://global-selling.mercadolibre.com/devsite/en_us/deals-gs/user-products-cbt)
- [Mercado Libre Global Listing](https://global-selling.mercadolibre.com/devsite/en_us/sync-and-modify-listings-gs/global-listing)
- [Mercado Libre Fully Managed](https://global-selling.mercadolibre.com/devsite/en_us/manage-claims/fully-managed-product-publishing)
- [GeekBI API endpoint](https://openapi.geekbi.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown analysis with JSON helper-script outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include service-returned authentication links and sample-scope caveats; product searches are limited to the first 200 sampled items.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
