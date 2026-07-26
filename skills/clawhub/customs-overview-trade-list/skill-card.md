## Description: <br>
Queries paginated national trade list data from the UpKuaJing Open Platform API, returning country-level annual, quarterly, and monthly trade volumes plus supplier and buyer counts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External export teams, market researchers, and trade analysts use this skill to compare import-export volumes across countries, analyze market penetration, and identify growth opportunities from structured country-level customs trade data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles an UpKuaJing API key and may read or write it in a plaintext local file. <br>
Mitigation: Prefer a managed secret store or a tightly permissioned local file, and avoid exposing the API key in prompts, logs, or shared outputs. <br>
Risk: API queries and account top-up actions can incur charges. <br>
Mitigation: Require separate explicit user confirmation before any billed query or top-up action, and check current pricing before execution. <br>
Risk: Queries send trade parameters and the API key to the UpKuaJing API. <br>
Mitigation: Install and use the skill only when the user trusts UpKuaJing and is comfortable sending the required query data to that service. <br>


## Reference(s): <br>
- [Customs Overview Trade List API Reference](references/customs-overview-trade-list-api.md) <br>
- [UpKuaJing Homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Developer Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/customs-overview-trade-list) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and formatted JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires UPKUAJING_API_KEY; paginated API calls return fee information and may include a cursor for additional pages.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
