## Description:

Researches Reddit via the Crawlora API for subreddit posts/comments/about, a single post plus its comment thread, keyword search, user post/comment history, domain-linked posts, and hot/new/rising/top trends, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query public Reddit posts, comments, user histories, search results, domain-linked posts, and trends through Crawlora for community research, sentiment review, and brand or competitor monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can send the Crawlora API key to an overridden API host.

Mitigation: Do not set CRAWLORA_API_BASE unless the destination is fully trusted; prefer the official Crawlora API base.

Risk: The helper can make broader authenticated Crawlora API requests than the documented Reddit GET endpoints.

Mitigation: Restrict use to the documented Reddit endpoints or revise the helper to validate the official API base and allowlist those endpoints.

Risk: Research prompts or identifiers may be sent to a third-party API provider.

Mitigation: Avoid sending private or sensitive data through the helper, and only use the skill when sharing the requested public Reddit query with Crawlora is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/reddit-research)
- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY; API calls return paginated public Reddit data as normalized JSON.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
