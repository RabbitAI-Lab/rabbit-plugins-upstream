## Description:

Searches Chinese tender and award listings using combined keywords, exclusions, location, date, and amount filters, and summarizes relevant results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams, suppliers, and market researchers use this skill to find Chinese tender opportunities, examine company bidding activity, and compare purchasing and award trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external provider handles tender searches and company or market queries.

Mitigation: Use only if the provider's access to these queries is acceptable; avoid sensitive search terms.

Risk: Optional registration collects a MAC-derived device identifier and saves an API key locally.

Mitigation: Prefer a personally supplied API key through a trusted secret mechanism; consent before using registration.

Risk: Contact lookups and account or recharge features can expose business contact data or incur charges.

Mitigation: Use contact and recharge flows only when intended, and review the scope of paid queries.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/pkuycl/skills/massive-tender-smart-search-biao800)
- [Provider skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Tender search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Business registry API reference](artifact/references/api-registry.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Optional registration procedure](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and linked result tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [States search filters and displays reported amounts with units.]

## Skill Version(s):

1.0.8 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
