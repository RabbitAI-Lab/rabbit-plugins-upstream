## Description:

Researches Reddit via the Crawlora API - subreddit posts/comments/about, a single post plus its comment thread, keyword search, user post/comment history, domain-linked posts, and hot/new/rising/top trends - returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and community researchers use this skill to query public Reddit posts, comments, user history, subreddit activity, domain-linked posts, and trends through Crawlora for sentiment, brand monitoring, competitor research, and thread analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security summary says the skill under-discloses a lead-generation endpoint.

Mitigation: Install only if lead discovery is acceptable for the intended use, and review the endpoint reference before using paths beyond ordinary Reddit research.

Risk: The server security guidance says the helper can call broader Crawlora API paths, not only Reddit endpoints.

Mitigation: Keep the Crawlora API key limited to this intended use and review generated shell commands so they call only acceptable Crawlora endpoints.

## Reference(s):

- [reddit-research endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON API responses with Markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; list endpoints are cursor-paginated and temporary Reddit throttling may require retrying after the Retry-After delay.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
