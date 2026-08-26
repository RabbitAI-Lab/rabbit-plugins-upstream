## Description:

调取 LinkedIn 企业主页数据获取员工清单与整体人员规模，剖析企业内部组织架构，挖掘潜在商务联系人以及核心岗位决策人员。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, sales teams, and B2B lead builders use this skill to retrieve LinkedIn-sourced employee lists and job titles by company ID. It supports talent research, organization analysis, contact enrichment, and lead qualification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup calls use Upkuajing's paid API and can deduct account balance.

Mitigation: Tell the user a lookup may incur charges, obtain separate explicit confirmation before paid calls, and use the pricing command or pricing page instead of estimating costs.

Risk: The skill reads or creates an API key in ~/.upkuajing/.env.

Mitigation: Keep the key local, avoid exposing it in prompts or reports, and rotate it if it is disclosed.

Risk: Error reports can include request context and response details.

Mitigation: Send reports only after user approval and remove secrets or sensitive business data from report context.

Risk: The skill makes network calls to Upkuajing services, including lookup, account, pricing, error-reporting, and version-check requests.

Mitigation: Install and run the skill only when Upkuajing network access and service terms are acceptable for the user's workflow.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/upkuajing/skills/linkedin-company-employee-zh)
- [Upkuajing homepage](https://www.upkuajing.com)
- [Upkuajing developer platform](https://developer.upkuajing.com/)
- [Upkuajing API pricing](https://www.upkuajing.com/web/openapi/price.html)
- [领英员工列表 API 参考](references/linkedin-company-employee-list-api.md)
- [Agent调用Skill异常上报 API 参考](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a company ID and supports cursor-based pagination; lookup calls may include fee and request ID details.]

## Skill Version(s):

1.0.3 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
