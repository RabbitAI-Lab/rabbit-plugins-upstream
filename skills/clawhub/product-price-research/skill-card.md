## Description:

Researches product listings, prices, sellers, and reviews across online marketplaces and retailers through the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Shoppers, analysts, and developers use this skill to find products, compare retailer prices and sellers, and review public listings and customer feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product searches, retailer URLs or IDs, review lookups, and store-locator inputs are sent to Crawlora.

Mitigation: Share only inputs appropriate for the service and review Crawlora and retailer terms for the intended use.

Risk: A disclosed API key could enable unauthorized use of the Crawlora account.

Mitigation: Keep CRAWLORA_API_KEY in the environment and avoid sharing logs or transcripts that expose it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/product-price-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora API and account setup](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown responses with structured product data and optional shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Product results depend on retailer coverage, available fields, and pagination.]

## Skill Version(s):

1.0.20 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
