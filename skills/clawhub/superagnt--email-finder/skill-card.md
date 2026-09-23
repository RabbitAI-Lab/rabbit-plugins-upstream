## Description:

Find and verify work emails from a name and company - waterfall lookup across providers, one call for agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

External teams and agents use this skill to find a person's professional email, verify an address before outreach, or list known addresses for a company domain. It is intended for authorized business-contact enrichment, outbound workflows, and list-cleaning tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can return work-email data, which should be treated as personal data.

Mitigation: Use the skill only for lawful, authorized business-contact workflows and apply applicable privacy and anti-spam requirements.

Risk: The skill sends lookup inputs and an API key to Superagnt services.

Mitigation: Install and run it only after confirming that the user trusts Superagnt with the API key and lookup inputs.

Risk: Bulk collection or outreach can create compliance risk.

Mitigation: Avoid bulk collection or outreach unless there is an appropriate basis and the workflow complies with relevant rules.

## Reference(s):

- [Superagnt Email Finder Documentation](https://superagnt.com/r/ch-email-finder-docs)
- [Email Finder MCP Server](https://mcp.superagnt.com/mcp/email-finder)
- [MCP Agent Setup](https://mcp.superagnt.com/agent-setup/prompt.md)
- [ClawHub Email Finder Listing](https://clawhub.ai/superagnt/skills/email-finder)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with curl examples and JSON API request schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and curl; API responses may contain work-email data and deliverability status.]

## Skill Version(s):

2.0.6 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
