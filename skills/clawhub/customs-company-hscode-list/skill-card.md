## Description: <br>
Queries paginated UpKuaJing customs HS code trade data for a company, including HS codes, trade counts, amounts, quantities, weights, and trade percentages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and trade analysts use this skill to query paginated HS code breakdowns for a supplier or buyer company through the UpKuaJing Open Platform API. It supports product-mix analysis and HS code drill-down across customs trade data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid API calls and top-up flows can incur costs. <br>
Mitigation: Confirm the fee impact before executing queries or creating top-up orders, and use the published pricing page or auth.py --price_info for current pricing. <br>
Risk: The skill stores and reads the UpKuaJing API key from ~/.upkuajing/.env. <br>
Mitigation: Keep the API key private, restrict local file access where possible, and rotate the key if it may have been exposed. <br>
Risk: Network calls send company query parameters to the third-party UpKuaJing API. <br>
Mitigation: Use only data appropriate for the third-party service and avoid enabling API logging when query parameters or responses are sensitive. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-company-hscode-list) <br>
- [Company HS Code List API](references/customs-company-hscode-list-api.md) <br>
- [UpKuaJing homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing API pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API response summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; API calls may incur per-call fees and return paginated results.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
