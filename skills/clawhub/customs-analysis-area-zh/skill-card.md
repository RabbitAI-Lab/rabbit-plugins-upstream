## Description: <br>
Queries country and region distribution data for a specified HS code through the Upkuajing customs trade API, returning trade counts, trade amounts, buyer counts, and supplier counts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External trade analysts, market researchers, and import/export teams use this skill to compare exporter or importer activity by country for a selected HS code and recent-month window. It helps identify active markets and geographic distribution patterns from customs trade data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores and reads an Upkuajing API key from the local environment or ~/.upkuajing/.env. <br>
Mitigation: Protect the local key file, avoid displaying or pasting the API key unnecessarily, and install only when the Upkuajing account and queries involved are trusted. <br>
Risk: Customs-data API calls are billable and may consume account balance. <br>
Mitigation: Check current pricing with the documented price command or pricing page and require a separate explicit confirmation before running billable queries. <br>
Risk: Recharge support flows can return a payment URL. <br>
Mitigation: Review the recharge URL before opening it and continue only after the user confirms payment completion. <br>


## Reference(s): <br>
- [分析报告-区域分布 API 参考](references/customs-analysis-area-api.md) <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-analysis-area-zh) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing developer platform](https://developer.upkuajing.com/) <br>
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [API responses include paginated country-level trade metrics and fee information when returned by the service.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md metadata and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
