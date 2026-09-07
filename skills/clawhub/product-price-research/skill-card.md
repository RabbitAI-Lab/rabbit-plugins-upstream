## Description:

Researches products, prices, sellers, and reviews across major online marketplaces and retailers using the Crawlora API, returning normalized JSON for product discovery, price comparison, seller checks, listing tracking, and review lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to research public product listings, compare prices and sellers, inspect variants and availability, and retrieve available reviews across supported marketplaces without scraping store pages directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The authenticated helper can send the Crawlora API key to an unvalidated CRAWLORA_API_BASE override URL.

Mitigation: Use only a trusted API base, restrict who can set CRAWLORA_API_BASE, and validate the base before running the helper.

Risk: Product, seller, review, or search terms may be sent to Crawlora and downstream public marketplace endpoints.

Mitigation: Avoid sensitive, proprietary, or personal terms unless the user is comfortable sharing them with Crawlora.

Risk: The helper exposes broader Crawlora API access than the stated shopping workflow.

Mitigation: Limit calls to approved product research and shopping endpoints for the deployment environment.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/product-price-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [JSON from Crawlora API calls, with concise Markdown summaries or shell command examples when useful]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; optional CRAWLORA_API_BASE override should be controlled by the user environment.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
