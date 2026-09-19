## Description:

Researches Bluesky profiles, posts, follower and follows graphs, account search, and trending topics via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and analysts use this skill to look up public Bluesky account profiles, recent posts, post threads, follower and follows graphs, account search results, and trending topics through Crawlora instead of scraping Bluesky directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crawlora receives the API key and query details when the helper runs.

Mitigation: Provide the key only through CRAWLORA_API_KEY and avoid using private or sensitive text as search terms.

Risk: The skill depends on a third-party service for public Bluesky lookups.

Mitigation: Install it only when Crawlora is an acceptable third-party service for the intended use case.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and is limited to public Bluesky data available through Crawlora.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
