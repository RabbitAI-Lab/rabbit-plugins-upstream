## Description:

Researches independent Shopify-powered storefronts, including products, collections, pages, sitemaps, search suggestions, and product recommendations, using the Crawlora API and returning normalized JSON for any store by domain plus pre-wired brand storefronts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and commerce researchers use this skill to inspect public Shopify storefront catalog, page, sitemap, search, and recommendation data without scraping storefront HTML directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Crawlora API key and sends storefront targets, searches, handles, and other request parameters to Crawlora.

Mitigation: Use a scoped Crawlora key where possible, keep the key in CRAWLORA_API_KEY, and avoid sending secrets, internal URLs, private research targets, or sensitive prompt content.

Risk: The included helper script can call broader Crawlora endpoints beyond the Shopify-focused workflow.

Mitigation: Review requested paths before execution and restrict use to the Shopify or documented brand storefront endpoints needed for the task.

Risk: The skill works with public storefront data that may still be subject to each store's terms and usage expectations.

Mitigation: Use it for public catalog research, respect storefront terms, and avoid attempting to access private or non-public resources.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; API responses are paginated where supported and returned as JSON.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
