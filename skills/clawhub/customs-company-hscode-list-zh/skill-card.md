## Description: <br>
Queries Upkuajing customs data for a company's paginated HS-code trade breakdown, including trade count, amount, quantity, weight, and percentage share. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External trade teams, sourcing analysts, and agents use this skill to inspect a company's HS-code product mix and drill into customs trade composition by supplier or buyer role. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid API calls and recharge flows can incur costs. <br>
Mitigation: Confirm paid queries or recharge actions in a separate user message before execution, and check current pricing through the documented pricing command or pricing page. <br>
Risk: The skill stores and reads the Upkuajing API key from a plaintext local file. <br>
Mitigation: Use a dedicated API key, restrict local file access, and avoid printing or sharing ~/.upkuajing/.env. <br>
Risk: The API client sends trade queries and account actions to Upkuajing services. <br>
Mitigation: Review requested company identifiers, filters, account actions, and returned fee information before using the skill in sensitive workflows. <br>


## Reference(s): <br>
- [公司贸易HS编码列表 API 参考](references/customs-company-hscode-list-api.md) <br>
- [Upkuajing Homepage](https://www.upkuajing.com) <br>
- [Upkuajing Developer Platform](https://developer.upkuajing.com/) <br>
- [Upkuajing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and the UPKUAJING_API_KEY environment variable or local Upkuajing credential file.] <br>

## Skill Version(s): <br>
1.0.0 (source: metadata.version and release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
