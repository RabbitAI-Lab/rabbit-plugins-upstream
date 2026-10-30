## Description:

Enrich people and companies from a name, domain, or LinkedIn URL — emails, titles, firmographics, and mobile numbers for agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and prospecting agents use this skill to find professional contact details and company information before outreach. CRM hygiene agents can use it to fill gaps in person and company records, including processing lists in bulk.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup data is shared with Superagnt and its upstream providers.

Mitigation: Send only records approved for this service and review the provider's data documentation.

Risk: Bulk requests can consume API credits.

Mitigation: Choose the records to process and set a spending limit before running bulk requests.

Risk: An exposed API key could authorize requests against the account.

Mitigation: Keep the API key in secret storage.

Risk: The bundled examples may need correction.

Mitigation: Check the provider documentation and confirm request parameters before using an example.

## Reference(s):

- [Lead enrichment documentation](https://superagnt.com/r/ch-lead-enrichment-docs)
- [Provider data documentation, parameters, and cost controls](https://www.superagnt.com/docs/data/people-and-companies)
- [Scoped Lead Enrichment MCP server](https://mcp.superagnt.com/mcp/lead-enrichment)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/lead-enrichment)

## Skill Output:

**Output Type(s):** [Structured data, API calls, Shell commands, Configuration instructions]

**Output Format:** [JSON lead records; Markdown instructions with curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Person and company enrichment results, including contact details and firmographics; bulk operations are supported.]

## Skill Version(s):

2.0.11 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
