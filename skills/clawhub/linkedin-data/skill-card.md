## Description:

Provides LinkedIn data lookups for company profiles, jobs, people, posts, and professional network insights using a superagnt API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, recruiting, and research agents use the skill to retrieve professional data for lead research, candidate context, company enrichment, and hiring or market insights.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup terms and API authentication are sent to superagnt, and requests consume credits.

Mitigation: Store the API key securely and submit only lookup terms you are comfortable sharing with the provider; monitor credit use.

Risk: The optional MCP connection's live behavior and the provider's data retention were not verified.

Mitigation: Review requested permissions and the provider's retention terms before approving the connection.

## Reference(s):

- [LinkedIn Data documentation](https://superagnt.com/r/ch-linkedin-data-docs)
- [LinkedIn Data API](https://api.superagnt.com/v1/data/linkedin)
- [LinkedIn Data MCP server](https://mcp.superagnt.com/mcp/linkedin)
- [superagnt API key setup](https://superagnt.com/r/ch-linkedin-data-key)
- [LinkedIn Data ClawHub listing](https://clawhub.ai/superagnt/skills/linkedin-data)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured JSON lookup results with text guidance for requesting LinkedIn data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returned fields vary by lookup and endpoint.]

## Skill Version(s):

2.0.13 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
