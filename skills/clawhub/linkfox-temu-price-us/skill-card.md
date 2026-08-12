## Description:

Temu 美国站商品价格管理 API，经 LinkFox 网关转发 Partner US 价格接口，支持定价单查询、批量修改 SKU 基础价、推荐供货价和基础价估算等操作。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Temu sellers, operators, and developers use this skill to manage United States marketplace pricing workflows, including price order lookup, recommended supply or base-price review, and batch SKU base-price changes.

### Deployment Geography for Use:

Global, for workflows targeting the Temu United States site.

## Known Risks and Mitigations:

Risk: The skill can handle Temu seller access tokens and LinkFox API keys.

Mitigation: Prefer direct accessToken use where appropriate, keep LinkFox keys out of shared shells and logs, and avoid unmasked token output.

Risk: Batch price-change operations can affect live seller pricing and account workflows.

Mitigation: Review the target site, store, goodsId, skuId, currency, and price values before running change-price scripts.

Risk: Gateway URL environment overrides can redirect API traffic.

Mitigation: Restrict LINKFOX_TOOL_GATEWAY, TEMU_API_BASE_URL, and STORE_API_BASE_URL to trusted LinkFox endpoints.

Risk: Downloaded files and saved JSON responses may persist sensitive seller or pricing data locally.

Mitigation: Store outputs only in controlled workspaces, restrict file permissions, and remove stale response files when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-price-us)
- [API reference](artifact/references/api.md)
- [Access token authorization](artifact/references/access-token.md)
- [Partner US catalog](artifact/references/partner-us-catalog.md)
- [Price API index](artifact/references/apis/README.md)
- [Price order query API](artifact/references/apis/bg-local-goods-priceorder-query.md)
- [Change SKU price API](artifact/references/apis/bg-local-goods-priceorder-change-sku-price.md)
- [Base price recommendation API](artifact/references/apis/temu-local-goods-baseprice-recommend.md)
- [Recommended price query API](artifact/references/apis/temu-local-goods-recommendedprice-query.md)
- [Temu Partner US documentation](https://partner-us.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Files]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses saved to local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are written under a linkfox date and session data directory; stdout prints full JSON for small responses or summaries for large responses.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
