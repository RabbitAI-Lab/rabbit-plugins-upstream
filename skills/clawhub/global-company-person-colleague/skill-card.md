## Description: <br>
Find internal company teammates by company ID and person ID, returning colleague identifiers and job titles from UpKuaJing's global company database. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Recruiters, sales teams, business development teams, and B2B researchers use this skill to retrieve a target person's colleague roster when they already have the required company and person identifiers. It supports paid UpKuaJing API lookups and should be used with fee confirmation and appropriate data-handling controls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a paid people-data API, and each colleague lookup or pagination request can incur fees. <br>
Mitigation: Confirm fees with the user before execution, use the pricing reference or price-info command for current pricing, and create payment orders only when the user intentionally requests a top-up. <br>
Risk: The skill requires an UpKuaJing API key stored locally and used for authenticated API requests. <br>
Mitigation: Protect UPKUAJING_API_KEY, avoid exposing the local credential file or command output that contains secrets, and limit access to the account environment. <br>
Risk: Colleague search results can contain sensitive personal or business relationship data. <br>
Mitigation: Share only necessary results, follow applicable privacy and compliance requirements, and avoid redistributing outputs beyond the intended business purpose. <br>


## Reference(s): <br>
- [Colleague List API Reference](references/person-colleague-list-api.md) <br>
- [UpKuaJing](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing API Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON output from the API scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; API calls are paid and can return paginated colleague records.] <br>

## Skill Version(s): <br>
1.0.4 (source: evidence release version and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
