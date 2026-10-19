## Description:

Searches Chinese procurement notices and company records to prepare sourced bid intelligence and market summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and market research teams use the skill to find Chinese tender and award notices, examine company bidding activity, and summarize purchasing trends and opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Without a configured API key, trial registration can send a hashed device identifier and device characteristics to an external service.

Mitigation: Request explicit consent before collecting device characteristics or registering; configure your own ZLBX_API_KEY to avoid this path.

Risk: Automatic registration stores the issued API key on the local device, and API requests transmit account credentials and package identity to the service.

Mitigation: Review the service and local credential-storage requirements before installation; protect the key and avoid sharing it in responses.

Risk: Some company-data queries consume account credits and historical records can be mistaken for current ownership.

Mitigation: Limit queries to the user's requested scope, check applicable credit costs, and label company records with their source and freshness.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/pkuycl/skills/authoritative-bid-policy-guide-yuanbowang)
- [Bid search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Company registry data guidance](references/api-registry.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Trial account registration guidance](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Markdown summaries and tables with links to source notices]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the external API and available account quota.]

## Skill Version(s):

1.0.10 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
