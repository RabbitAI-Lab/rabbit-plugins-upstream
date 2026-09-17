## Description:

Reddit posts, comments, and subreddit data for agents — community research and sentiment as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaencarrodine](https://clawhub.ai/user/jaencarrodine)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, research teams, marketing teams, and product teams use this skill to configure Reddit data access for agents that search Reddit posts, comments, subreddit metadata, and user activity as structured JSON for community research, social listening, creator intelligence, alerts, digests, and dashboards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Reddit research queries and a Superagnt API key to Superagnt services.

Mitigation: Install only when that data sharing is acceptable, protect the API key, and review external setup instructions before use.

Risk: The related Superagnt platform can expose broader tool families beyond Reddit, including workspace files, databases, webhooks, queues, and enrichment tools.

Mitigation: Prefer a Reddit-only MCP configuration when available and do not enable broader Superagnt tool families unless that access is intentional.

## Reference(s):

- [Superagnt Reddit Data Documentation](https://superagnt.com/r/ch-reddit-data-docs)
- [Superagnt Reddit MCP Server](https://mcp.superagnt.com/mcp/reddit)
- [Superagnt Agent Setup](https://mcp.superagnt.com/agent-setup/prompt.md)
- [ClawHub Skill Listing](https://clawhub.ai/jaencarrodine/skills/reddit-data)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown with inline bash commands and JSON API schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and curl for the documented command-line flow.]

## Skill Version(s):

2.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
