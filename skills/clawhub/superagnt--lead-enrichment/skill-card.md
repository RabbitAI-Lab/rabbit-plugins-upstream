## Description:

Enrich people and companies from a name, domain, or LinkedIn URL — emails, titles, firmographics, and mobile numbers for agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Sales agents, CRM-hygiene agents, and prospecting workflows use this skill to find contact details and company firmographics for people and organizations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lead data sent for enrichment may be shared with Superagnt and its providers.

Mitigation: Submit only lead data you intend to share with those services.

Risk: Bulk enrichment requests can consume credits.

Mitigation: Check credit costs and balance before sending bulk requests.

Risk: The API key also supports other Superagnt services if exposed.

Mitigation: Keep the key private and provide it only through the intended environment variable.

Risk: Escaped command examples and incomplete request parameters may cause failed or unintended requests.

Mitigation: Correct the command quoting and obtain complete request parameters before execution.

## Reference(s):

- [Lead Enrichment documentation](https://superagnt.com/r/ch-lead-enrichment-docs)
- [Lead Enrichment MCP server](https://mcp.superagnt.com/mcp/lead-enrichment)
- [MCP client installation guide](https://www.superagnt.com/install?facet=lead-enrichment)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/lead-enrichment)

## Skill Output:

**Output Type(s):** [API Calls, JSON]

**Output Format:** [Structured JSON lead and company records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returned fields depend on the requested enrichment and available provider matches.]

## Skill Version(s):

2.0.8 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
