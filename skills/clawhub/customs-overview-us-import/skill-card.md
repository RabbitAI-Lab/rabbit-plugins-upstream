## Description: <br>
Query US import transaction statistics, including import records, container counts, and last-90-day data grouped by state or city with cursor-based pagination. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Export teams, logistics analysts, and trade professionals use this skill to monitor US import activity, compare state-level or city-level container flows, and evaluate market entry opportunities using UpKuaJing customs data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API calls and top-up actions can incur fees through UpKuaJing's paid API. <br>
Mitigation: Confirm current pricing and get explicit user approval before running paid queries or creating recharge orders. <br>
Risk: The skill can store UPKUAJING_API_KEY in plaintext at ~/.upkuajing/.env. <br>
Mitigation: Protect the local .env file, limit access to the user account, and remove the key when it is no longer needed. <br>
Risk: The skill performs a daily version check with the provider during API use. <br>
Mitigation: Run the skill only in environments where outbound provider checks are acceptable. <br>


## Reference(s): <br>
- [US Import API Reference](references/customs-overview-us-import-api.md) <br>
- [UpKuaJing Homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/customs-overview-us-import) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; calls a paid UpKuaJing API and returns paginated state or city import statistics with fee information.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
