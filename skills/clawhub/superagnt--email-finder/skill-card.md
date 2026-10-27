## Description:

Find and verify work emails from a name and company — waterfall lookup across providers, one call for agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and outbound agents use this skill to find a person's professional email from their name and company, verify an address before sending, and list known addresses on a domain. It also supports list cleaning and lead enrichment workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional MCP connection may expose workspace tools beyond email lookup.

Mitigation: Inspect its enabled tools before approving the connection; use the documented REST endpoints for a narrower workflow.

Risk: Email lookups use an API key and may involve lookup costs and data sharing.

Mitigation: Keep the API key in secure configuration and review costs and data sharing before use.

Risk: The documented command examples contain incomplete or escaped request content.

Mitigation: Correct and review command quoting and request payloads before running them.

## Reference(s):

- [Email Finder documentation](https://superagnt.com/r/ch-email-finder-docs)
- [Scoped Email Finder MCP server](https://mcp.superagnt.com/mcp/email-finder)
- [MCP client installation instructions](https://www.superagnt.com/install?facet=email-finder)
- [superagnt API keys](https://superagnt.com/r/ch-email-finder-key)
- [Email Finder ClawHub listing](https://clawhub.ai/superagnt/skills/email-finder)

## Skill Output:

**Output Type(s):** [API Calls, Structured data, Shell commands]

**Output Format:** [JSON API responses with email addresses and deliverability status; curl commands for direct use]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

2.0.8 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
