## Description:

Find and verify work emails from a name and company — waterfall lookup across providers, one call for agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and outbound teams use the skill to find a person's work email, verify an address before sending, or list known addresses for a company domain.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup information is shared with superagnt and its downstream providers, and API calls use credits.

Mitigation: Send only information intended for that sharing and account for credit usage.

Risk: The request examples are incomplete, and remote service behavior and optional MCP authorization scopes have not been verified.

Mitigation: Confirm the full request schemas and review MCP authorization scopes before use; keep SUPERAGNT_API_KEY private.

## Reference(s):

- [Email Finder documentation](https://superagnt.com/r/ch-email-finder-docs)
- [Email Finder MCP server](https://mcp.superagnt.com/mcp/email-finder)
- [MCP client installation](https://www.superagnt.com/install?facet=email-finder)
- [API key setup](https://superagnt.com/r/ch-email-finder-key)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/email-finder)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration instructions]

**Output Format:** [Markdown instructions with curl examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lookup responses can include email deliverability status.]

## Skill Version(s):

2.0.12 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
