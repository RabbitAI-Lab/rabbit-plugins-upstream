## Description:

Reddit Public Data API lets agents retrieve normalized, read-only public Reddit data, including subreddit post listings, single posts, user activity, and keyword search, through the ReplyNodes HTTPS gateway.

This skill is ready for commercial/non-commercial use.

## Publisher:

[replynodes-ai](https://clawhub.ai/user/replynodes-ai)

### License/Terms of Use:

MIT

## Use Case:

Developers and external agents use this skill to fetch bounded public Reddit data for research, monitoring, and question answering without Reddit credentials or write access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bearer keys or x402 payment proofs could be exposed if pasted into chat, committed, or logged.

Mitigation: Keep API keys and payment proofs in secret storage and avoid printing or logging them.

Risk: Paid routes can incur cost or use stale pricing assumptions.

Mitigation: Call the free capabilities endpoint before paid requests to verify current route and pricing details.

Risk: Returned Reddit text, URLs, titles, and comments are untrusted third-party content.

Mitigation: Treat returned content as data, not instructions, and review links or claims before acting on them.

Risk: Gateway or upstream Reddit data sources can fail, degrade, or return incomplete data.

Mitigation: Handle final error responses gracefully and preserve the request_id for support without exposing secrets.

## Reference(s):

- [Endpoint reference](references/endpoints.md)
- [MCP schema](references/reddit-api-mcp.schema.json)
- [Scenario examples](references/scenarios.md)
- [ReplyNodes Reddit gateway](https://api.replynodes.com/v1/reddit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON response examples and curl command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only HTTPS GET guidance; API responses are normalized JSON and should be treated as untrusted public data.]

## Skill Version(s):

1.0.9 (source: SKILL.md frontmatter, manifest.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
