## Description:

Helps users search procurement notices across China and analyze companies, suppliers, and bidding markets through the Caizhaowang data service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement analysts and business users search Chinese tender and award notices, examine company records and contacts, and compare purchasing and supplier trends.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The provider receives procurement queries and can return sensitive project contacts and account details.

Mitigation: Review requests for contact, balance, or recharge data; avoid bulk contact exports and do not reveal API credentials.

Risk: Without a configured API key, registration can collect device characteristics including a hashed MAC address and save a new credential locally.

Mitigation: Set ZLBX_API_KEY yourself to avoid registration, or require informed consent before collecting device characteristics or creating an account.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/pkuycl/skills/national-procurement-data-center-caizhaowang)
- [Skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Procurement search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Registration flow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language responses with procurement results, company profiles, and market summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on provider data and available account credits; contact details may be masked.]

## Skill Version(s):

1.0.8 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
