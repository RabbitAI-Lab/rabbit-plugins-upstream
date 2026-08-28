## Description:

查询供应商或采购商TopN排名，按国家维度和年份返回供应商或采购商的贸易量排名列表，支持游标分页。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External trade analysts, procurement agents, and import/export teams use this skill to identify top suppliers or buyers on a country route for a selected year, evaluate market concentration, and support sourcing or sales planning with customs trade data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill manages paid API calls and account/recharge helper commands.

Mitigation: Tell the user when an action may incur charges and wait for explicit confirmation before running query or recharge commands.

Risk: The skill stores an API key in plaintext under ~/.upkuajing.

Mitigation: Use only trusted environments, restrict local file access, rotate exposed keys, and avoid sharing the ~/.upkuajing/.env file.

Risk: Error-report context may include sensitive business details or personal data.

Mitigation: Ask before submitting reports and omit secrets, personal data, and sensitive business payloads from report context.

Risk: The skill performs an automatic version check against the Upkuajing service.

Mitigation: Review outbound network behavior before deployment in restricted environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-overview-top-n-zh)
- [Upkuajing homepage](https://www.upkuajing.com)
- [Upkuajing developer platform](https://developer.upkuajing.com/)
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html)
- [国家贸易概览-采供商TopN API 参考](references/customs-overview-top-n-api.md)
- [Agent调用Skill异常上报 API 参考](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [API Calls, Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; paid API calls should be confirmed before execution.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
