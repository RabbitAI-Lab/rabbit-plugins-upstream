## Description:

Fetches structured public web data via the Crawlora REST API -- search engines, e-commerce, social, finance, maps, app stores, media, and reviews -- returning clean JSON instead of HTML.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use Crawlora to fetch structured JSON from public websites for product research, search results, reviews, transcripts, trends, finance, places, and similar data-gathering tasks that would otherwise require scraping or parsing HTML.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a Crawlora API key.

Mitigation: Store the key only in CRAWLORA_API_KEY, avoid hardcoding or committing it, and install the skill only where agent access to that key is acceptable.

Risk: The broad catalog includes account usage endpoints and persistent website monitor create, update, and delete actions.

Mitigation: Require explicit user confirmation before monitor changes and avoid account or monitor endpoints unless the task specifically calls for them.

Risk: The skill is intended for public web data and may receive user-supplied URLs or queries.

Mitigation: Use it only for public data, avoid secrets and private URLs, and respect source-site terms and rate limits.

## Reference(s):

- [Crawlora endpoint catalog](artifact/reference/catalog.md)
- [Crawlora website](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/crawlora)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns public web data from Crawlora endpoints.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
