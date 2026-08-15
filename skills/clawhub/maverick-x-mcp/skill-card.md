## Description:

Read and work with X posts, users, and search through X's hosted MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maverick](https://clawhub.ai/user/maverick)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research X posts, users, and search results, and to perform explicitly confirmed X write actions through the hosted MCP integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confirmed write actions can publish, delete, like, repost, follow, or otherwise change externally visible X account state.

Mitigation: Require explicit confirmation of the exact final content or destructive action immediately before any write.

Risk: The skill depends on OAuth tokens and refresh behavior for an X account.

Mitigation: Do not print or pass credential values as tool arguments; reconnect X if authentication fails after a refresh attempt.

Risk: Available tools, arguments, grants, and provider limits can vary by authenticated catalog and X entitlement.

Mitigation: Discover the live authenticated catalog before tool selection and honor provider rate-limit or usage-cap responses without blind retries.

## Reference(s):

- [X MCP documentation](https://docs.x.com/tools/mcp)
- [X OAuth 2.0 Authorization Code + PKCE](https://docs.x.com/fundamentals/authentication/oauth-2-0/user-access-token)
- [X API errors and rate limits](https://docs.x.com/x-api/fundamentals/response-codes-and-errors)
- [mcporter configuration](https://github.com/openclaw/mcporter/blob/v0.11.1/docs/config.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON tool-call output from mcporter]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent discovers the live authenticated X MCP catalog before choosing tools and obtains explicit user confirmation before externally visible write actions.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
