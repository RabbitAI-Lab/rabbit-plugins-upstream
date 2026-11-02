## Description:

Connects to superagnt’s LinkedIn Data API to retrieve company, job, profile, post, and professional network information for sales, recruiting, or enrichment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, recruiting, and research agents use this skill to retrieve LinkedIn company, job, profile, post, and professional network data for enrichment and analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup parameters and the API credential are sent to superagnt, and requests can consume paid credits.

Mitigation: Protect the API key, review lookup parameters before sending them, and monitor credit use.

Risk: The API key also works with other superagnt services.

Mitigation: Store the key securely and limit lookups to information you intend to share.

## Reference(s):

- [LinkedIn Data API documentation](https://superagnt.com/r/ch-linkedin-data-docs)
- [LinkedIn Data MCP server](https://mcp.superagnt.com/mcp/linkedin)
- [MCP facet installation guide](https://www.superagnt.com/install?facet=linkedin)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured JSON data, with optional text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the requested LinkedIn data and API response.]

## Skill Version(s):

2.0.11 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
