## Description:

Analyzes tender activity, top purchasers and frequent awards to summarize market trends and concentration in Chinese procurement data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement analysts and business users use this skill to search tender records, compare purchasers and suppliers, and summarize market activity by industry, geography or period.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts Zhiliaobiaoxun services using an API key and transmits package and source identity.

Mitigation: Review service data sharing before use and configure the API key only for accounts authorized to access the service.

Risk: Trial registration can collect device features and persist a local API credential.

Mitigation: Obtain informed consent before registration; configure ZLBX_API_KEY manually to avoid automatic registration.

Risk: The source contains hidden request and acknowledgement rules that may obscure actions from users.

Mitigation: Review the skill instructions before installation and disclose relevant account or request actions to users.

Risk: Contact lookups and broad company queries may expose sensitive contact data or consume paid credits.

Mitigation: Limit queries to a legitimate business need, respect masked contact details and confirm the scope of paid calls.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/liu-jiapeng/skills/trending-miner-huobiaowang)
- [Tender search API](artifact/references/api-search.md)
- [Company analysis API](artifact/references/api-company.md)
- [Market analysis API](artifact/references/api-market.md)
- [Business registry interpretation](artifact/references/api-registry.md)
- [Account API](artifact/references/api-account.md)
- [Automatic registration](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown text and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the available tender data and the user's API access.]

## Skill Version(s):

2.1.9 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
