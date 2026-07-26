## Description: <br>
Queries monthly customs trade trend details for a company by company ID and optional filters, returning trade count, quantity, weight, and amount over time. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External trade teams, analysts, and supply-chain managers use this skill to analyze company-level customs trade patterns, monitor seasonal changes, and track long-term import/export activity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a paid external customs-data API, so queries and account actions can incur charges. <br>
Mitigation: Tell the user when an operation may cost money, use the pricing helper or pricing page for current rates, and wait for explicit confirmation before paid calls. <br>
Risk: The API key may be stored locally in ~/.upkuajing/.env. <br>
Mitigation: Keep the local environment file private, avoid sharing the key, and consider tightening file permissions before use. <br>
Risk: Recharge and account-management helpers can create payment flows or expose account balance information. <br>
Mitigation: Review account and recharge actions with the user before running them, and only open payment flows when the user intends to proceed. <br>


## Reference(s): <br>
- [公司贸易趋势 API 参考](references/customs-company-trends-api.md) <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-company-trends-zh) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing developer portal](https://developer.upkuajing.com/) <br>
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, JSON] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; paid API calls may return fee and balance details.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
