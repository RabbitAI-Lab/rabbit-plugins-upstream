## Description:

Researches anime and manga titles via the Crawlora API for search, title details, characters, staff, recommendations, rankings, and airing schedules, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to answer anime and manga research questions with public title, character, staff, ranking, recommendation, and airing-schedule data from Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and requested lookup parameters are sent to Crawlora using the configured Crawlora API key.

Mitigation: Use a dedicated Crawlora API key and avoid sending private or sensitive text as search input.

Risk: API-key handling mistakes could expose credentials during manual API calls.

Mitigation: Keep the key in CRAWLORA_API_KEY and use the bundled helper, which keeps the key out of query parameters and command-line arguments.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the CRAWLORA_API_KEY environment variable and paginated Crawlora endpoints for public anime and manga data.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
