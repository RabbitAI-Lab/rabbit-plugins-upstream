## Description:

Browses Wayfair category taxonomy, category product grids, and product details through the Crawlora API and returns normalized JSON for product research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to browse Wayfair departments, inspect category product grids, and retrieve product price, brand, stock status, rating, variant, and image data by product id.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper can call broader Crawlora API paths beyond the Wayfair endpoints described by the skill.

Mitigation: Restrict agent use to the documented Wayfair endpoints or review commands before execution in environments where Crawlora credit spend matters.

Risk: The skill requires an authenticated Crawlora API key and successful requests may consume Crawlora credits.

Mitigation: Use a dedicated Crawlora key, keep it in CRAWLORA_API_KEY, and monitor usage or set external account limits where available.

## Reference(s):

- [Wayfair endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/wayfair-research)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and may consume Crawlora credits for successful API calls.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
