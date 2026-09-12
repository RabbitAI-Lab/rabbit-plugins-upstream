## Description:

Researches Wish's marketplace - categories, product search, product detail, related items, and reviews - using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to research public Wish marketplace categories, products, prices, ratings, related items, and reviews through Crawlora rather than scraping Wish pages directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Crawlora API key and sends Wish research queries to Crawlora.

Mitigation: Install only where sharing those queries with Crawlora is acceptable, keep the key in CRAWLORA_API_KEY, and rotate or revoke the key if it is exposed.

Risk: Security evidence reports that the helper can make broader authenticated Crawlora POST requests than the documented read-only Wish endpoints require.

Mitigation: Review the helper before use and restrict use to the documented Wish research endpoints needed for the task.

## Reference(s):

- [Wish endpoint reference](artifact/reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/wish-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY and Crawlora Wish endpoints; API responses are normalized JSON.]

## Skill Version(s):

1.0.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
