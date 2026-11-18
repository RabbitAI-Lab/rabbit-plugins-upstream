## Description:

This skill uses a single superagnt API key to retrieve LinkedIn company, profile, job, post, and professional-network data for sales, recruiting, and enrichment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, recruiting, and market-intelligence agents use this skill to retrieve company, professional profile, job, post, and article data for account enrichment, candidate research, and market analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API requests may send query data and professional-network identifiers to an external service; the scan does not establish what data the service receives or how it handles it.

Mitigation: Review request contents and the provider's data-handling terms before sending sensitive or personal information, and keep SUPERAGNT_API_KEY out of prompts and logs.

## Reference(s):

- [LinkedIn Data API documentation](https://superagnt.com/r/ch-linkedin-data-docs)
- [LinkedIn Data API](https://api.superagnt.com/v1/data/linkedin)
- [LinkedIn Data MCP server](https://mcp.superagnt.com/mcp/linkedin)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [JSON API responses with concise agent-written summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fields and results vary by endpoint and available API data.]

## Skill Version(s):

2.0.15 (source: frontmatter, server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
