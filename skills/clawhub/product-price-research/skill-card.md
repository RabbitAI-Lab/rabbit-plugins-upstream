## Description:

Researches product listings, prices, sellers, and reviews across online marketplaces and retailers through the Crawlora API to support comparison and monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Shoppers, researchers, and commerce teams use this skill to find products and compare retailer prices, seller details, availability, and reviews without scraping storefront pages directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product queries and request parameters are sent to Crawlora with an API key.

Mitigation: Keep the key secret and avoid including personal or sensitive data in lookup queries.

Risk: Competitive monitoring, live inventory figures, and regulated-product attributes can require extra care.

Mitigation: Review the endpoint reference and verify source data before using results for consequential decisions.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/product-price-research)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Markdown summaries and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on retailer coverage and may be paginated.]

## Skill Version(s):

1.0.21 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
