## Description:

Analyzes Chinese public procurement notices, awards, suppliers, and pricing to help identify opportunities and market trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Business development teams and analysts use this skill to search Chinese government procurement notices, assess buyers and suppliers, compare award prices, and identify upcoming opportunities.

### Deployment Geography for Use:

Global (focused on Chinese public procurement data)

## Known Risks and Mitigations:

Risk: Trial registration can transmit a hashed device identifier and save an API key locally.

Mitigation: Confirm registration with the user first; configure ZLBX_API_KEY manually to avoid automatic registration and local key creation.

Risk: Data and company-registry queries can consume paid account credits.

Mitigation: Call only the requested endpoints, avoid unsolicited pagination, and check the free balance endpoint when needed.

Risk: Account checks and update acknowledgments create additional service requests.

Mitigation: Review these requests before use and acknowledge an update only after displaying its notice to the user.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/government-procurement-bigdata-analyzer)
- [Zhiliaobiaoxun skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Procurement search API reference](references/api-search.md)
- [Account API reference](references/api-account.md)
- [Automatic registration reference](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Markdown with result tables and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries and comparisons depend on returned procurement data and selected filters.]

## Skill Version(s):

1.0.8 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
