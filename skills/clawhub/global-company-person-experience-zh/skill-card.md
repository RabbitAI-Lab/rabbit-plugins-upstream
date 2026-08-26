## Description:

调取全球企业人员数据库获取目标人员的任职履历和完整工作时间线，充实 B2B 销售线索画像，梳理联系人过往任职经历，研判对方职业发展轨迹。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Business development, recruiting, and research users can use this skill to look up a person's global company work-history records by person ID, optionally filter by company ID, and page through returned employment records. It is suited to enriching contact profiles, reviewing prior roles, and understanding career timelines before outreach or assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a UPKUAJING API key and may store a newly issued key in plaintext under ~/.upkuajing/.env.

Mitigation: Use a dedicated API key, restrict local file access where possible, and rotate or remove the key when the skill is no longer needed.

Risk: Lookup calls are paid and recharge actions can create payment links.

Mitigation: Require explicit user confirmation before paid lookups or recharge actions, and verify current pricing through the provider before use.

Risk: Confirmed error reports are sent to the provider and may include request context.

Mitigation: Review report context before submission and remove secrets, customer data, or other sensitive details.

Risk: The skill may write version-check cache data under the user's home directory.

Mitigation: Review the automatic version-cache behavior before deployment in environments that prohibit silent home-directory writes.

## Reference(s):

- [工作经历列表 API](references/person-experience-list-api.md)
- [异常上报 API](references/skill-error-report-api.md)
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/global-company-person-experience-zh)
- [跨境魔方 homepage](https://www.upkuajing.com)
- [跨境魔方 developer platform](https://developer.upkuajing.com/)
- [OpenAPI price information](https://www.upkuajing.com/web/openapi/price.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance, API results]

**Output Format:** [Markdown guidance with Python command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; lookup API calls are paid and require explicit user confirmation before execution.]

## Skill Version(s):

1.0.4 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
