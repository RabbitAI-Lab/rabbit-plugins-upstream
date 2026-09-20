## Description:

Reddit posts, comments, and subreddit data for agents -- community research and sentiment as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaencarrodine](https://clawhub.ai/user/jaencarrodine)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, research teams, and marketing teams use this skill to retrieve Reddit posts, comments, subreddit metadata, user activity, and search results for social listening, community research, sentiment analysis, alerts, digests, and dashboards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Reddit research targets and a Superagnt credential to Superagnt's hosted service.

Mitigation: Install only when that hosted-service data flow is acceptable, and keep SUPERAGNT_API_KEY scoped and protected.

Risk: The skill points agents toward broader Superagnt platform tool families beyond the Reddit data purpose.

Mitigation: Use the scoped Reddit endpoints for this release, and review or avoid broader MCP tool-enablement guidance unless those additional capabilities are intentionally needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/jaencarrodine/skills/reddit-data)
- [Superagnt Reddit Data documentation](https://superagnt.com/r/ch-reddit-data-docs)
- [Superagnt Reddit MCP server](https://mcp.superagnt.com/mcp/reddit)
- [Superagnt agent setup](https://mcp.superagnt.com/agent-setup/prompt.md)
- [Superagnt dashboard and API keys](https://superagnt.com/r/ch-reddit-data-key)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls, JSON]

**Output Format:** [Markdown guidance with curl examples and structured JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and curl for the documented HTTP flow; MCP-capable clients can connect to the scoped Reddit server.]

## Skill Version(s):

2.0.5 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
