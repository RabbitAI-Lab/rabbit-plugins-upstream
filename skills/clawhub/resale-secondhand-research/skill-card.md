## Description:

Researches secondhand, resale, and handmade marketplaces via the Crawlora API - Poshmark, Etsy, Vinted, StockX, Mercari, Depop, and Whatnot - returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and shopping researchers use this skill to search, compare, and vet public marketplace listings, sellers, shops, sneaker resale prices, handmade goods, vintage goods, and livestream shopping events through Crawlora API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper requires a Crawlora API key and makes authenticated requests to Crawlora.

Mitigation: Install only where sharing the Crawlora API key with the helper is acceptable, keep the key in CRAWLORA_API_KEY, and do not hardcode or commit it.

Risk: The security summary says the API helper is broader than the main description and allows POST and nested routes beyond the documented read-only catalog.

Mitigation: Review or tighten route and method checks before automated use, especially when untrusted prompts can choose helper arguments.

Risk: Marketplace data may be incomplete, stale, or constrained by endpoint-specific requirements such as StockX and Whatnot category inputs.

Mitigation: Check the endpoint reference before calling required-parameter routes and treat returned marketplace data as research input rather than a purchase or valuation guarantee.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY from the environment and returns normalized public marketplace data.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
