## Description:

Enrich people and companies from a name, domain, or LinkedIn URL - emails, titles, firmographics, and mobile numbers for agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaencarrodine](https://clawhub.ai/user/jaencarrodine)

### License/Terms of Use:

MIT-0

## Use Case:

External sales, prospecting, and CRM operations teams use this skill to enrich lead and company records, search for people, find professional emails, and fill missing contact or firmographic data through Superagnt APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Superagnt as a third-party processor for lead and contact enrichment, including personal data such as emails, titles, locations, and mobile numbers.

Mitigation: Install only when authorized to submit and receive this data, and confirm that the intended data processing complies with applicable organizational and legal requirements.

Risk: The same Superagnt credential may expose broader platform tool families beyond contact enrichment.

Mitigation: Prefer a scoped MCP connection or a credential limited to enrichment when available, and review any prompt or UI that enables additional Superagnt tool families before approving it.

## Reference(s):

- [Superagnt Lead Enrichment Documentation](https://superagnt.com/r/ch-lead-enrichment-docs)
- [Superagnt Lead Enrichment MCP Server](https://mcp.superagnt.com/mcp/lead-enrichment)
- [ClawHub Skill Listing](https://clawhub.ai/jaencarrodine/skills/lead-enrichment)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON API request guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and curl for direct API use; MCP-capable clients can connect to the scoped MCP server.]

## Skill Version(s):

2.0.5 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
