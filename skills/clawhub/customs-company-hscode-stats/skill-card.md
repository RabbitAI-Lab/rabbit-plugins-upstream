## Description: <br>
Query company customs trade statistics by HS code dimension to analyze HS code distribution, trade volume breakdown, and monthly trade trends. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to query UpKuaJing customs data for a company's HS code distribution, trade volume breakdown, and monthly trade trends. It supports supplier or buyer analysis using a company ID, role, and optional filters such as date range, products, HS codes, ports, and countries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses an UpKuaJing API key and can store it in ~/.upkuajing/.env. <br>
Mitigation: Keep the API key out of shared logs and restrict local file permissions for ~/.upkuajing/.env. <br>
Risk: Queries and account top-up actions are tied to paid account workflows. <br>
Mitigation: Confirm every paid query or top-up action separately before execution. <br>
Risk: The scripts can check for skill updates against the UpKuaJing service and cache version data locally. <br>
Mitigation: Review the once-daily version check behavior before installing in restricted environments. <br>


## Reference(s): <br>
- [Company HS Code Trade Statistics API](references/customs-company-hscode-stats-api.md) <br>
- [UpKuaJing Homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing Open API Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with direct Python commands and formatted JSON API responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires UPKUAJING_API_KEY and paid UpKuaJing account access; successful responses include HS code statistics, monthly trend data, and fee information.] <br>

## Skill Version(s): <br>
1.0.0 (source: artifact metadata and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
