## Description:

X posts, profiles, followers, and search for agents — audience research and social listening as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and marketing teams use the skill to gather X posts, account details, follower information, search results, and hashtag data for social listening, audience research, and creator intelligence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and analysis text are sent to the third-party Superagnt service.

Mitigation: Use the skill only with queries and text you are comfortable sharing with Superagnt.

Risk: The API key can be exposed if mishandled, and requests may incur usage costs.

Mitigation: Protect SUPERAGNT_API_KEY and review usage and billing in the Superagnt app.

Risk: The documented shell examples contain quoting that should be corrected before execution.

Mitigation: Review and correct shell quoting before running the examples.

Risk: The optional MCP connection requires user authorization.

Mitigation: Approve the MCP connection only when you want to use it.

## Reference(s):

- [X (Twitter) Data documentation](https://superagnt.com/r/ch-x-twitter-data-docs)
- [Scoped X MCP server](https://mcp.superagnt.com/mcp/x)
- [MCP installation instructions](https://www.superagnt.com/install?facet=x)
- [Superagnt API keys](https://superagnt.com/r/ch-x-twitter-data-key)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/x-twitter-data)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Analysis]

**Output Format:** [Structured JSON data from X endpoints, with agent-readable research results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Endpoint-dependent records; paginated results may use continuation tokens.]

## Skill Version(s):

2.0.8 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
