## Description:

Researches Bluesky profiles, posts, follower/follows graphs, account search, and trending topics via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and social media analysts use this skill to retrieve normalized JSON for public Bluesky profiles, posts, threads, follower/follows graphs, account search, and trending topics through the Crawlora API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can use the configured Crawlora API key against arbitrary Crawlora endpoints beyond the documented Bluesky endpoints.

Mitigation: Install only when agents are allowed to use the Crawlora key, and constrain usage to the documented Bluesky endpoint paths.

Risk: The skill depends on a third-party API key that could be exposed if hardcoded, logged, committed, or passed in URLs.

Mitigation: Store the key only in CRAWLORA_API_KEY, avoid query-parameter secrets, and review agent outputs before sharing logs or transcripts.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/bluesky-research)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; list endpoints are cursor-paginated.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
