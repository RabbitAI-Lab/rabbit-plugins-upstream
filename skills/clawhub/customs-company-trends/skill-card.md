## Description: <br>
Delivers monthly customs trade trend breakdowns for companies, including shipment frequency, product quantity, gross weight, and transaction value with optional filters. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Export teams, analysts, and supply-chain managers use this skill to analyze monthly customs activity, supplier performance, seasonal fluctuations, and long-term trade-flow patterns across global customs data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid UpKuaJing API calls and top-up operations can incur charges. <br>
Mitigation: Inform the user before fee-incurring actions, check current pricing through the documented price flow, and wait for explicit confirmation before executing paid queries or creating top-up orders. <br>
Risk: The skill reads or creates a local API-key file at ~/.upkuajing/.env. <br>
Mitigation: Keep UPKUAJING_API_KEY private, avoid sharing command output that contains credentials, and remove or rotate the key if it may have been exposed. <br>
Risk: The scripts contact openapi.upkuajing.com for customs queries, account actions, pricing, and version checks. <br>
Mitigation: Install and run the skill only in environments where outbound requests to the UpKuaJing API are acceptable. <br>


## Reference(s): <br>
- [Company Trade Trends API Reference](references/customs-company-trends-api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/customs-company-trends) <br>
- [UpKuaJing Homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Developer Portal](https://developer.upkuajing.com/) <br>
- [UpKuaJing API Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns one record per month and includes fee information when the API response provides it.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
