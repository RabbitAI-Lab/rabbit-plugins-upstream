## Description:

Researches Sam's Club's catalog -- department/category navigation, category product grids, product detail with pricing/availability/ratings, related-item shelves, and curated content pages -- using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to browse Sam's Club departments and categories, inspect product pricing, availability, ratings, and related items, and retrieve curated content pages through Crawlora-backed JSON endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Crawlora API key could be sent to an arbitrary API host if the helper is run with an overridden API base.

Mitigation: Use only the documented Crawlora API host and avoid using a sensitive or high-value Crawlora key until the helper validates or pins the API base.

Risk: The helper can call paths beyond the documented Sam's Club GET endpoints.

Mitigation: Limit use to the documented Sam's Club endpoints and review requested paths before running commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/samsclub-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; uses public Sam's Club catalog endpoints exposed by Crawlora.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
