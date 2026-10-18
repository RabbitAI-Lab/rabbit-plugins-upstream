## Description:

Helps agents search and analyze Chinese procurement notices, company activity, supplier relationships, market rankings, and historical award prices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams, business analysts, and their agents use this skill to find Chinese tender and award notices, assess companies and suppliers, and summarize market and pricing trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Procurement and company queries are sent to the Zhiliaobiaoxun service.

Mitigation: Avoid entering sensitive queries unless sharing them with the service is acceptable.

Risk: Auto-registration collects device features and saves an API key locally.

Mitigation: Prefer your own ZLBX_API_KEY; otherwise review the device data and ~/.zlbx/config.json before consenting.

Risk: Package-identity headers and upgrade-display acknowledgements may be under-disclosed.

Mitigation: Review these network behaviors with the publisher before installing or enabling the skill.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhiliaobiaoxun/skills/bid-data-intelligent-agent)
- [Zhiliaobiaoxun skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Procurement search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Registration and credential guidance](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text]

**Output Format:** [Markdown summaries, linked result tables, and structured reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results and contact details depend on available data and account access.]

## Skill Version(s):

1.0.9 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
