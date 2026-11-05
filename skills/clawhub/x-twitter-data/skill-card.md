## Description:

X posts, profiles, followers, and search for agents — audience research and social listening as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and research or marketing teams use this skill to retrieve X posts, profiles, followers, search results, and hashtag activity for social listening and audience research. The results are returned as structured JSON for agent workflows and analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API key also works with other Superagnt services, so exposure may grant broader account access.

Mitigation: Store the key in the environment and protect it as a credential; avoid placing it in prompts, logs, or shared files.

Risk: Queries and submitted analysis text are sent to Superagnt, and requests may incur charges.

Mitigation: Avoid sending sensitive text and review the request and credit costs before running larger queries.

Risk: The packaged shell examples have quoting that should be corrected before use; the optional MCP setup requests OAuth permissions.

Mitigation: Review and correct shell quoting before execution, and inspect the requested OAuth permissions before approving MCP access.

## Reference(s):

- [X (Twitter) Data documentation](https://superagnt.com/r/ch-x-twitter-data-docs)
- [Scoped X MCP server](https://mcp.superagnt.com/mcp/x)
- [MCP client installation guide](https://www.superagnt.com/install?facet=x)

## Skill Output:

**Output Type(s):** [JSON, Analysis]

**Output Format:** [Structured JSON from X data and analysis endpoints]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Endpoint results vary by query, account or post, filters, and pagination.]

## Skill Version(s):

2.0.13 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
