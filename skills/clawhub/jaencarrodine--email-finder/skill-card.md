## Description:

Find and verify work emails from a name and company - waterfall lookup across providers, one call for agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaencarrodine](https://clawhub.ai/user/jaencarrodine)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and outbound automation agents use this skill to find professional email addresses, verify deliverability before sending, and list known addresses for a company domain.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A remotely changeable MCP setup can expose broader Superagnt platform tools beyond email finding.

Mitigation: Use only the email-specific curl endpoints or an email-only MCP configuration unless broader Superagnt tool families are intentionally enabled.

Risk: Email lookup and verification requests send contact data and credentials to Superagnt and its providers.

Mitigation: Confirm what contact data and credentials will be sent before installation or use.

## Reference(s):

- [Documentation](https://superagnt.com/r/ch-email-finder-docs)
- [Email Finder MCP server](https://mcp.superagnt.com/mcp/email-finder)
- [Agent setup prompt](https://mcp.superagnt.com/agent-setup/prompt.md)
- [Dashboard and API keys](https://superagnt.com/r/ch-email-finder-key)
- [ClawHub listing](https://clawhub.ai/jaencarrodine/skills/email-finder)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and curl for direct API usage; MCP clients may use the hosted Email Finder MCP server.]

## Skill Version(s):

2.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
