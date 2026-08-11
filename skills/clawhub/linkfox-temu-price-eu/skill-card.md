## Description:

Temu EU product pricing API skill that routes Partner EU price operations through the LinkFox gateway, including pricing order queries, batch SKU base price changes, recommended supply price queries, and base price estimates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to inspect and update Temu Europe pricing through LinkFox-backed scripts and API guidance. It supports querying pricing orders, estimating or retrieving recommended supply prices, and submitting batch SKU base price changes.

### Deployment Geography for Use:

Europe

## Known Risks and Mitigations:

Risk: The skill can manage live Temu EU prices, including batch SKU base price changes.

Mitigation: Use it only for intended live pricing work and require confirmation before every batch price change.

Risk: The skill can store Temu access tokens locally.

Mitigation: Use least-privilege Temu tokens and protect or avoid the ~/.linkfox token file.

Risk: The skill includes broader proxy and file-download helpers beyond the narrow price scripts.

Mitigation: Use only the needed helpers and only trusted LinkFox gateway endpoints.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-price-eu)
- [linkfox-temu-price-eu API reference](references/api.md)
- [Temu accessToken authorization](references/access-token.md)
- [Temu authorization flow](references/authorization-flow.md)
- [Partner EU price interface catalog](references/partner-eu-catalog.md)
- [Price API document index](references/apis/README.md)
- [Pricing order query](references/apis/bg-local-goods-priceorder-query.md)
- [Batch SKU base price change](references/apis/bg-local-goods-priceorder-change-sku-price.md)
- [Base price recommendation](references/apis/temu-local-goods-baseprice-recommend.md)
- [Recommended price query](references/apis/temu-local-goods-recommendedprice-query.md)
- [Temu Partner EU documentation](https://partner-eu.temu.com/documentation?menu_code=dfff38c23adf498d8a7cd55052bd3648)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls, JSON, Files]

**Output Format:** [Markdown guidance with shell commands and JSON API responses or saved response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts save full responses under a linkfox session data directory and print either full JSON or a concise summary depending on response size.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
