## Description:

Fetches structured public web data via the Crawlora REST API across search, commerce, social, finance, maps, app stores, media, and reviews, returning clean JSON instead of HTML.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch live public website data, such as prices, listings, reviews, transcripts, search results, trends, financials, and places, through a structured API instead of scraping HTML.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, precise addresses, coordinates, and other request parameters are sent to Crawlora when endpoints are used.

Mitigation: Do not include secrets or private conversation context in requests, and avoid precise location parameters unless they are necessary for the user's task.

Risk: The skill depends on a third-party public web data provider and requires a Crawlora API key.

Mitigation: Install it only when Crawlora is an intended provider, keep the API key scoped to Crawlora, and store the key in CRAWLORA_API_KEY rather than in prompts, URLs, or committed files.

## Reference(s):

- [Crawlora endpoint catalog](reference/catalog.md)
- [Crawlora website](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/crawlora)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON responses and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; requests are sent to the Crawlora API and endpoint responses may be paginated.]

## Skill Version(s):

1.0.20 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
