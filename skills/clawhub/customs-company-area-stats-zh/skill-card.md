## Description:

查询公司海关贸易区域维度统计数据，帮助分析贸易量、金额、月度趋势和国家分布，覆盖全球市场。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External trade teams and agents use this skill to query Upkuajing customs data for a company's supplier or buyer trade distribution by country and region. It supports regional market coverage analysis, import/export trend monitoring, and discovery of emerging market opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid API queries can incur charges.

Mitigation: Tell the user a query will cost money and wait for explicit confirmation before running paid query scripts.

Risk: The API key is stored in a plaintext .env file when created by the helper script.

Mitigation: Ask users to store the key carefully, avoid sharing it, and remove or rotate it if exposure is suspected.

Risk: Error reports can include diagnostic context from failed API calls.

Mitigation: Review the context with the user and get confirmation before sending an error report.

## Reference(s):

- [公司贸易区域维度统计 API 参考](references/customs-company-area-stats-api.md)
- [Agent调用Skill异常上报 API 参考](references/skill-error-report-api.md)
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-company-area-stats-zh)
- [Upkuajing homepage](https://www.upkuajing.com)
- [Upkuajing developer platform](https://developer.upkuajing.com/)
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; paid query responses include fee information and request IDs.]

## Skill Version(s):

1.0.1 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
