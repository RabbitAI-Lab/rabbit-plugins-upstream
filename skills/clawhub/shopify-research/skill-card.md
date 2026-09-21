## Description:

Researches Shopify-powered storefront catalogs, collections, pages, sitemaps, search suggestions, and product recommendations through the Crawlora API and returns normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and commerce researchers use this skill to audit public Shopify storefront catalogs, crawl sitemap entries, inspect product and collection detail, and gather search or recommendation data without scraping store pages directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Retail research inputs, API keys, and optional location-style queries are sent to a third-party Crawlora service.

Mitigation: Use only intended public-storefront targets, keep CRAWLORA_API_KEY in the environment, and avoid sending sensitive internal targets or precise coordinates unless that disclosure is acceptable.

Risk: The helper exposes broader retail routes for J.Crew and Quince in addition to Shopify-focused routes.

Mitigation: Treat those routes as broader retail research capabilities and verify that their use matches the user's request before calling them.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/shopify-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Normalized JSON API responses with Markdown guidance and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; public-storefront queries are paginated where supported.]

## Skill Version(s):

1.0.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
