## Description: <br>
Queries company customs trade statistics by region dimension, including trade volume, amount, monthly trends, and country distribution across global markets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and analysts use this skill to query UpKuaJing customs data for company-level trade distribution by country or region. It helps review market coverage, trade volume, monthly activity, and import-export country distribution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores and reads the UpKuaJing API key from a plaintext file under ~/.upkuajing/.env. <br>
Mitigation: Treat the file as a secret, avoid pasting or displaying its contents in chat or logs, and limit access to the local account that runs the skill. <br>
Risk: The skill performs paid API calls and includes account top-up workflows. <br>
Mitigation: Require explicit user confirmation before fee-generating calls and review any payment URL before opening it. <br>
Risk: Customs-data queries are sent to the UpKuaJing API service. <br>
Mitigation: Use the skill only when the user trusts UpKuaJing with the queried company and trade-data context. <br>


## Reference(s): <br>
- [Company Area Trade Statistics API](references/customs-company-area-stats-api.md) <br>
- [UpKuaJing Homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing API Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/customs-company-area-stats) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python, httpx, and UPKUAJING_API_KEY; API calls may return fee information.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md metadata and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
