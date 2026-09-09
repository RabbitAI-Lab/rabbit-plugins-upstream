## Description:

Browses Wayfair's category taxonomy and pulls category product grids and product detail (price, brand, stock status, rating, variants, images) using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and shopping research agents use this skill to browse Wayfair categories, inspect category product grids, and retrieve product details through Crawlora rather than scraping Wayfair pages directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper uses outbound network access with a Crawlora API key and can call paths beyond the documented Wayfair endpoints.

Mitigation: Limit use to /wayfair/categories, /wayfair/category, and /wayfair/product/{id}; review calls before execution.

Risk: Changing CRAWLORA_API_BASE could send the Crawlora API key to an unintended destination.

Mitigation: Avoid setting CRAWLORA_API_BASE and keep the API key in CRAWLORA_API_KEY only.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/wayfair-research)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns paginated public Wayfair category and product data.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
