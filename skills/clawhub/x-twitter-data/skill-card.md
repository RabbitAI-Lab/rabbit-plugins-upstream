## Description:

X posts, profiles, followers, and search for agents -- audience research and social listening as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, marketing and research teams, product teams, and data teams use this skill to access X posts, user profiles, followers, likes, search, hashtag streams, trends, lists, and text-analysis helpers as structured JSON for agents, dashboards, alerts, digests, and analytics pipelines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends X accounts, tweet or list IDs, search terms, and submitted text to the third-party superagnt service.

Mitigation: Install and use it only when the user is comfortable with superagnt receiving that data, and avoid sending sensitive private text unless the user trusts superagnt's handling of it.

Risk: Authentication depends on a superagnt API credential.

Mitigation: Use the documented Bearer-token authentication and avoid alternate API-key header patterns unless the provider confirms they are supported.

## Reference(s):

- [superagnt X (Twitter) Data documentation](https://superagnt.com/r/ch-x-twitter-data-docs)
- [Scoped MCP server](https://mcp.superagnt.com/mcp/x)
- [MCP client setup prompt](https://mcp.superagnt.com/agent-setup/prompt.md)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/x-twitter-data)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown instructions with curl commands and structured JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and curl for the documented curl workflow; MCP-capable clients can use the scoped MCP endpoint.]

## Skill Version(s):

2.0.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
