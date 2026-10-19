## Description:

Helps source medical devices and consumables using Chinese tender and award records, including historical prices, brands, buyers, and product details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams and suppliers use this skill to find medical-device tenders, compare awarded prices and brands, and identify purchasing organizations. Its connected service also supports broader tender, market, and company research.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The service requires an API key and may store a newly issued key locally.

Mitigation: Use your own configured ZLBX_API_KEY when possible, protect stored credentials, and monitor account and quota usage.

Risk: Optional trial-account registration sends device characteristics to the service.

Mitigation: Review and consent to registration before sharing device characteristics, or configure an existing API key to skip it.

Risk: Account and update checks may occur alongside data queries, and the connector covers more than medical-device sourcing.

Mitigation: Review service interactions and authorize only the tender, company, and market queries needed for the task.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pkuycl/skills/medical-device-sourcing-yiliaoqixiezhaobiaowang)
- [Service skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Tender search API reference](artifact/references/api-search.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account and registration reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Markdown with tender summaries, tables, and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the service's available records and API quota.]

## Skill Version(s):

1.0.10 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
