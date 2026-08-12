## Description:

Researches Bluesky profiles, posts, follower and follows graphs, account search, and trending topics via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to retrieve public Bluesky profile, post, thread, follower, follows, account-search, and trending-topic data through Crawlora instead of scraping Bluesky or calling the AT Protocol directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can send requests to Crawlora beyond the stated Bluesky-only purpose.

Mitigation: Constrain agent use to the documented /bluesky endpoints when the same Crawlora key must not be used for unrelated services.

Risk: Requests and API credentials involve a third-party Crawlora service.

Mitigation: Keep the key in CRAWLORA_API_KEY, avoid embedding credentials in commands or files, and review outbound requests before execution.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/bluesky-research)

## Skill Output:

**Output Type(s):** [JSON, API Calls, Shell commands, Guidance]

**Output Format:** [JSON responses with Markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns public Bluesky data from Crawlora endpoints.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
