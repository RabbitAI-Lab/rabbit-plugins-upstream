## Description:

Enrich people and companies from a name, domain, or LinkedIn URL — emails, titles, firmographics, and mobile numbers for agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and prospecting agents can enrich a person or company record before outreach, while CRM hygiene agents can fill gaps in existing records. Developers can also use the documented endpoints to build lead research workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Enrichment requests send the selected person or company information to an external API and use an API key.

Mitigation: Consider what information you choose to send, and keep SUPERAGNT_API_KEY private.

## Reference(s):

- [Lead Enrichment documentation](https://superagnt.com/r/ch-lead-enrichment-docs)
- [Lead Enrichment MCP server](https://mcp.superagnt.com/mcp/lead-enrichment)
- [MCP client setup](https://www.superagnt.com/install?facet=lead-enrichment)
- [Lead Enrichment API](https://api.superagnt.com/v1/data/agnt)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown instructions with curl examples; API responses are JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requests use the SUPERAGNT_API_KEY bearer credential.]

## Skill Version(s):

2.0.15 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
