## Description:

调取 LinkedIn 用户的完整任职履历清单，梳理目标人员职业发展轨迹、就职企业变动情况以及专业从业背景，为商务尽调、客户背景分析提供参考依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, hiring managers, sales teams, and diligence users use this skill to retrieve a LinkedIn person's employment history by person ID, including company names, roles, dates, and employment status. It supports candidate screening, background review, professional experience assessment, and talent acquisition workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid API lookups may incur charges for each query page.

Mitigation: Tell the user the lookup is paid and wait for an explicit separate confirmation before running a paid query.

Risk: The API key is stored in a local plaintext .env file.

Mitigation: Limit access to the local environment file and avoid sharing the UPKUAJING_API_KEY value in prompts, logs, or reports.

Risk: Recharge-order and payment URL flows can expose users to payment risk.

Mitigation: Have the user verify payment URLs and account context before opening or paying any recharge order.

Risk: Error reports can include request context or response details.

Mitigation: Ask for confirmation before reporting errors and avoid including sensitive personal data, tokens, or full API responses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/linkedin-person-experience-zh)
- [Upkuajing homepage](https://www.upkuajing.com)
- [Upkuajing developer platform](https://developer.upkuajing.com/)
- [工作经历列表 API](references/linkedin-person-experience-list-api.md)
- [异常上报 API](references/skill-error-report-api.md)
- [OpenAPI price information](https://www.upkuajing.com/web/openapi/price.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; paid queries require explicit user confirmation before execution.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
