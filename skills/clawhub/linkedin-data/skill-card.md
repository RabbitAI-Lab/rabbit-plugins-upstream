## Description:

LinkedIn API integration with a single superagnt API key (Bearer token). Fetch company profiles, jobs, people, posts, and professional network insights. Use this skill when users want LinkedIn data for sales, recruiting, or enrichment. For other social data platforms, use the social-data skill (https://clawhub.ai/superagnt/skills/social-data).

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can retrieve LinkedIn company, profile, job, and post data for sales research, recruiting, contact enrichment, and market intelligence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the service requires providing an API key to an external service.

Mitigation: Only configure a key for a service you trust, keep it in the designated environment variable, and avoid exposing it in prompts or logs.

## Reference(s):

- [LinkedIn Data documentation](https://superagnt.com/r/ch-linkedin-data-docs)
- [LinkedIn Data MCP server](https://mcp.superagnt.com/mcp/linkedin)
- [superagnt API key](https://superagnt.com/r/ch-linkedin-data-key)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/linkedin-data)

## Skill Output:

**Output Type(s):** [JSON, Text, Markdown, Guidance]

**Output Format:** [Structured JSON data from the LinkedIn Data API, with text or Markdown summaries when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a SUPERAGNT_API_KEY; available results depend on API access and account credits.]

## Skill Version(s):

2.0.17 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
