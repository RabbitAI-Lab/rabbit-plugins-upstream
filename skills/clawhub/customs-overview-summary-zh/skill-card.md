## Description: <br>
查询国家贸易概览汇总数据，帮助外贸团队、贸易分析师和市场研究人员获取年度贸易总量、季度贸易量以及供应商和采购商数量等国家级汇总信息。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External trade teams, trade analysts, and market researchers use this skill to query paid Upkuajing customs data for country-level annual and quarterly trade summaries. It supports strategic market assessment by returning trade volume, supplier counts, and buyer counts for an origin or destination country and year. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a paid Upkuajing API account for queries, account information, and recharge order actions. <br>
Mitigation: Require explicit user confirmation before fee-incurring queries or recharge actions, and check current pricing with the provided price lookup instead of estimating costs. <br>
Risk: The skill reads an API key from the environment or ~/.upkuajing/.env and can create and store a new key locally. <br>
Mitigation: Protect ~/.upkuajing/.env with appropriate file permissions, avoid exposing the key in prompts or logs, and rotate the key if disclosure is suspected. <br>
Risk: The skill includes version-check behavior that contacts the Upkuajing API during request handling. <br>
Mitigation: Review outbound network behavior before deployment and run it only in environments where the Upkuajing endpoints are approved. <br>


## Reference(s): <br>
- [国家贸易概览-交易汇总 API 参考](references/customs-overview-summary-api.md) <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-overview-summary-zh) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing developer platform](https://developer.upkuajing.com/) <br>
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, JSON, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; API calls may incur charges.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
