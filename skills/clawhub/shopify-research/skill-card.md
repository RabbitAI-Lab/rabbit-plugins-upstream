## Description:

Researches independent Shopify-powered storefronts using the Crawlora API to return normalized JSON for products, collections, pages, sitemaps, search suggestions, and product recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and commerce researchers use this skill to query public Shopify storefront metadata and catalog content through Crawlora for catalog audits, sitemap crawls, search suggestion checks, and product recommendation research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Crawlora API key could be sent to an unintended API host if CRAWLORA_API_BASE is overridden.

Mitigation: Keep CRAWLORA_API_BASE unset or verify that it points to https://api.crawlora.net/api/v1 before using the helper.

Risk: The API helper can call broader Crawlora endpoints than the Shopify-focused skill description advertises.

Mitigation: Use only the documented /shopify endpoints unless broader Crawlora access is intentional and reviewed.

Risk: Storefront research may collect public catalog and page data from third-party Shopify stores.

Mitigation: Limit use to public data and respect the target store's applicable terms and access expectations.

## Reference(s):

- [Shopify endpoint reference](artifact/reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/shopify-research)
- [Publisher profile](https://clawhub.ai/user/tonywangcn)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and a public Shopify storefront URL for each request.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
