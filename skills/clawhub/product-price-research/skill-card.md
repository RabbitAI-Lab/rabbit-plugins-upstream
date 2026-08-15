## Description:

Researches products, prices, sellers, and reviews across 20 major online marketplaces and big-box/specialty retailers using the Crawlora API, returning clean JSON for product discovery, price comparison, seller checks, listing tracking, and review lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research teams use this skill to query Crawlora marketplace endpoints for product prices, seller information, listing details, availability, and reviews across supported retailers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can call broader Crawlora API paths than the stated marketplace-research purpose needs.

Mitigation: Prefer only the documented marketplace endpoints and add endpoint allowlisting before broader deployment.

Risk: Product research terms, store URLs, seller names, and lookup IDs are sent to Crawlora.

Mitigation: Avoid confidential business research unless stricter input validation and endpoint controls are added.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/product-price-research)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns normalized marketplace data from Crawlora endpoints.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
