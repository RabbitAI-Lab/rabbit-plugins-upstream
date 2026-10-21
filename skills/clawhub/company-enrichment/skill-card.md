## Description:

Enriches company domains with firmographics, technology stack, headcount, and account intelligence for agent-ready research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and research teams use this skill to enrich company records, find target accounts, and review company intelligence before outreach or market mapping.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queried domains, company lists, and search criteria are shared with Superagnt.

Mitigation: Only submit company data approved for sharing with Superagnt.

Risk: The Superagnt API key authenticates requests, and bulk enrichment or email lookup may consume credits.

Mitigation: Keep the key private and review Superagnt's data and billing terms before running large requests.

Risk: Email lookup may return contact data.

Mitigation: Review returned contact data before using or sharing it.

## Reference(s):

- [Company Enrichment documentation](https://superagnt.com/r/ch-company-enrichment-docs)
- [Company Enrichment MCP setup](https://mcp.superagnt.com/agent-setup/prompt.md)
- [ClawHub skill listing](https://clawhub.ai/superagnt/skills/company-enrichment)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [JSON API results and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include firmographics, funding, competitors, technology stack, and known domain emails.]

## Skill Version(s):

2.0.7 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
