## Description:

Facebook pages, posts, groups, Marketplace listings, and the Ad Library for agents — no Facebook app, review, or login of yours.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and research or marketing teams can use agents to retrieve Facebook page and group content, posts, videos, Marketplace listings, people-search results, and Ad Library data for monitoring, research, and downstream analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: People-search results may include personal information, and the security guidance flags this capability for deliberate review.

Mitigation: Use people search only for a clear, authorized purpose, and limit queries and retained results to what that purpose requires.

Risk: The security guidance identifies a credit-check request as the least clearly related capability.

Mitigation: Confirm that any such request is relevant to the task and within the documented API scope before using it.

## Reference(s):

- [Facebook Data documentation](https://superagnt.com/r/ch-facebook-data-docs)
- [Scoped Facebook MCP server](https://mcp.superagnt.com/mcp/facebook)
- [Superagnt API key setup](https://superagnt.com/r/ch-facebook-data-key)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/facebook-data)

## Skill Output:

**Output Type(s):** [JSON]

**Output Format:** [Structured JSON data retrieved from documented Facebook endpoints]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live results depend on the selected Facebook data source, query filters, pagination, and API access.]

## Skill Version(s):

2.0.18 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
