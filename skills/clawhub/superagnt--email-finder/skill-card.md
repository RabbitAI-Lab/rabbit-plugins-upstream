## Description:

Find and verify professional email addresses by name and company, or list known addresses for a company domain.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and outreach teams, list-cleaning agents, and developers use this skill to find work email addresses, check deliverability before sending, and enrich lead records through superagnt's email lookup API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prospect names, company domains, and email addresses are sent to superagnt and its server-side providers.

Mitigation: Confirm organizational approval before sharing contact data with these services.

Risk: Exposure of the SUPERAGNT_API_KEY could permit unauthorized API use.

Mitigation: Keep the API key in a protected environment variable and do not include it in shared output.

## Reference(s):

- [Email Finder documentation](https://superagnt.com/r/ch-email-finder-docs)
- [MCP client setup](https://mcp.superagnt.com/agent-setup/prompt.md)
- [ClawHub skill listing](https://clawhub.ai/superagnt/skills/email-finder)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON API responses or text summaries of email lookup and verification results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may contain professional email addresses and deliverability status.]

## Skill Version(s):

2.0.7 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
