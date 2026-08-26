## Description:

Researches anime and manga titles via the Crawlora API - search, title detail, characters, staff, recommendations, rankings, and airing schedules - returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search anime and manga titles, retrieve title details, cast, staff, recommendations, rankings, and airing schedules as normalized JSON from Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can send the API key and arbitrary requests to non-anime Crawlora endpoints or to an untrusted API base if misconfigured.

Mitigation: Restrict use to the documented /anime and /manga endpoints, avoid setting CRAWLORA_API_BASE to an untrusted URL, and do not include private data in searches.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/anime-manga-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY and paginated Crawlora API endpoints.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
