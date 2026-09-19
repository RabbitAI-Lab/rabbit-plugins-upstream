## Description:

Researches products, prices, brands, and categories on Zalando using the Crawlora API, returning clean JSON for product search, category browsing, brand lookup, autocomplete, product details, and storefront market resolution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to look up and compare public Zalando product, price, brand, category, SKU, autocomplete, and storefront-market data through Crawlora instead of scraping Zalando pages directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-directed product and search queries are sent to Crawlora as a third-party API provider.

Mitigation: Install only if comfortable using Crawlora for Zalando research, and avoid sending private or sensitive search terms unless Crawlora receiving them is acceptable.

Risk: The Crawlora API key could be exposed if it is hardcoded, committed, or passed in command-line arguments.

Mitigation: Keep CRAWLORA_API_KEY in the environment and use the provided helper, which avoids putting the key in query parameters or normal command-line arguments.

## Reference(s):

- [Zalando endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY from the environment; documented Zalando routes are GET-only and return normalized public marketplace data.]

## Skill Version(s):

1.0.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
