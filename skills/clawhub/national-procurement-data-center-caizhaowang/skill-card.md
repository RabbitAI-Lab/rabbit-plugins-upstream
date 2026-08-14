## Description:

全国采招大数据中心-采招网 helps agents search Chinese procurement notices, analyze company bidding activity, inspect market trends, and retrieve account usage information through the provider's API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to answer procurement, supplier, buyer, competitor, project-renewal, and market-price questions using Caizhaowang/Zhiliaobiaoxun data. It is most useful when a task needs cross-region bid search, company profiles, partner/contact lookup, or aggregate market analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: If no API key is configured, the skill may initiate an optional automatic trial signup that collects OS type, CPU architecture, and a hashed MAC-derived value, then sends them to the provider and stores an API key locally.

Mitigation: Configure ZLBX_API_KEY before use to avoid the automatic signup path, and approve the signup flow only when comfortable with the described device-feature collection.

Risk: Company contact lookup and group-wide company analysis can expose sensitive business or contact information returned by the provider.

Mitigation: Use the returned information only for the requested procurement analysis, avoid unnecessary broad queries, and do not ask users to share or reveal API keys.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pkuycl/skills/national-procurement-data-center-caizhaowang)
- [API overview](references/api-search.md)
- [Company analysis API](references/api-company.md)
- [Market analysis API](references/api-market.md)
- [Account API](references/api-account.md)
- [Automatic registration flow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with JSON request examples, shell commands, and API-derived analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or provider-managed local configuration for authenticated API access.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
