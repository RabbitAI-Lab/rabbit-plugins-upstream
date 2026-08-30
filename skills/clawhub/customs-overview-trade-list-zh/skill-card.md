## Description:

查询分页的国家级贸易列表数据，返回年度、季度和月度贸易量以及供应商和采购商数量，用于国家间进出口市场分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External trade teams, market researchers, and trade analysts use this skill to query paginated country-level customs trade data, compare origin and arrival countries, and analyze trade volume patterns across annual, quarterly, and monthly views.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles an Upkuajing API key and reads or writes local files under ~/.upkuajing.

Mitigation: Install only when comfortable granting access to the Upkuajing account, keep the API key out of shared logs and messages, and review local credential storage before use.

Risk: Trade-list queries and recharge-order workflows can involve paid API usage.

Mitigation: Confirm paid queries and recharge orders in a separate explicit user message, and use the platform price information before estimating costs.

Risk: Diagnostic error reports can include request context, request data, or response data related to business activity.

Mitigation: Approve diagnostic reports only after checking that the submitted context and payload do not contain secrets or sensitive business information.

Risk: The security verdict is suspicious because API keys, recharge orders, diagnostics, and automatic version checks deserve manual review before installation.

Mitigation: Review the security summary and script behavior before deployment, especially network calls and local ~/.upkuajing state changes.

## Reference(s):

- [国家贸易列表 API 参考](artifact/references/customs-overview-trade-list-api.md)
- [Agent 调用 Skill 异常上报 API 参考](artifact/references/skill-error-report-api.md)
- [Upkuajing Homepage](https://www.upkuajing.com)
- [跨境魔方开放平台](https://developer.upkuajing.com/)
- [开放平台价格说明](https://www.upkuajing.com/web/openapi/price.html)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; successful trade-list calls include paginated data, fee details, and request identifiers.]

## Skill Version(s):

1.0.1 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
