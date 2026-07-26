## Description: <br>
Searches UpKuaJing customs data for matching HS codes by product name and HS code keyword so agents can prepare downstream trade analysis reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Trade analysts, exporters, import-export professionals, and agents use this skill to find likely customs classification codes before running deeper market, competitor, or trade-flow analysis. It is intended for HS code lookup using the paid UpKuaJing Open Platform API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a paid external API, and each HS code search can incur account charges. <br>
Mitigation: Tell the user that the query is billable and wait for explicit confirmation before making a charged API call or creating a top-up order. <br>
Risk: The API key may be stored in plaintext under ~/.upkuajing/.env. <br>
Mitigation: Prefer supplying UPKUAJING_API_KEY through a managed secret mechanism when available and restrict access to any local credential file. <br>
Risk: The helper scripts include account, balance, key creation, and top-up workflows. <br>
Mitigation: Use account and payment helpers only after the user explicitly requests them, and show payment URLs without completing payment on the user's behalf. <br>
Risk: The security review notes an automatic version check to UpKuaJing. <br>
Mitigation: Inform operators that the skill may contact UpKuaJing for version information before API use and review that behavior before deployment. <br>


## Reference(s): <br>
- [HS Code Search API Reference](references/customs-analysis-hscode-search-api.md) <br>
- [UpKuaJing Homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing Open API Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Natural-language guidance with optional shell commands and JSON API results containing matching HS code strings, pagination cursor, and fee details.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python, httpx, and UPKUAJING_API_KEY; queries are paid per API call.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
