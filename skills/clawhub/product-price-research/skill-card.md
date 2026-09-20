## Description:

Researches products, prices, sellers, and reviews across major online marketplaces and big-box/specialty retailers using the Crawlora API and returns clean JSON for comparison and review workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external agents use this skill to find products, compare marketplace or retailer prices, inspect sellers, track listings, and summarize public reviews without scraping retailer pages directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product queries, retailer URLs, seller names, and store-locator ZIP, address, or coordinate inputs are sent to Crawlora.

Mitigation: Use the skill only when third-party processing by Crawlora is acceptable, and avoid precise personal location or other sensitive inputs unless they are required for the task.

Risk: The helper requires a Crawlora API key.

Mitigation: Store the key only in CRAWLORA_API_KEY; do not hardcode it, pass it in query parameters, or commit it to source control.

Risk: Retailer coverage and endpoint behavior vary by platform, including some retailers without keyword search, product details, or review endpoints.

Mitigation: Consult the endpoint reference before use and explain coverage gaps when results are incomplete or unavailable.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/product-price-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the CRAWLORA_API_KEY environment variable and returns normalized public product, price, seller, store, and review data from documented Crawlora API routes.]

## Skill Version(s):

1.0.18 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
