## Description:

依托全球企业数据库查询企业员工清单与人员规模（Headcount），摸清企业内部组织架构，帮外贸销售、猎头从业者挖掘目标企业潜在对接人员。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, sales teams, and B2B lead builders use this skill to retrieve employee lists, titles, and pagination data for a known company ID from Upkuajing's global company database. It supports talent research, competitor organization analysis, decision-maker discovery, and lead qualification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a paid Upkuajing API and employee lookup calls may incur charges.

Mitigation: Confirm each paid lookup or recharge step before execution and use the provided pricing/account checks when cost details are needed.

Risk: The skill depends on UPKUAJING_API_KEY and may read it from the user's environment or ~/.upkuajing/.env.

Mitigation: Treat the API key as a secret, avoid displaying or sharing the env file, and rotate the key if it is exposed.

Risk: Optional error reports may include request or response details.

Mitigation: Review the report contents before sending and omit sensitive or unnecessary context.

Risk: The scanner noted a limited under-disclosed version check.

Mitigation: Expect a version-check request to Upkuajing infrastructure when scripts run, and evaluate that network behavior before deployment in restricted environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/global-company-employee-zh)
- [Upkuajing homepage](https://www.upkuajing.com)
- [Upkuajing developer portal](https://developer.upkuajing.com/)
- [Upkuajing API pricing](https://www.upkuajing.com/web/openapi/price.html)
- [Global company employee list API](references/company-employee-list-api.md)
- [Skill error report API](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a company ID and an Upkuajing API key; employee list responses may be paginated with a cursor.]

## Skill Version(s):

1.0.6 (source: server release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
