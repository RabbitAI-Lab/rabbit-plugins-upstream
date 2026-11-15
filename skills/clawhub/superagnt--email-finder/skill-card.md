## Description:

Find and verify work emails for prospects from a name and company — one call per lookup, and it never reads your inbox.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and outbound agents use this skill to find a prospect’s work email, verify an address before outreach, or list addresses associated with a domain. It can also support list-cleaning and lead-enrichment workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installation check requests a credit balance, which differs from the stated email-finding purpose.

Mitigation: Before installing, confirm that the skill’s actual function and API requests match the intended use and understand how the API key and submitted data may be used.

Risk: Email lookup and domain listing send prospect or domain information to an external API.

Mitigation: Submit only the business contact information needed for the requested operation and review the provider’s data handling terms.

## Reference(s):

- [Email Finder documentation](https://superagnt.com/r/ch-email-finder-docs)
- [API key setup](https://superagnt.com/r/ch-email-finder-key)
- [Email Finder MCP server](https://mcp.superagnt.com/mcp/email-finder)
- [Client installation instructions](https://www.superagnt.com/install?facet=email-finder)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/email-finder)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Guidance]

**Output Format:** [JSON API responses with Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns results for email lookup, verification, or domain address listing; lookup results may include deliverability status.]

## Skill Version(s):

2.0.14 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
