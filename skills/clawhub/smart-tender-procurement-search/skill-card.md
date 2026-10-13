## Description:

Searches Chinese tender and procurement announcements by keyword, location, budget, date, and industry, with project details and market insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and sales teams use this skill to find Chinese tender opportunities, inspect announcements and project timelines, research companies, and compare market activity.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: First-use account registration may collect device characteristics, including a hashed network MAC address.

Mitigation: Set your own ZLBX_API_KEY to avoid automatic registration, or review the data collection and give explicit consent before registering.

Risk: Automatic registration persists an API key in a local account configuration file.

Mitigation: Protect the local configuration and review whether persistent credentials are appropriate for your environment.

Risk: Queries may use paid credits, and exhausted accounts may be directed to recharge or login links.

Mitigation: Check account balance and query costs before use; verify payment or login links before following them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/smart-tender-procurement-search)
- [Skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Search API reference](references/api-search.md)
- [Company API reference](references/api-company.md)
- [Market API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [First-use registration reference](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with linked results and summary tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes search filters, dates, amounts, and source links when available.]

## Skill Version(s):

1.0.6 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
