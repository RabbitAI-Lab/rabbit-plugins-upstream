## Description:

全国采招大数据中心-采招网 helps agents search Chinese procurement notices, analyze companies, inspect market activity, and check account usage through documented REST APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business analysts use this skill to find procurement opportunities, review bid timelines, analyze company bidding profiles, compare competitors, and summarize market trends from the Caizhaowang data service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initiate provider account creation after consent and send a hashed device identifier for trial deduplication.

Mitigation: Prefer manually setting ZLBX_API_KEY; if auto-registration is used, confirm the consent prompt and provider terms before continuing.

Risk: The skill may store the service API key in ~/.zlbx/config.json.

Mitigation: Protect the local configuration file, avoid sharing logs that expose account details, and rotate the key if the workstation is shared or compromised.

Risk: Vendor notices, referral links, and recharge flows are supplied by the third-party provider.

Mitigation: Treat provider links and notices as vendor-supplied content and review them before purchase or account actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pkuycl/skills/national-procurement-data-center-caizhaowang)
- [Bid search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Auto-registration flow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Shell commands, Configuration]

**Output Format:** [Markdown answers with API request examples and structured result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-based auto-registration before paid data APIs can be used.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
