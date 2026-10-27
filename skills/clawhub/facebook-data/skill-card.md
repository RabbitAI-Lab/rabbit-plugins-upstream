## Description:

Facebook pages, posts, and group data for agents — brand and market research without scraping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, research teams, and marketing teams use this skill to query Facebook pages, posts, groups, ads, and marketplace listings for social listening, market research, and creator intelligence. Agents can use the documented API calls to retrieve structured results for analysis and downstream workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the API key and research queries to Superagnt, and calls may consume paid credits.

Mitigation: Protect the API key, limit requests to the intended research, and check the account's credit balance.

Risk: People-search and seller-lookup calls can return information about individuals or marketplace sellers.

Mitigation: Review these capabilities before enabling them and use returned information only for an appropriate research purpose.

Risk: Some documented curl examples are malformed and may fail when copied as written.

Mitigation: Check and correct the command quoting before running an example.

## Reference(s):

- [Facebook Data documentation](https://superagnt.com/r/ch-facebook-data-docs)
- [Facebook Data MCP server](https://mcp.superagnt.com/mcp/facebook)
- [MCP client setup](https://www.superagnt.com/install?facet=facebook)
- [Facebook Data API](https://api.superagnt.com/v1/data/facebook)
- [API key and account access](https://superagnt.com/r/ch-facebook-data-key)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/facebook-data)

## Skill Output:

**Output Type(s):** [API calls, JSON data, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with endpoint descriptions, JSON parameter schemas, and inline shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API responses are structured JSON; requests require a Superagnt API key and may use paid credits.]

## Skill Version(s):

2.0.8 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
