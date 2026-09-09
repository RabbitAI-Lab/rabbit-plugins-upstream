## Description:

Researches Walmart products, prices, sellers, and reviews using the Crawlora API and returns clean JSON for product discovery, price comparison, listing tracking, and review pulls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and shopping research agents use this skill to query Walmart product search, detail, and review endpoints through Crawlora. It supports price comparison, seller review, availability checks, catalog research, and review summaries using normalized JSON from public Walmart data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora wrapper can send the user's API key to a configurable API base if CRAWLORA_API_BASE is set.

Mitigation: Do not set CRAWLORA_API_BASE unless the destination is trusted; prefer validating or hardcoding the Crawlora API host before deployment.

Risk: The bundled script is a general Crawlora API wrapper while this skill is intended for Walmart research.

Mitigation: Limit use to the documented Walmart GET paths: /walmart/search, /walmart/product/{item_id}, and /walmart/product/{item_id}/reviews.

## Reference(s):

- [Walmart endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; requests should stay within the documented Walmart GET endpoints.]

## Skill Version(s):

1.0.8 (source: server release metadata, released 2026-09-08)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
