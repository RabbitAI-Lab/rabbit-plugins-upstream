## Description: <br>
核验邮箱地址的真实可用状态，逐条返回邮箱验证结果以及判定原因，清理无效邮箱数据，降低外贸邮件群发退信概率，完成邮件列表合规清洗。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales, recruiting, marketing, procurement, and CRM data teams use this skill to validate email address status before outreach, list cleaning, supplier checks, or candidate screening. It helps reduce bounce risk by returning per-address validation status and reason data from Upkuajing's external API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Email addresses submitted for validation are sent to Upkuajing's external API. <br>
Mitigation: Confirm the user is comfortable sharing the email addresses with Upkuajing before running validation. <br>
Risk: API calls may incur paid usage. <br>
Mitigation: Disclose that validation is billable and get explicit user confirmation before making cost-incurring calls. <br>
Risk: The API key may be stored locally in ~/.upkuajing/.env. <br>
Mitigation: Keep the credential file private and do not expose the API key in responses, logs, or shared files. <br>
Risk: If API logging is enabled, request and response payloads can be stored locally. <br>
Mitigation: Leave API logging disabled unless local payload retention is intentional and the logs are protected. <br>
Risk: Recharge workflows may return payment URLs. <br>
Mitigation: Review payment URLs before opening them and let the user complete payment directly. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/email-validity-check-zh) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing API pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [Email validity API reference](references/email-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; successful validation results include total count, per-email status and reason data, and fee information.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
