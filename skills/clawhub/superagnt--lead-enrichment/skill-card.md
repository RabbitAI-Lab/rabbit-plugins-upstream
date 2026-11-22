## Description:

Enrich people and companies from a name, domain, or LinkedIn URL — emails, titles, firmographics, and mobile numbers for agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and prospecting agents can enrich person and company records from a name, domain, or LinkedIn URL. CRM hygiene workflows can use it to fill missing contact details and firmographic information, including for bulk lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Superagnt API key, and its setup check retrieves the account's credit balance.

Mitigation: Keep the API key in a secret store or protected environment variable, provide it only to trusted clients, and review the account's credit usage.

## Reference(s):

- [Lead Enrichment documentation](https://superagnt.com/r/ch-lead-enrichment-docs)
- [Scoped Lead Enrichment MCP server](https://mcp.superagnt.com/mcp/lead-enrichment)
- [MCP client installation guide](https://www.superagnt.com/install?facet=lead-enrichment)
- [Superagnt app and API keys](https://superagnt.com/r/ch-lead-enrichment-key)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/lead-enrichment)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Guidance]

**Output Format:** [JSON API responses and Markdown setup and usage instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY for API access.]

## Skill Version(s):

2.0.18 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
