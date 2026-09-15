## Description:

Researches products, prices, sellers, and reviews across major online marketplaces and big-box/specialty retailers using the Crawlora API, returning clean JSON instead of scraping store pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and shopping analysts use this skill to compare product prices, sellers, listings, availability, and reviews across supported marketplaces and retailers through normalized Crawlora API responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shopping searches, product identifiers, retailer URLs, and optional store-location inputs are sent to Crawlora's API.

Mitigation: Share only the data needed for the task, avoid precise location unless local store or availability lookup requires it, and confirm that users are comfortable using the third-party API.

Risk: The Crawlora API key could be exposed if it is hardcoded, committed, or passed in URLs.

Mitigation: Keep CRAWLORA_API_KEY private in the environment and use the provided helper so the key is sent as a header rather than as a command-line argument or query parameter.

Risk: Product, price, review, and availability data may be incomplete or change after retrieval.

Mitigation: Treat results as research inputs and verify important prices, stock status, seller details, and terms with the retailer before acting on them.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora website](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/product-price-research)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, JSON]

**Output Format:** [Markdown guidance with inline shell commands and normalized JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends product, seller, review, retailer URL, and optional store-location inputs to Crawlora.]

## Skill Version(s):

1.0.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
