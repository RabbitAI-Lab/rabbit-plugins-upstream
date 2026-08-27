## Description:

查询日期参考信息，返回去年年份、上月月份、去年当月月份等日期参考值，用于海关贸易数据查询。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External trade teams, trade analysts, and import/export practitioners use this skill to fetch date reference values for customs trade queries, market trend analysis, and trade intelligence workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores and uses an Upkuajing API key from ~/.upkuajing/.env.

Mitigation: Protect the local key file, avoid sharing the key in prompts or reports, and rotate the key if exposure is suspected.

Risk: Normal Upkuajing API calls are paid and the helper can create recharge or payment order requests.

Mitigation: Confirm charges before running queries and review any recharge or payment URL before paying.

Risk: Optional error reports may include business context or request details.

Mitigation: Send error reports only after user confirmation and omit sensitive business data where possible.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-overview-date-zh)
- [Upkuajing homepage](https://www.upkuajing.com)
- [Upkuajing developer platform](https://developer.upkuajing.com/)
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html)
- [国家贸易概览-日期相关 API 参考](references/customs-overview-date-api.md)
- [Agent调用Skill异常上报 API 参考](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Configuration guidance]

**Output Format:** [Markdown with JSON-backed date reference values and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires UPKUAJING_API_KEY; the date query has no business parameters; normal API calls are paid and require explicit user confirmation before execution.]

## Skill Version(s):

1.0.1 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
