## Description:

查询指定HS编码在最近N个月的进出口贸易趋势数据，返回出口和进口的月度贸易次数、数量、重量、金额、采购商数量和供应商数量。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Trade analysts, supply chain managers, market researchers, and agents use this skill to retrieve monthly import and export trend data for a specified HS code, optionally filtered by country. It supports trend analysis, seasonal pattern review, and comparison of import versus export activity using Upkuajing customs trade data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: This skill uses a paid Upkuajing API service and normal trend queries can incur charges.

Mitigation: Confirm user consent before any charged query or recharge flow, and use the documented price endpoint or pricing page instead of estimating fees.

Risk: The API key may be stored in ~/.upkuajing/.env and can authorize paid API calls.

Mitigation: Keep the API key file private, avoid exposing the key in chat or reports, and prefer environment-variable or local-file handling over copying credentials into prompts.

Risk: Exception reports can include request context, parameters, or response snippets that may contain sensitive customer or trade details.

Mitigation: Submit exception reports only after user confirmation and avoid including secrets, customer data, or confidential trade details.

## Reference(s):

- [贸易趋势 API 参考](references/customs-analysis-trends-api.md)
- [Skill 异常上报 API 参考](references/skill-error-report-api.md)
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-analysis-trends-zh)
- [Upkuajing homepage](https://www.upkuajing.com)
- [Upkuajing developer platform](https://developer.upkuajing.com/)
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Query output includes trend data, fee details, and requestId when the API call succeeds.]

## Skill Version(s):

1.0.1 (source: server release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
