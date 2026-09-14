## Description:

Researches Old Navy's catalog and its Gap Inc. sibling storefronts Gap, Banana Republic, and Athleta for categories, products, colors, sizes, in-store pickup availability, and reviews using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and shopping research agents use this skill to search and browse Old Navy, Gap, Banana Republic, and Athleta product data, check color and size details, review in-store pickup availability, find nearby stores, and summarize customer reviews without scraping storefront HTML.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Catalog, review, inventory, and store-location requests are sent to Crawlora as a third-party API provider.

Mitigation: Install only when third-party API use is acceptable, and prefer zip code or city lookup over exact coordinates unless precise location is needed.

Risk: The Crawlora API key could be exposed if hardcoded, committed, or passed in command-line arguments.

Mitigation: Keep CRAWLORA_API_KEY in the environment, do not commit it, and use the provided helper so the key is supplied through a private curl config.

Risk: Retail search relevance and availability data can be best-effort or change quickly.

Mitigation: Verify pricing, product fit, and local pickup stock before relying on results for purchase or recommendation decisions.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; API responses cover public retail catalog, review, inventory, and store-location data.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
