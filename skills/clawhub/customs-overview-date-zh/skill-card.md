## Description: <br>
Queries UpKuaJing for date reference values such as last year, last month, and the same month last year for customs trade analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, trade analysts, and developers use this skill to retrieve accurate date parameters for customs overview queries, trend analysis, and related import-export research. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API calls can incur fees and may require account top-up or payment approval. <br>
Mitigation: Confirm fee-generating operations with the user before execution and use UpKuaJing pricing or account-balance checks for current cost details. <br>
Risk: The skill reads an UpKuaJing API key from the environment or ~/.upkuajing/.env. <br>
Mitigation: Prefer a managed environment variable for the API key and avoid exposing or sharing the local credential file. <br>
Risk: The skill contacts openapi.upkuajing.com to retrieve date reference values. <br>
Mitigation: Use the skill only when outbound requests to UpKuaJing are acceptable for the user's environment. <br>


## Reference(s): <br>
- [Date Reference API](references/customs-overview-date-api.md) <br>
- [UpKuaJing](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, shell commands, guidance] <br>
**Output Format:** [Formatted JSON from Python scripts, with natural-language guidance before paid API operations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results include date reference fields and fee information returned by the UpKuaJing API.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md metadata and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
