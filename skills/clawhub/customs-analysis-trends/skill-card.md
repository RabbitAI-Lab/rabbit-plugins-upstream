## Description: <br>
Retrieves monthly import and export trend data for a specified HS code, including trade counts, quantities, weights, amounts, buyer counts, and seller counts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External trade analysts, supply chain managers, and market researchers use this skill to analyze recent import and export trends for specific HS codes, compare product flow over time, and monitor seasonal or market changes across global customs data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts UpKuaJing using a metered API key, and normal query or top-up flows can incur fees. <br>
Mitigation: Confirm every fee-incurring query or top-up flow explicitly before execution, and use the published pricing page or price_info helper for current pricing. <br>
Risk: The API key may be stored in plaintext at ~/.upkuajing/.env. <br>
Mitigation: Prefer environment-variable injection where possible, or restrict file permissions on ~/.upkuajing/.env and avoid sharing the file. <br>
Risk: The skill may perform automatic version checks against UpKuaJing during API use. <br>
Mitigation: Review this outbound check before deployment in restricted environments and ensure users understand that UpKuaJing network access is part of normal operation. <br>


## Reference(s): <br>
- [Customs Analysis Trends API Reference](references/customs-analysis-trends-api.md) <br>
- [UpKuaJing Homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/customs-analysis-trends) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON API results with concise natural-language guidance for setup, pricing, and confirmation steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; API calls may incur fees and return fee details with the data.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
