## Description:

Researches independent Shopify-powered storefronts using the Crawlora API, including products, collections, pages, sitemaps, search suggestions, and product recommendations for any store domain plus pre-wired brand storefronts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and commerce operators use this skill to audit public Shopify storefront catalogs, inspect product and collection data, crawl sitemaps, and research search or recommendation behavior through Crawlora's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Storefront domains, product handles, search terms, and similar research inputs are sent to the third-party Crawlora API.

Mitigation: Use only public or policy-approved research inputs, and do not submit secrets, private customer data, or confidential target lists unless third-party API use is approved.

Risk: The helper requires a Crawlora API key.

Mitigation: Keep the key in CRAWLORA_API_KEY, avoid hardcoding or committing it, and review commands before execution.

Risk: The skill is designed for public storefront research and may be constrained by storefront terms, pagination, and endpoint limits.

Mitigation: Respect each store's terms, paginate deliberately, and verify empty result pages before concluding that data is absent.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/shopify-research)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends user-supplied storefront domains, product handles, search terms, and related research inputs to Crawlora.]

## Skill Version(s):

1.0.15 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
