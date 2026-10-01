## Description:

Enrich people and companies from a name, domain, or LinkedIn URL — emails, titles, firmographics, and mobile numbers for agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, CRM-hygiene, and prospecting agents use this skill to enrich people and companies from names, domains, or LinkedIn URLs before outreach or data cleanup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lead and company lookup requests may include personal or business data such as names, LinkedIn URLs, emails, domains, and mobile-number lookups.

Mitigation: Use the skill only when sending that data to Superagnt is intended, authorized, and consistent with organizational privacy and consent requirements.

Risk: The skill requires a Superagnt API key for bearer-token authentication.

Mitigation: Provide SUPERAGNT_API_KEY through the environment, avoid exposing it in shared logs or prompts, and rotate the key if it is disclosed.

## Reference(s):

- [Superagnt Lead Enrichment Documentation](https://superagnt.com/r/ch-lead-enrichment-docs)
- [Lead Enrichment MCP Server](https://mcp.superagnt.com/mcp/lead-enrichment)
- [MCP Agent Setup Prompt](https://mcp.superagnt.com/agent-setup/prompt.md)
- [ClawHub Lead Enrichment Listing](https://clawhub.ai/superagnt/skills/lead-enrichment)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, API calls, JSON]

**Output Format:** [Markdown with curl examples, endpoint schemas, and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and curl; sends lead or company lookup data to Superagnt APIs.]

## Skill Version(s):

2.0.6 (source: SKILL.md frontmatter, evidence.release, artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
