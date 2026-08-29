## Description:

Researches secondhand, resale, and handmade marketplaces through the Crawlora API for Poshmark, Etsy, Vinted, StockX, Mercari, Depop, and Whatnot, returning normalized JSON for listing, seller, shop, price, and marketplace research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and marketplace researchers use this skill to find and compare public resale listings, inspect seller or shop storefronts, check sneaker and streetwear resale prices, and research handmade or vintage goods across supported marketplaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send requests, request bodies, and the API key to arbitrary Crawlora-compatible paths or to a redirected base URL.

Mitigation: Use only documented Poshmark, Etsy, Vinted, StockX, Mercari, Depop, and Whatnot endpoints, and avoid setting CRAWLORA_API_BASE unless you control the destination.

Risk: API usage can spend Crawlora credits when requests succeed.

Mitigation: Use a Crawlora key with acceptable spending limits and review planned calls before running broad searches or pagination.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; API calls return public marketplace data from documented Crawlora endpoints.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
