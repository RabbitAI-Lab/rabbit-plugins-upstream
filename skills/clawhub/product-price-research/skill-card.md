## Description:

Researches products, prices, sellers, and reviews across major online marketplaces and big-box retailers (Amazon, eBay, Shopify stores, Shop.app, Target, Costco, Zalando, Walmart) using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and commerce researchers use this skill to search product listings, compare prices and sellers, pull marketplace reviews, and summarize public product data from supported retailers through Crawlora API responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can forward arbitrary paths, methods, and request bodies to the configured Crawlora API host, making it broader than the stated product-price workflow.

Mitigation: Review calls before execution, use only product-research endpoints, and avoid passing sensitive data in request bodies.

Risk: Changing CRAWLORA_API_BASE can redirect requests and API credentials to an alternate host.

Mitigation: Leave CRAWLORA_API_BASE unset unless the alternate host is intentionally trusted.

Risk: The skill depends on a Crawlora API key and external API responses.

Mitigation: Store the key only in CRAWLORA_API_KEY, do not hardcode or commit it, and check returned marketplace data before using it for decisions.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/product-price-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns normalized product, price, seller, availability, and review data from supported public marketplace endpoints.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
