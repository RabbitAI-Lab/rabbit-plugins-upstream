## Description:

Enrich people and companies from a name, domain, or LinkedIn URL — emails, titles, firmographics, and mobile numbers for agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, prospecting, and CRM-hygiene agents use this skill to enrich person and company records from a name, domain, or LinkedIn URL before outreach or to fill gaps in a CRM.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lead lookup data is shared with Superagnt and its data providers.

Mitigation: Send only lead data you are authorized to share.

Risk: Bulk lookups can consume account credits.

Mitigation: Check credit costs before running bulk lookups.

Risk: The API key also supports other Superagnt services.

Mitigation: Protect the key and avoid exposing it in prompts, logs, or shared shell history.

Risk: The documented request schemas are incomplete and the curl examples need quoting corrections; the optional hosted MCP service was not independently verified.

Mitigation: Obtain the correct request schemas and fix the curl quoting before use; verify the MCP service and its setup before connecting.

## Reference(s):

- [Lead Enrichment documentation](https://superagnt.com/r/ch-lead-enrichment-docs)
- [Scoped Lead Enrichment MCP server](https://mcp.superagnt.com/mcp/lead-enrichment)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/lead-enrichment)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Text]

**Output Format:** [Structured JSON lead and company enrichment responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fields vary by endpoint and may include work email, title, seniority, location, mobile number, or company firmographics.]

## Skill Version(s):

2.0.12 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
