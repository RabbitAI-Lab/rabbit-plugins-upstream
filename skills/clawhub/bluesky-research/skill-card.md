## Description:

Researches Bluesky profiles, posts, follower/follows graphs, account search, and trending topics via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to retrieve public Bluesky profile, post, thread, graph, search, and trending-topic data through Crawlora instead of scraping the Bluesky app or calling the AT Protocol directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill sends Bluesky handles, post URIs, search terms, and the Crawlora API key to Crawlora.

Mitigation: Use it only when that data sharing is acceptable, keep the API key in CRAWLORA_API_KEY, and avoid private or sensitive data.

Risk: The skill is designed for public Bluesky data and may be unsuitable for private or sensitive investigations.

Mitigation: Limit use to public Bluesky profiles, posts, graph data, account search, and trending topics.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/bluesky-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY and supports cursor-paginated public Bluesky endpoints.]

## Skill Version(s):

1.0.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
