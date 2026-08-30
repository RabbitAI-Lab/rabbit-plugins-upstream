## Description:

查询国家贸易概览汇总数据，获取年度贸易总量、季度贸易量、供应商和采购商数量等国家维度汇总信息，帮助外贸团队、贸易分析师和市场研究人员评估国家级贸易概览和伙伴生态。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External trade teams, analysts, and market researchers use this skill to query the Upkuajing paid API for annual and quarterly country-level trade totals and supplier or buyer counts. It supports macro trade intelligence across country pairs or broader country filters when the user has an API key and confirms paid calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid API queries or recharge flows could incur cost without clear user intent.

Mitigation: Tell the user the action may incur charges and wait for explicit confirmation in a separate message before running paid query or recharge commands.

Risk: The API key may be exposed if environment files or command output are shared carelessly.

Mitigation: Keep UPKUAJING_API_KEY private and avoid printing or sharing the contents of ~/.upkuajing/.env.

Risk: Error reports may include operational context from failed API calls.

Mitigation: Review the error-report context with the user and send it only after user confirmation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/customs-overview-summary-zh)
- [Upkuajing Homepage](https://www.upkuajing.com)
- [国家贸易概览-交易汇总 API 参考](references/customs-overview-summary-api.md)
- [Agent调用Skill异常上报 API 参考](references/skill-error-report-api.md)
- [Upkuajing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; paid query and recharge flows require separate user confirmation.]

## Skill Version(s):

1.0.1 (source: evidence.release.version and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
