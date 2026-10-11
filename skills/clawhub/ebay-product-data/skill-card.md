## Description:

Guides agents through Scavio API searches for live and sold eBay listings, full listing details, and public seller profiles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other eBay marketplace users can research sold prices, find live listings, examine individual items, and check public seller profiles through Scavio's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, item IDs, seller names, and the API key are sent to Scavio's external API.

Mitigation: Avoid sensitive private search inputs and keep the API key in a secret store or environment variable.

Risk: API requests may consume paid credits after the free allowance.

Mitigation: Monitor the credit balance and approve paid usage before making repeated requests.

Risk: Historical sold prices or ineffective category filters could mislead pricing decisions.

Mitigation: Include sale dates and listing links, and verify category IDs before relying on filtered results.

## Reference(s):

- [Scavio eBay search documentation](https://scavio.dev/docs/ebay-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=ebay-product-data)
- [Scavio eBay product documentation](https://scavio.dev/docs/ebay-product?utm_source=agent-skills&utm_medium=skill&utm_campaign=ebay-product-data)
- [Scavio eBay seller documentation](https://scavio.dev/docs/ebay-seller?utm_source=agent-skills&utm_medium=skill&utm_campaign=ebay-product-data)
- [Scavio API rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=ebay-product-data)

## Skill Output:

**Output Type(s):** [Text, JSON, Code, Shell commands]

**Output Format:** [Markdown guidance with structured JSON results and optional code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Listing URLs support verification; sold prices should include sale dates.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
