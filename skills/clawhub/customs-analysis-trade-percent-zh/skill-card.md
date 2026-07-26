## Description: <br>
This skill queries Upkuajing customs data for company-level trade share by HS code, with export/import country type and recent-month filters. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Trade analysts, sourcing agents, and market researchers use this skill to identify leading companies for a product, analyze market concentration, assess supplier competition, and discover potential trade partners from customs trade data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill calls an external Upkuajing API and paid lookups can consume API balance. <br>
Mitigation: Tell the user a query may incur fees, obtain separate explicit confirmation before paid calls, and use the pricing command or pricing page for current costs. <br>
Risk: The Upkuajing API key is sensitive and may be stored locally in ~/.upkuajing/.env. <br>
Mitigation: Restrict local file permissions, prefer environment variables where appropriate, and avoid sharing the key in prompts, logs, or support messages. <br>
Risk: Recharge and account-management flows may open payment or account URLs. <br>
Mitigation: Review Upkuajing payment and account URLs before opening them, and continue only after the user confirms the payment or account action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-analysis-trade-percent-zh) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing developer platform](https://developer.upkuajing.com/) <br>
- [Upkuajing API pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [Trade percent API reference](references/customs-analysis-trade-percent-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON API responses with fee metadata and concise natural-language guidance before paid calls] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python, httpx, and UPKUAJING_API_KEY; API calls may consume paid balance after user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
