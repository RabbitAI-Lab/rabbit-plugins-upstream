## Description:

Queries Crawlora's pre-built hosted datasets across markets, apps, social profiles, jobs, housing, businesses, books, finance, games, and other public-data domains through search, facet, item, and nearby endpoints that return JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, analysts, and agents use this skill to query Crawlora's pre-indexed public datasets for bulk research, aggregate faceting, filtered search, item lookup, and nearby analysis instead of crawling each source live.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the user's Crawlora API key and chosen query parameters, filters, and coordinates to Crawlora.

Mitigation: Store the key only in CRAWLORA_API_KEY, and avoid sending secrets or private personal data in query parameters unless that transmission is intended.

Risk: Hosted datasets refresh on a schedule and may not reflect real-time source state.

Mitigation: Use the skill for indexed bulk and aggregate research, and verify time-sensitive facts with a live source or a platform-specific real-time lookup.

Risk: Large result sets are paginated, so a single request may not cover the full population.

Mitigation: Follow page and page-size guidance in the endpoint reference and walk pages when complete coverage is required.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora hosted skill page](https://clawhub.ai/crawlora-org/skills/crawlora-datasets)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Raw JSON from GET requests, with Markdown instructions and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; requests are GET-only and paginated.]

## Skill Version(s):

1.0.18 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
