## Description:

Researches independent Shopify-powered storefronts using the Crawlora API, returning normalized JSON for products, collections, pages, sitemaps, search suggestions, and product recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, analysts, and commerce teams use this skill to audit public Shopify storefront catalogs, crawl storefront sitemaps, inspect pages, and compare search or recommendation behavior without scraping storefront HTML directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send the Crawlora API key and arbitrary requests outside the Shopify-focused scope.

Mitigation: Use only public storefront research targets, keep CRAWLORA_API_KEY out of committed files, avoid overriding CRAWLORA_API_BASE unless the destination is fully trusted, and prefer a hardened helper restricted to approved Shopify/Crawlora endpoints.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/shopify-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; API results are paginated and subject to endpoint limits.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
