## Description:

Researches products, prices, brands, and categories on Zalando using the Crawlora API and returns normalized JSON without scraping Zalando pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and shopping research agents use this skill to query Zalando storefront markets, product search, autocomplete, category listings, and product details through Crawlora. It is suited for storefront-aware price checks, catalog research, and search-to-detail product comparison using public listing data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper can call arbitrary Crawlora endpoints and send arbitrary request bodies outside the Zalando-only scope.

Mitigation: Restrict or edit scripts/crawlora.sh before use so it only allows /zalando/markets, /zalando/search, /zalando/suggest, /zalando/product, and /zalando/category.

Risk: The skill requires a Crawlora API key, and misuse could expose credentials or send unintended authenticated requests.

Mitigation: Keep the key only in CRAWLORA_API_KEY, do not hardcode or commit it, and review proposed shell commands before execution.

Risk: Zalando storefront, SKU, and category behavior is market-specific, so using mismatched market codes or translated slugs can produce incomplete or misleading results.

Mitigation: Resolve storefronts with /zalando/markets and keep the same market code between search, category, and product-detail calls.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key in CRAWLORA_API_KEY; Zalando search and category results are limited to the first page.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
