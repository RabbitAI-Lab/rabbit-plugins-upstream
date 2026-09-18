## Description:

X posts, profiles, followers, and search for agents, supporting audience research and social listening as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaencarrodine](https://clawhub.ai/user/jaencarrodine)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, research teams, marketing teams, and data teams use this skill to retrieve X/Twitter posts, profiles, followers, search results, hashtags, trends, and related analysis outputs for social listening, audience research, alerts, digests, and dashboards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, handles, tweet IDs, and submitted text are sent to Superagnt for processing.

Mitigation: Use the skill only for data that is appropriate to share with Superagnt, and avoid sending secrets or sensitive private text.

Risk: The security summary notes that the skill points agents toward broader third-party tools and arbitrary text processing beyond the narrow X/Twitter data description.

Mitigation: Prefer the scoped X-only use case, and review MCP tool-family enablement before allowing broader platform access such as files, databases, webhooks, or queues.

## Reference(s):

- [Superagnt X Data Documentation](https://superagnt.com/r/ch-x-twitter-data-docs)
- [Superagnt X MCP Server](https://mcp.superagnt.com/mcp/x)
- [MCP Agent Setup Prompt](https://mcp.superagnt.com/agent-setup/prompt.md)
- [ClawHub Skill Listing](https://clawhub.ai/jaencarrodine/skills/x-twitter-data)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with curl examples and structured JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and curl for direct API calls; MCP-capable clients can connect to the scoped X server.]

## Skill Version(s):

2.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
