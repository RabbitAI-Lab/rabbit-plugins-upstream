## Description: <br>
Queries UpKuajing customs company product-list data so an agent can retrieve product names, trade counts, amounts, quantities, weights, trade share, pagination cursors, and related HS codes for product portfolio analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External trade teams and agents use this skill to inspect a company's traded product list, quantify product-level trade activity, and connect products to HS codes for market analysis and competitor tracking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid API calls can incur charges for each product-list query page. <br>
Mitigation: Tell the user the query is paid and wait for explicit confirmation in a separate message before running the query. <br>
Risk: The API key may be stored in a local plaintext dotfile. <br>
Mitigation: Use the environment variable when possible, restrict access to the local credentials file, and avoid sharing command output that includes secrets. <br>
Risk: Recharge order creation can produce a payment link. <br>
Mitigation: Only create recharge orders when the user asks, present the returned payment URL for user action, and continue only after the user confirms payment. <br>
Risk: The helper performs an automatic version check against the UpKuajing API service. <br>
Mitigation: Install only if this outbound version check is acceptable for the deployment environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-company-product-list-zh) <br>
- [公司贸易产品列表 API 参考](references/customs-company-product-list-api.md) <br>
- [UpKuajing homepage](https://www.upkuajing.com) <br>
- [UpKuajing developer platform](https://developer.upkuajing.com/) <br>
- [UpKuajing API pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [JSON responses with product-list data and fee information, plus concise user guidance before paid actions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; query parameters are passed as a JSON string to the script.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
