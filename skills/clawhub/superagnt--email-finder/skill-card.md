## Description:

Find and verify work emails for prospects from a name and company — one call per lookup, and it never reads your inbox.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Outbound agents can find a prospect's work email from a name and company, verify an address before sending, and list known emails on a domain for enrichment or list cleaning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports a mismatch between the email-finding description and an account-credits operation. The documented workflow also sends a bearer API key to an external service.

Mitigation: Review the documented credits check and API endpoints before use. Provide SUPERAGNT_API_KEY only for the intended service and monitor the associated credit balance.

## Reference(s):

- [Email Finder documentation](https://superagnt.com/r/ch-email-finder-docs)
- [Scoped Email Finder MCP server](https://mcp.superagnt.com/mcp/email-finder)
- [MCP installation guide](https://www.superagnt.com/install?facet=email-finder)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/email-finder)

## Skill Output:

**Output Type(s):** [API calls, Shell commands, JSON]

**Output Format:** [HTTP requests and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Endpoint-specific request fields; email results may include deliverability status.]

## Skill Version(s):

2.0.18 (source: frontmatter; server-resolved release 2.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
