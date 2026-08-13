## Description:

Researches independent Shopify-powered storefronts - products, collections, pages, sitemaps, search suggestions, and product recommendations - using the Crawlora API, returning clean JSON for any store by domain.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and commerce analysts use this skill to inspect public Shopify storefront catalogs, pages, sitemaps, search suggestions, and product recommendations through Crawlora instead of direct page scraping.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper can call non-Shopify Crawlora endpoints, beyond the skill's stated Shopify research purpose.

Mitigation: Constrain use to documented /shopify/* paths and review generated API calls before execution.

Risk: The skill sends requests to Crawlora using an API key.

Mitigation: Keep CRAWLORA_API_KEY in the environment only, avoid committing it, and confirm that collection is limited to public storefront data.

## Reference(s):

- [shopify-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub release page](https://clawhub.ai/tonywangcn/skills/shopify-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; Shopify endpoint results may be paginated and consume Crawlora credits.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
