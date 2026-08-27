## Description:

查询公司海关贸易区域列表数据，获取国家或地区的贸易次数、金额和占比，用于市场进入分析、客户分布研究和区域贸易情报。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External trade teams, market analysts, and agents use this skill to query a company's country or region-level customs trade distribution, including trade count, amount, quantity, weight, and share. It helps compare regional market exposure and identify priority export or procurement markets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill performs paid customs-data API calls and exposes account balance or recharge flows.

Mitigation: Tell the user a lookup or recharge action may incur cost, obtain explicit confirmation before paid actions, and use price information from the provider instead of estimating fees.

Risk: The skill handles UPKUAJING_API_KEY and may store it in a local plaintext configuration file.

Mitigation: Avoid displaying or pasting the API key, restrict local file access where possible, and rotate the key if it may have been exposed.

Risk: Diagnostic error reports may include request context and response details.

Mitigation: Review report contents with the user and send diagnostic reports only after explicit confirmation.

Risk: The skill performs automatic provider version-check calls with local persistence.

Mitigation: Install only if this provider communication is acceptable in the deployment environment and review local cache behavior during security assessment.

## Reference(s):

- [公司贸易区域列表 API 参考](references/customs-company-area-list-api.md)
- [Agent调用Skill异常上报 API 参考](references/skill-error-report-api.md)
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-company-area-list-zh)
- [跨境魔方官网](https://www.upkuajing.com)
- [跨境魔方开放平台](https://developer.upkuajing.com/)
- [开放平台价格说明](https://www.upkuajing.com/web/openapi/price.html)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; successful lookup responses include data, fee information, and request identifiers.]

## Skill Version(s):

1.0.1 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
