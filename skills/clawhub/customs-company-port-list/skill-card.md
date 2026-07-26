## Description: <br>
Query paginated port trade data for a company and retrieve port-level trade statistics with counts, amounts, quantities, weights, and percentages for logistics analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, logistics analysts, and developers use this skill to inspect a company's import-export port distribution and drill into paginated port-level customs trade statistics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid API queries and top-up actions can incur charges. <br>
Mitigation: Require a separate explicit confirmation before fee-incurring queries or top-up flows, and use the provider pricing reference or price-info command for current fees. <br>
Risk: The API key may be stored locally in ~/.upkuajing/.env. <br>
Mitigation: Prefer managed secret storage for UPKUAJING_API_KEY and keep any local credential file private. <br>
Risk: Queries and daily version checks contact UpKuaJing services. <br>
Mitigation: Use the skill only when sharing query parameters with the UpKuaJing API and checking for provider-hosted updates is acceptable. <br>


## Reference(s): <br>
- [Company Port List API](references/customs-company-port-list-api.md) <br>
- [UpKuaJing Homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [JSON responses from Python scripts plus Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns paginated port-list data and fee information; requires UPKUAJING_API_KEY and explicit user confirmation before paid queries.] <br>

## Skill Version(s): <br>
1.0.0 (source: metadata.version and release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
