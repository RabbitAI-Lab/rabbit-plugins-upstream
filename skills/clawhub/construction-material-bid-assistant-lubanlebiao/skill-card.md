## Description:

Helps users research Chinese construction-material procurement, including historical unit prices, leading brands and suppliers, tender notices, and company information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thuanlynham-stack](https://clawhub.ai/user/thuanlynham-stack)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams, suppliers, and analysts use this skill to find Chinese construction-material tenders, compare historical awarded prices and brands, and investigate purchasers, suppliers, and companies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time registration can transmit hashed device characteristics to the service.

Mitigation: Obtain explicit consent before registration; users can provide their own API key instead.

Risk: The skill stores and uses an API key and may incur account credits for data queries.

Mitigation: Protect the locally stored key, avoid exposing it in responses, and confirm the scope of credit-consuming queries.

Risk: The service exposes broader procurement, company, and contact information than material pricing alone.

Mitigation: Limit queries to the user's request, preserve contact masking, and avoid bulk exporting contact details.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/thuanlynham-stack/skills/construction-material-bid-assistant-lubanlebiao)
- [Skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Market analysis API reference](references/api-market.md)
- [Company analysis API reference](references/api-company.md)
- [Registration and API key guidance](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include tender prices, company details, and account-dependent masked contact information.]

## Skill Version(s):

1.0.10 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
