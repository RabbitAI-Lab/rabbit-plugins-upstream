## Description:

Fetches structured public web data through the Crawlora REST API across search, commerce, social, finance, maps, app stores, media, and reviews, returning JSON instead of scraped HTML.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to retrieve live public-web data such as product prices, search results, reviews, transcripts, trends, finance data, places, and listings through a normalized API instead of scraping HTML.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and endpoint parameters are sent to Crawlora as a third-party API provider.

Mitigation: Use the skill only for public-web lookups, keep the API key in CRAWLORA_API_KEY, and avoid sensitive or private queries, precise addresses, coordinates, or personal identifiers unless deliberately approved.

Risk: Returned public-web data can be incomplete, stale, challenged by upstream sites, or subject to source-specific terms and rate limits.

Mitigation: Review the returned JSON before relying on it, retry or use alternate providers when endpoints fail, and respect source terms and rate limits.

## Reference(s):

- [Crawlora ClawHub skill page](https://clawhub.ai/crawlora-org/skills/crawlora)
- [Crawlora endpoint catalog](reference/catalog.md)
- [Crawlora API site](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses the documented Crawlora public-web endpoint catalog.]

## Skill Version(s):

1.0.25 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
