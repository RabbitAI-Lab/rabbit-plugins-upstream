## Description:

Browses Wayfair's category taxonomy and pulls category product grids and product detail (price, brand, stock status, rating, variants, images) using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to browse Wayfair categories, inspect category product grids, and retrieve product details through Crawlora instead of scraping Wayfair directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wayfair category/product queries and the Crawlora API key are sent to Crawlora.

Mitigation: Use a dedicated Crawlora API key, monitor credit usage, and avoid sending sensitive query context.

Risk: The helper comments include stale generic examples that are outside the Wayfair endpoint set.

Mitigation: Use only the documented Wayfair endpoints in artifact/reference/endpoints.md.

## Reference(s):

- [wayfair-research endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/wayfair-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends user-directed Wayfair category or product requests to Crawlora.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
