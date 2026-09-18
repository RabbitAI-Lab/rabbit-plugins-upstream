## Description:

Enrich people and companies from a name, domain, or LinkedIn URL with emails, titles, firmographics, and mobile numbers for agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaencarrodine](https://clawhub.ai/user/jaencarrodine)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, prospecting, and CRM-hygiene agents use this skill to enrich people and companies, find professional emails or mobile numbers, search for prospects, and fill lead records at scale.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The recommended MCP setup can expose broader Superagnt capabilities than the reviewed lead-enrichment API functions.

Mitigation: Use the direct lead-enrichment API path when only enrichment is needed, and grant OAuth or bearer access only after reviewing the broader tool surface.

Risk: The skill processes lead and company data, including professional emails and mobile numbers.

Mitigation: Provide only authorized lead or company data and apply the user's compliance requirements before enrichment or outreach use.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/jaencarrodine/skills/lead-enrichment)
- [Documentation](https://superagnt.com/r/ch-lead-enrichment-docs)
- [MCP server](https://mcp.superagnt.com/mcp/lead-enrichment)
- [Agent setup](https://mcp.superagnt.com/agent-setup/prompt.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON schemas and curl command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY for authenticated API access; API and MCP calls can return JSON lead and company enrichment records.]

## Skill Version(s):

2.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
