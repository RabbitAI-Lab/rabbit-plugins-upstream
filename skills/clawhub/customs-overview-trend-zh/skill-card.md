## Description: <br>
Queries monthly import and export trade totals for a requested date range through the Upkuajing customs data API, with cursor pagination for browsing trend results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Trade analysts, supply chain managers, market researchers, and agents use this skill to retrieve monthly country-level trade trend data, compare trade volumes over time, and identify seasonal or cyclical patterns for planning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid API calls can incur charges and expose fee or account balance metadata in responses. <br>
Mitigation: Confirm costs with the user before each paid query and use the skill's pricing flow instead of estimating fees. <br>
Risk: The API key is stored locally in ~/.upkuajing/.env. <br>
Mitigation: Protect the local environment file, avoid displaying full keys, and rotate or recreate credentials if they are exposed. <br>
Risk: The scripts contact openapi.upkuajing.com and perform a daily version check with a local cache. <br>
Mitigation: Use the skill only in environments where outbound Upkuajing API calls and local cache writes are acceptable. <br>


## Reference(s): <br>
- [国家贸易概览-进出口趋势 API 参考](references/customs-overview-trend-api.md) <br>
- [Upkuajing](https://www.upkuajing.com) <br>
- [跨境魔方开放平台](https://developer.upkuajing.com/) <br>
- [Upkuajing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; successful trend queries return paginated monthly trade data and fee metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
