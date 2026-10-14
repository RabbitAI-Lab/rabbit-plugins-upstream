## Description:

Helps users research construction-material procurement bids, historical awarded prices, leading brands, and suppliers using Zhiliaobiaoxun data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thuanlynham-stack](https://clawhub.ai/user/thuanlynham-stack)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams and construction-material suppliers use this skill to find bid opportunities, compare awarded unit prices, and identify brands, suppliers, and relevant companies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts Zhiliaobiaoxun services with an API key and can check account status or use paid data queries.

Mitigation: Use a manually configured API key where preferred, authorize only needed queries, and monitor account usage.

Risk: Trial-account registration can use device-derived identifiers and store an API key locally.

Mitigation: Require consent before registration; configure ZLBX_API_KEY manually to avoid device-based registration and local key persistence.

Risk: Contact lookup and company intelligence can expose personal or commercially sensitive information.

Mitigation: Limit searches and sharing to authorized business purposes; avoid bulk contact exports or attempts to uncover masked details.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/thuanlynham-stack/skills/construction-material-bid-assistant-lubanlebiao)
- [Bid-search API reference](artifact/references/api-search.md)
- [Market-analysis API reference](artifact/references/api-market.md)
- [Company-analysis API reference](artifact/references/api-company.md)
- [Company-registry interpretation](artifact/references/api-registry.md)
- [Account API reference](artifact/references/api-account.md)
- [Trial-account registration and privacy](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include awarded prices, supplier lists, and procurement or company details.]

## Skill Version(s):

1.0.9 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
