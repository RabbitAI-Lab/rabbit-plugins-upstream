## Description:

X posts, profiles, followers, and search for agents \u2014 audience research and social listening as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaencarrodine](https://clawhub.ai/user/jaencarrodine)

### License/Terms of Use:

MIT-0

## Use Case:

External teams, developers, and agents use this skill to retrieve X posts, profiles, followers, search results, trends, and related analysis data for audience research, social listening, alerts, digests, and dashboards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends X research data and submitted text to Superagnt.

Mitigation: Install it only when that data sharing is intended, and avoid submitting sensitive text unless approved for the use case.

Risk: The Superagnt API key grants access to paid data services.

Mitigation: Keep SUPERAGNT_API_KEY private, use the scoped X connector where possible, and rotate the key if it is exposed.

Risk: The instructions can expand beyond X into broader Superagnt MCP tool families.

Mitigation: Do not enable workspace files, databases, webhooks, queues, or other broader tool families unless they are explicitly needed and reviewed.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/jaencarrodine/skills/x-twitter-data)
- [Superagnt X data documentation](https://superagnt.com/r/ch-x-twitter-data-docs)
- [Superagnt X MCP server](https://mcp.superagnt.com/mcp/x)
- [Superagnt agent setup prompt](https://mcp.superagnt.com/agent-setup/prompt.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls]

**Output Format:** [Markdown with endpoint tables, JSON schemas, and bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and curl; API responses are structured JSON from Superagnt.]

## Skill Version(s):

2.0.5 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
