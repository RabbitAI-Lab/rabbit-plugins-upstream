## Description:

Browses Wayfair category taxonomy and retrieves category product grids and product details, including price, brand, stock status, ratings, variants, and images, through the Crawlora API as normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and shopping analysts use this skill to browse Wayfair categories, inspect category product grids, and look up specific Wayfair products by W-prefixed product id without scraping wayfair.com.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Crawlora as a third-party API provider and sends category or product lookup parameters to that service.

Mitigation: Install only if that provider relationship is acceptable, avoid private data in lookup parameters, and review Crawlora and Wayfair terms before use.

Risk: API keys can be exposed if they are hardcoded, committed, or passed in URLs.

Mitigation: Provide the key only through CRAWLORA_API_KEY and use the included helper, which keeps the key out of command-line arguments.

Risk: The skill is narrow: it has category browsing and product detail endpoints, but no full-text product search or reviews endpoint.

Mitigation: Use category taxonomy and W-prefixed product ids for discovery, and verify important product or review details against current Wayfair sources when needed.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Wayfair Research on ClawHub](https://clawhub.ai/crawlora-org/skills/wayfair-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON responses and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; endpoints are GET-only and limited to Wayfair categories, category pages, and product detail.]

## Skill Version(s):

1.0.16 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
