## Description:

Find and verify work emails for prospects from a name and company — one call per lookup, and it never reads your inbox.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Outbound sales agents, lead enrichment workflows, and list-cleaning jobs use this skill to find a prospect's work email, verify an address before outreach, or list known addresses for a domain.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup details are sent to Superagnt and its data providers, and may include personal or professional contact information.

Mitigation: Share only the information needed for the lookup and ensure the data sharing is appropriate for your use case.

Risk: The API key grants access to the service, and bulk lookups can consume credits.

Mitigation: Protect the API key, approve only the intended MCP access, and check costs before running bulk lookups.

Risk: The documented curl examples and request schemas are incomplete for making production requests reliably.

Mitigation: Obtain corrected curl examples and complete request schemas, and confirm them against the service documentation before use.

## Reference(s):

- [Email Finder documentation](https://superagnt.com/r/ch-email-finder-docs)
- [Email Finder scoped MCP server](https://mcp.superagnt.com/mcp/email-finder)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Text]

**Output Format:** [JSON email lookup, verification, or domain-list results with deliverability status when provided]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the service response and available data.]

## Skill Version(s):

2.0.13 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
