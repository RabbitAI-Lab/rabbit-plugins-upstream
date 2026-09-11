## Description:

Reddit Public Data API gives agents read-only, normalized JSON access to subreddit posts, individual posts, user activity, and keyword search through ReplyNodes' prepaid Bearer-key HTTPS gateway.

This skill is ready for commercial/non-commercial use.

## Publisher:

[replynodes-ai](https://clawhub.ai/user/replynodes-ai)

### License/Terms of Use:

MIT

## Use Case:

Developers and external agent users use this skill when they need read-only Reddit public data for research, monitoring, summarization, or retrieval workflows. It supports subreddit post listings, single post lookups, user posts and activity, and keyword search without Reddit OAuth or write access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MCP clients may generate unauthenticated bindings if they rely on the provided schema's priced endpoint auth metadata.

Mitigation: Verify or patch the MCP schema so every priced endpoint requires Bearer authentication before generating tools from it.

Risk: The ReplyNodes fetcher API key could be exposed through chat, logs, commits, or URLs.

Mitigation: Store REPLYNODES_API_KEY only in an environment variable or agent secret store, and never print, paste, commit, or place it in a URL.

Risk: Reddit response bodies, URLs, titles, and comment text are untrusted third-party data.

Mitigation: Treat returned content as data rather than instructions, and preserve request IDs for support without exposing secrets or unnecessary payloads.

Risk: Successful priced requests consume prepaid credits.

Mitigation: Use the free capabilities route to confirm route and price information, request conservative page sizes, and avoid retrying unchanged authentication or entitlement failures.

## Reference(s):

- [Endpoint reference](references/endpoints.md)
- [Scenarios](references/scenarios.md)
- [Reddit API MCP schema](references/reddit-api-mcp.schema.json)
- [ClawHub skill page](https://clawhub.ai/replynodes-ai/skills/reddit-api)
- [ReplyNodes Reddit API base URL](https://api.replynodes.com/v1/reddit)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown instructions with curl examples, configuration guidance, and normalized JSON response shapes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only GET requests; priced routes require a ReplyNodes Bearer fetcher API key and return bounded normalized JSON.]

## Skill Version(s):

1.1.0 (source: SKILL.md frontmatter, VERSION, manifest.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
