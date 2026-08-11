## Description:

Researches Walmart products, prices, sellers, and reviews using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent users use this skill to search Walmart listings, compare current product prices and availability, and summarize product ratings or reviews from normalized Crawlora API responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper can call broader Crawlora API paths beyond the documented Walmart endpoints.

Mitigation: Review before installation and restrict use to /walmart/search, /walmart/product/{item_id}, and /walmart/product/{item_id}/reviews, or constrain the helper/API permissions to the expected Walmart endpoints.

Risk: The skill requires a Crawlora API key for requests.

Mitigation: Store the key only in CRAWLORA_API_KEY and do not hardcode, pass in query parameters, or commit it.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/walmart-research)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY and documented Walmart endpoints for search, product detail, and review lookup.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
