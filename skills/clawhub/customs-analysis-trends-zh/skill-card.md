## Description: <br>
Queries recent monthly import and export trend data for a specified HS code, including trade count, quantity, weight, value, buyer count, and supplier count. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Trade analysts, supply chain managers, and market researchers use this skill to retrieve monthly export and import trend data for a specified HS code, compare movement over time, and monitor seasonal or market changes across customs trade data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a paid Upkuajing API account and may trigger billable calls. <br>
Mitigation: Require separate user confirmation before billable calls, check current pricing through the documented pricing command or pricing page, and review any recharge or payment URL before opening it. <br>
Risk: The skill handles an Upkuajing API key and stores or reads it from the local user environment. <br>
Mitigation: Keep the API key out of chat output, store it with restricted local permissions, and avoid sharing logs or files that may expose account details. <br>
Risk: The security evidence notes an undisclosed version check in addition to the advertised trade-trend query. <br>
Mitigation: Review the outbound version-check behavior before installation and account for it when evaluating network access. <br>


## Reference(s): <br>
- [Analysis Trends API reference](references/customs-analysis-trends-api.md) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing developer platform](https://developer.upkuajing.com/) <br>
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON, guidance] <br>
**Output Format:** [Markdown guidance with Python command examples and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; API responses may include fee and account-balance information.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
