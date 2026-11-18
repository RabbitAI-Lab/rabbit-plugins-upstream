## Description:

X posts, profiles, followers, and search for agents — audience research and social listening as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and marketing or product teams can use the skill to retrieve X posts, profiles, followers, and search results for audience research, social listening, and analytics workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends authenticated requests to an external Superagnt service, and its setup check reports account credit status.

Mitigation: Use the service only for queries you intend to send, keep SUPERAGNT_API_KEY private, and check the account's credit balance before use.

## Reference(s):

- [X (Twitter) Data documentation](https://superagnt.com/r/ch-x-twitter-data-docs)
- [Scoped X MCP server](https://mcp.superagnt.com/mcp/x)
- [X facet installation guide](https://www.superagnt.com/install?facet=x)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/x-twitter-data)

## Skill Output:

**Output Type(s):** [JSON, Guidance, Shell commands, Configuration]

**Output Format:** [Structured JSON API responses; Markdown instructions with curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the requested endpoint and query; paginated results may require continuation tokens.]

## Skill Version(s):

2.0.15 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
