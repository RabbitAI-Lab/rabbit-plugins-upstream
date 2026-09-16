## Description:

Discovers and compares public podcast shows, episodes, charts, rankings, and related programs using Apple Podcasts and Spotify Podcasts through the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research teams use this skill to discover podcast shows and episodes, compare platform chart snapshots, inspect public show metadata, and build bounded guest or partnership shortlists from public episode evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Podcast search terms, platform IDs, and query parameters are sent to Crawlora with the user's Crawlora API key.

Mitigation: Avoid sending private notes, secrets, unrelated personal data, or sensitive research terms in Crawlora queries.

Risk: Podcast descriptions, show notes, charts, and rankings may be promotional, incomplete, locale-specific, or time-sensitive.

Mitigation: Preserve source URLs, retrieval time, platform, market, category, and chart context, and do not infer downloads, audience size, or revenue from rankings.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/podcast-discovery-research)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Markdown, Configuration]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; queries are limited to documented Apple Podcasts and Spotify Podcasts Crawlora endpoints.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
