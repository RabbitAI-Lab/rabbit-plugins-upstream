## Description: <br>
Retrieves company shareholder, executive, and beneficial-owner information from UpKuaJing's global company database by company ID. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, investors, industry analysts, sales teams, and risk specialists use this skill to look up shareholder rosters, ownership ratios, and beneficial-owner signals for due diligence, investment research, competitor analysis, related-party screening, and B2B prospecting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API calls and account top-ups may incur charges through UpKuaJing's paid API. <br>
Mitigation: Review current pricing and require explicit user confirmation before running billable queries or creating top-up orders. <br>
Risk: The billable API key may be stored locally in ~/.upkuajing/.env. <br>
Mitigation: Keep the file private, avoid sharing logs or screenshots that expose credentials, and rotate the key if it may have been disclosed. <br>
Risk: The skill performs an automatic version check against the UpKuaJing API. <br>
Mitigation: Account for this outbound request when reviewing network behavior and deployment policy. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/global-company-shareholder) <br>
- [UpKuaJing homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [Shareholder List API reference](references/company-shareholder-list-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON responses and Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a company ID and an UPKUAJING_API_KEY; successful responses include shareholder list data and fee metadata.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
