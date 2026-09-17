## Description:

Company firmographics, tech stack, headcount, and intelligence from a domain — agent-ready account research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaencarrodine](https://clawhub.ai/user/jaencarrodine)

### License/Terms of Use:

MIT-0

## Use Case:

External business users, sales teams, marketing teams, and RevOps operators use this skill to enrich companies, research accounts, filter target lists, and map markets from domains or company names.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The recommended MCP setup can expose broader Superagnt platform tool families as the remote tool catalog changes.

Mitigation: Connect only the scoped company-enrichment server initially and review permissions before enabling additional tool families.

Risk: Company enrichment and domain email lookup may return personal or contact data.

Mitigation: Use results only for lawful, authorized business purposes and apply internal privacy and data-handling controls.

Risk: The skill requires a Superagnt API key or OAuth access for remote API and MCP calls.

Mitigation: Store credentials in approved secret storage, grant access only to intended workspaces, and rotate or revoke credentials when they are no longer needed.

## Reference(s):

- [Superagnt company enrichment documentation](https://superagnt.com/r/ch-company-enrichment-docs)
- [Company enrichment MCP server](https://mcp.superagnt.com/mcp/company-enrichment)
- [MCP client setup prompt](https://mcp.superagnt.com/agent-setup/prompt.md)
- [ClawHub skill listing](https://clawhub.ai/jaencarrodine/skills/company-enrichment)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with curl examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY or OAuth access; remote results may include company intelligence and contact data.]

## Skill Version(s):

2.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
