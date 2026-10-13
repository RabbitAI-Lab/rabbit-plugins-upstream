## Description:

Helps users search and analyze Chinese bidding notices, suppliers, companies, pricing, and procurement trends through the 知了标讯 data service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and bidding professionals use this skill to find tender opportunities, investigate companies and potential suppliers, and assess competitors, prices, and market trends in Chinese procurement data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bidding queries are sent to a third-party data provider.

Mitigation: Use the service only when comfortable sharing the query with that provider; avoid submitting sensitive details unnecessarily.

Risk: Without an existing API key, trial registration can transmit a hashed device identifier and create an account.

Mitigation: Require explicit opt-in before collecting device details or registering; configure ZLBX_API_KEY manually to bypass registration.

Risk: Auto-registration stores an API key locally and can generate login and recharge links.

Mitigation: Protect the local key, avoid sharing login links, and review the recharge flow before using trial credentials.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/liu-jiapeng/skills/zlbx-bidding-skill)
- [知了标讯 skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Bidding search API reference](references/api-search.md)
- [Automatic registration and account guidance](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and linked result tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include bidding notice links, company and market analysis, and account guidance.]

## Skill Version(s):

1.4.7 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
