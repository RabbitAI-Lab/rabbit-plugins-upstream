## Description:

Researches video games via the Crawlora API, including Steam store pages, pricing, reviews, player counts, charts, tags, achievements, and PlayStation Store products, categories, and deals, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to research public video game storefront data, compare prices and reviews, check player activity, find trending or discounted games, and retrieve normalized store listing details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper uses a Crawlora API key and can consume Crawlora credits.

Mitigation: Keep the key in CRAWLORA_API_KEY, restrict use to intended game endpoints, and monitor credit usage.

Risk: POST request bodies could send private text to the Crawlora API.

Mitigation: Avoid putting private or sensitive text in request bodies.

Risk: The security review found the helper route and method surface broader than the main Steam and PlayStation description.

Mitigation: Review requests before execution and narrow usage to the documented game-research endpoints.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/gaming-research)
- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY. Responses use public game-store data and can vary by country and language parameters.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
