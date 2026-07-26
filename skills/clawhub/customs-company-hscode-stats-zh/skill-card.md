## Description: <br>
Queries Upkuajing customs data for company-level HS-code trade statistics, including monthly trends, HS-code distribution, trade counts, and share of trade. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Trade analysts, sourcing teams, and supply-chain operators use this skill to inspect how a company’s import or export activity breaks down by HS code and how those product categories change over time. The skill helps agents prepare and run paid Upkuajing API queries, then interpret returned HS-code and monthly trend data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read or create ~/.upkuajing/.env and store UPKUAJING_API_KEY there in plaintext. <br>
Mitigation: Keep the file private, prefer environment-variable injection where practical, never paste or display the full API key in chat, and rotate the key if it is exposed. <br>
Risk: The skill makes paid Upkuajing API calls and can create recharge payment links. <br>
Mitigation: Review pricing or recharge links first, tell the user a query will incur charges, and wait for explicit confirmation in a separate message before running charged commands. <br>
Risk: Company IDs and query filters are sent to Upkuajing over network API calls. <br>
Mitigation: Confirm the requested company and filters are appropriate to share with Upkuajing, and send only the parameters needed for the analysis. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-company-hscode-stats-zh) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing developer platform](https://developer.upkuajing.com/) <br>
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [公司贸易HS编码维度统计 API 参考](references/customs-company-hscode-stats-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, JSON] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [API responses include HS-code statistics, monthly trend data, and fee details; charged queries require explicit user confirmation before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
