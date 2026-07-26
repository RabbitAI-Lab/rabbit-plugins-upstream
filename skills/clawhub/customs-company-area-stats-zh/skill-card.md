## Description: <br>
查询公司海关贸易区域维度统计数据，帮助外贸团队分析贸易量、金额、月度趋势和国家分布，覆盖全球市场。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External trade intelligence users and business analysts use this skill to query company-level customs trade statistics by region or country, including trade counts, amounts, quantities, weights, monthly trends, and country distribution. It supports supplier and buyer market coverage analysis, import/export distribution tracking, and emerging-market discovery through the Upkuajing customs data API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid API calls may spend account credits. <br>
Mitigation: Confirm the user's intent before running paid queries and use the pricing helper or pricing page when cost details are needed. <br>
Risk: The API key may be stored locally in plaintext at ~/.upkuajing/.env. <br>
Mitigation: Avoid displaying the API key, restrict local file permissions where possible, and prefer environment-variable injection in managed environments. <br>
Risk: Recharge helpers can create payment URLs. <br>
Mitigation: Only create or share recharge payment URLs after the user explicitly requests account recharge. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-company-area-stats-zh) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing developer platform](https://developer.upkuajing.com/) <br>
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [公司贸易区域维度统计 API 参考](references/customs-company-area-stats-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python, httpx, and UPKUAJING_API_KEY; paid API calls return fee information with the query result.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
