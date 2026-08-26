## Description:

按 LinkedIn 人员 ID 查询教育经历列表，返回院校、学位、专业、辅修科目、GPA、时间范围和摘要等信息。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, HR teams, hiring managers, and sales or business development users can retrieve LinkedIn education history for a known person ID to support credential review, candidate screening, background checks, talent assessment, customer profiling, and relationship discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid lookups and paginated follow-up requests can incur charges through Upkuajing's API service.

Mitigation: Confirm each paid query or pagination request before running the lookup, and use the documented price information flow rather than estimating costs.

Risk: The skill requires an Upkuajing API key that may be stored in ~/.upkuajing/.env.

Mitigation: Store the key only in the documented environment variable or local .env file, avoid sharing it in prompts or reports, and rotate it if exposed.

Risk: Lookups, account support, recharge helpers, version checks, and optional error reports contact Upkuajing services.

Mitigation: Use the skill only when external service contact is acceptable for the intended workflow and data handling requirements.

Risk: Optional error reports can include request context and response data.

Mitigation: Submit error reports only after user confirmation and exclude secrets or unnecessary personal data from the report context.

## Reference(s):

- [LinkedIn 人物教育经历列表 API 参考](references/linkedin-person-education-list-api.md)
- [Agent 调用 Skill 异常上报 API 参考](references/skill-error-report-api.md)
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/linkedin-person-education-zh)
- [Upkuajing homepage](https://www.upkuajing.com)
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html)
- [Upkuajing developer platform](https://developer.upkuajing.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API results from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Education lookup results are paginated by cursor and include fee and request identifiers when returned by the API.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
