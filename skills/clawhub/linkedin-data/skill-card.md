## Description:

LinkedIn API integration with a single superagnt API key (Bearer token). Fetch company profiles, jobs, people, posts, and professional network insights. Use this skill when users want LinkedIn data for sales, recruiting, or enrichment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, recruiting, and market research agents use this skill to retrieve LinkedIn company, people, jobs, post, and professional network data for enrichment and research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search identifiers and queries are sent to superagnt, and data requests consume credits.

Mitigation: Send only the identifiers and search terms needed, and check expected credit use before making requests.

Risk: The SUPERAGNT_API_KEY is a bearer credential.

Mitigation: Keep the API key private and out of prompts, logs, and shared command history.

Risk: An optional MCP connection may expose enabled LinkedIn data tools to the agent.

Mitigation: Review the enabled tools and approve only the LinkedIn access needed for the task.

## Reference(s):

- [LinkedIn Data documentation](https://superagnt.com/r/ch-linkedin-data-docs)
- [LinkedIn Data MCP server](https://mcp.superagnt.com/mcp/linkedin)
- [LinkedIn Data installation instructions](https://www.superagnt.com/install?facet=linkedin)
- [superagnt API key and credits](https://superagnt.com/r/ch-linkedin-data-key)

## Skill Output:

**Output Type(s):** [JSON data, Guidance]

**Output Format:** [Structured JSON API responses with Markdown setup and usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses cover LinkedIn company, people, jobs, posts, articles, and related professional data. Requests use the superagnt service and consume credits.]

## Skill Version(s):

2.0.8 (source: SKILL.md frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
