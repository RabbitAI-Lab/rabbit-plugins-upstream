## Description:

Enrich people and companies from a name, domain, or LinkedIn URL — emails, titles, firmographics, and mobile numbers for agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and prospecting agents can enrich people and companies from a name, domain, or LinkedIn URL before outreach. CRM hygiene and prospecting workflows can use the returned contact details and firmographics to fill record gaps or process lead lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lead details are sent to SuperAGNT and its upstream providers, whose permissions and data-retention practices are unverified.

Mitigation: Send only lead details you intend to share, and confirm the service's permissions and retention practices before use.

Risk: The API key can authorize requests and bulk lookups can consume credits.

Mitigation: Protect SUPERAGNT_API_KEY and monitor or limit bulk requests and credit use.

Risk: The documented request schemas are incomplete and some shell examples need correction before use.

Mitigation: Obtain complete request schemas and review and correct the shell examples before running them.

## Reference(s):

- [Lead Enrichment documentation](https://superagnt.com/r/ch-lead-enrichment-docs)
- [Scoped Lead Enrichment MCP server](https://mcp.superagnt.com/mcp/lead-enrichment)
- [Client installation guide](https://www.superagnt.com/install?facet=lead-enrichment)
- [SuperAGNT API key setup](https://superagnt.com/r/ch-lead-enrichment-key)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/lead-enrichment)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [JSON enrichment responses with Markdown setup and API guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses depend on the supplied lead details and available provider data; bulk endpoints can process lists.]

## Skill Version(s):

2.0.13 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
