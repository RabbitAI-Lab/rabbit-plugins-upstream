## Description:

Researches Zalando products, prices, brands, categories, search suggestions, and storefront markets through the Crawlora API and returns normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research public Zalando catalog data, compare prices, inspect product details by SKU, browse market-specific categories, autocomplete search terms, and resolve supported storefront markets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and market-specific Zalando requests are sent to Crawlora with the user's Crawlora API key.

Mitigation: Avoid private or sensitive personal information in queries, and provide the API key only through the CRAWLORA_API_KEY environment variable.

Risk: Catalog and price data may be incomplete or market-specific because search and category endpoints return only the first page and require explicit storefront codes.

Mitigation: Resolve the intended market first, keep the same market through search and product-detail calls, and treat first-page results as scoped research rather than exhaustive inventory.

## Reference(s):

- [Zalando endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/zalando-research)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora API key signup](https://crawlora.net)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Normalized JSON from Crawlora API responses, with Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; limited to documented GET endpoints for Zalando markets, search, suggestions, products, categories, and category navigation.]

## Skill Version(s):

1.0.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
