## Description:

Reddit posts, comments, and subreddit data for agents - community research and sentiment as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, research teams, marketing teams, and data teams use this skill to query Reddit posts, comments, users, subreddit metadata, and search results for social listening, creator intelligence, product research, alerts, digests, and analytics workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Reddit search terms, usernames, subreddit names, post URLs, and the user's Superagnt API key to Superagnt's service.

Mitigation: Use only when external processing by Superagnt is approved, avoid sensitive or regulated research targets unless permitted, and keep the API key in the SUPERAGNT_API_KEY environment variable.

Risk: Optional MCP setup uses OAuth or bearer-token authorization with a third-party service.

Mitigation: Review the OAuth consent screen and authorization scope before connecting the MCP server.

## Reference(s):

- [Reddit Data Documentation](https://superagnt.com/r/ch-reddit-data-docs)
- [Reddit Data MCP Server](https://mcp.superagnt.com/mcp/reddit)
- [MCP Agent Setup](https://mcp.superagnt.com/agent-setup/prompt.md)
- [Superagnt API Key Dashboard](https://superagnt.com/r/ch-reddit-data-key)
- [Reddit Data Listing](https://clawhub.ai/superagnt/skills/reddit-data)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, json]

**Output Format:** [Markdown guidance with curl commands and JSON API schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and curl; API responses are structured JSON from Superagnt's Reddit data endpoints.]

## Skill Version(s):

2.0.6 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
