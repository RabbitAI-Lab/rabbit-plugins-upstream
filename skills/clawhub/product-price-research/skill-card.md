## Description:

Researches product listings, prices, sellers, and reviews across online retailers through the Crawlora API for comparison and purchasing research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Shoppers, researchers, and commerce teams use this skill to find retail products, compare prices and sellers, and review product feedback across supported marketplaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product queries, seller lookups, reviews, and supplied store-locator locations are sent to Crawlora.

Mitigation: Share only necessary search terms and locations; omit secrets, proprietary terms, and unnecessary personal data.

Risk: The Crawlora API key could be exposed if included in commands or shared outputs.

Mitigation: Keep CRAWLORA_API_KEY private in the environment and never include it in query parameters or published results.

## Reference(s):

- [Skill endpoint reference](artifact/reference/endpoints.md)
- [Product Price Research on ClawHub](https://clawhub.ai/crawlora-org/skills/product-price-research)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands]

**Output Format:** [Markdown research summaries and normalized JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Price, currency, seller, and review availability vary by retailer; results may be paginated.]

## Skill Version(s):

1.0.22 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
