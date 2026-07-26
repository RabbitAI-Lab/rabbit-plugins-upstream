## Description: <br>
Customs Analysis Overview queries the UpKuaJing customs analysis overview API to return supplier and buyer counts grouped by country with cursor-based pagination. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Trade analysts, market researchers, and import-export professionals use this skill to compare supplier and buyer presence by country and identify active markets in customs trade data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can query a paid customs-data API and may create top-up payment URLs. <br>
Mitigation: Confirm any paid query or top-up action with the user before execution and check current pricing through the provider before making calls. <br>
Risk: The skill can use or create an UPKUAJING_API_KEY and store it in a plaintext ~/.upkuajing/.env file. <br>
Mitigation: Prefer an environment variable or another managed secret-storage process, and avoid exposing the key in prompts, logs, or shared files. <br>
Risk: The skill performs a daily provider version check when making API requests. <br>
Mitigation: Review this outbound provider contact before installation in restricted environments. <br>


## Reference(s): <br>
- [Analysis Overview API Reference](references/customs-analysis-overview-api.md) <br>
- [UpKuaJing Homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Developer Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing Open API Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/customs-analysis-overview) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns country-level records with country code, supplier count, buyer count, latest trade date, cursor pagination, and fee information when available.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
