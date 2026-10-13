## Description:

Helps agents research Chinese medical-device and consumables procurement through tender searches, award prices, brand analysis, and buyer details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams, suppliers, and analysts use this skill to find Chinese tender and award records for medical devices and consumables, compare historical prices and brands, and identify purchasers. It also supports broader procurement, company, contact, market, and account queries.

### Deployment Geography for Use:

Global (data coverage focused on China)

## Known Risks and Mitigations:

Risk: The skill covers company, contact, market, and account queries beyond medical-device sourcing.

Mitigation: Limit queries to the user's requested procurement task and review additional data access before use.

Risk: Automatic registration may collect device features and create an API credential.

Mitigation: Prefer a user-provided, scoped API key; obtain explicit consent before any device-feature collection or registration.

Risk: Contact lookups and generated login links can expose sensitive information or grant access.

Mitigation: Respect masked contact data, avoid bulk extraction, and treat login links and account information as sensitive.

Risk: Some company and market queries consume paid account credits.

Mitigation: Confirm scope and potential charges before expanding or repeating queries.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/pkuycl/skills/medical-device-sourcing-yiliaoqixiezhaobiaowang)
- [Tender search API](references/api-search.md)
- [Company analysis API](references/api-company.md)
- [Company registry API](references/api-registry.md)
- [Market analysis API](references/api-market.md)
- [Account API](references/api-account.md)
- [Automatic registration procedure](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and result tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include award prices, product details, procurement parties, and market comparisons; availability depends on API results and account access.]

## Skill Version(s):

1.0.8 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
