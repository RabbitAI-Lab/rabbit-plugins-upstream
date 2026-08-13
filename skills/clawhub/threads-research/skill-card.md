## Description:

Researches public Threads (Meta) profiles, posts, replies, and search results via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and social-listening teams use this skill to inspect public Threads profiles, posts, replies, and keyword search results through the Crawlora API instead of scraping Threads directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can send arbitrary requests with the user's Crawlora API key.

Mitigation: Use only the documented read-only Threads endpoints and review commands before execution.

Risk: The API key could be exposed if placed in source files, query parameters, or logs.

Mitigation: Store CRAWLORA_API_KEY in secure environment storage and never commit or print it.

Risk: Changing CRAWLORA_API_BASE can route requests and credentials to an unintended endpoint.

Mitigation: Set CRAWLORA_API_BASE only when the endpoint is intentionally trusted.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON responses with Markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses public Threads data and requires CRAWLORA_API_KEY.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
