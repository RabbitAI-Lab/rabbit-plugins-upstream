## Description:

Company firmographics, tech stack, headcount, and intelligence from a domain — agent-ready account research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, account research, and market intelligence teams can use the skill to enrich company names or domains with firmographics, headcount, funding, competitors, and technology information. It also supports company discovery, search, bulk enrichment, and domain email lookups before outreach or ICP analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company queries and submitted account lists are sent to superagnt and may consume credits.

Mitigation: Submit only data you are authorized to share and check credit usage before bulk requests.

Risk: The API key grants access to the service account.

Mitigation: Keep SUPERAGNT_API_KEY private and avoid exposing it in logs or shared output.

Risk: Optional MCP connections may request permissions, and malformed request parameters can produce incorrect results.

Mitigation: Review requested MCP permissions and check request parameters before running examples.

## Reference(s):

- [Company Enrichment documentation](https://superagnt.com/r/ch-company-enrichment-docs)
- [Company Enrichment MCP server](https://mcp.superagnt.com/mcp/company-enrichment)
- [MCP installation guide](https://www.superagnt.com/install?facet=company-enrichment)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/company-enrichment)

## Skill Output:

**Output Type(s):** [Company intelligence, JSON, Shell commands, Configuration instructions]

**Output Format:** [Structured JSON company data with Markdown guidance and inline curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Company search and enrichment requests may use API credits]

## Skill Version(s):

2.0.10 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
