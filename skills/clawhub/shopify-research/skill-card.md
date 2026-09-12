## Description:

Researches independent Shopify-powered storefronts using the Crawlora API, returning normalized JSON for products, collections, pages, sitemaps, search suggestions, and product recommendations across any public Shopify store plus 14 pre-wired brand storefronts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and commerce analysts use this skill to audit public Shopify storefront catalogs, enumerate sitemap URLs, inspect product or page handles, and research search or recommendation behavior without scraping storefront HTML directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends public storefront URLs, product handles, and search terms to the third-party Crawlora API under the user's API key.

Mitigation: Use only approved public storefront targets and avoid secrets, private internal targets, or proprietary research terms unless third-party API use has been approved.

Risk: The helper requires a Crawlora API key to call external endpoints.

Mitigation: Store the key only in CRAWLORA_API_KEY; the artifact validates the key format and keeps it out of command-line arguments.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/shopify-research)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and works with public Shopify storefront URLs or documented brand-pinned endpoints.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
