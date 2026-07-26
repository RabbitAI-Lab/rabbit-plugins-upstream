## Description: <br>
查询跨境魔方海关数据中的企业基础贸易统计，包括交易次数、重量、数量、金额、合作伙伴数量和贸易时间范围。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External trade teams, analysts, and researchers use this skill to query a paid Upkuajing customs API by company ID and company role, then review aggregate trade scale and partner-network indicators for supplier screening, buyer validation, and trade intelligence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid API calls can incur charges for each company trade-statistics query. <br>
Mitigation: Tell the user the query is paid, retrieve current pricing when needed, and wait for a separate explicit confirmation before running a cost-incurring script. <br>
Risk: The API key is stored in ~/.upkuajing/.env and is used for authenticated requests. <br>
Mitigation: Keep the file private, avoid exposing the key in chat or logs, and rotate the key if it may have been shared. <br>
Risk: When account balance is insufficient, the skill can create a recharge order and return a payment URL. <br>
Mitigation: Create recharge orders only after the user asks to proceed, and have the user verify the payment page before paying. <br>
Risk: The skill performs a small automatic version check and cache update under ~/.upkuajing. <br>
Mitigation: Disclose this network and local-cache behavior to users who require strict egress or filesystem controls. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-company-stats-zh) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing developer platform](https://developer.upkuajing.com/) <br>
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [Company trade statistics API reference](references/customs-company-stats-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [JSON API responses with concise human-facing guidance and direct Python command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires UPKUAJING_API_KEY and explicit user confirmation before paid API calls.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
