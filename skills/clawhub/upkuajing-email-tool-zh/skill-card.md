## Description: <br>
支持发送个性化邮件，自动追踪邮件打开、点击及回复数据，助力企业高效开展跨境客户触达与海外营销推广，适用于外贸开发、客户跟进与跨境私域运营。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and sales teams use this skill to send outbound business email through UpKuajing, then review task-level and recipient-level delivery, open, click, read, and reply status. It is suited to cross-border sales outreach, foreign trade prospecting, and follow-up workflows where users already intend to use UpKuajing's email platform. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends recipient lists, message content, and tracking data to a third-party email platform. <br>
Mitigation: Use it only when the user intends to use UpKuajing for email delivery, and avoid sending unnecessary personal or confidential data. <br>
Risk: Email sending and recharge order creation can incur costs. <br>
Mitigation: Confirm pricing and get explicit user approval before sending mail or creating payment-related orders. <br>
Risk: The API key may be stored locally in ~/.upkuajing/.env and can appear in command usage if handled carelessly. <br>
Mitigation: Protect the local environment file as a secret and avoid sharing command output that contains credentials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/upkuajing-email-tool-zh) <br>
- [UpKuajing homepage](https://www.upkuajing.com) <br>
- [UpKuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [UpKuajing OpenAPI endpoint](https://openapi.upkuajing.com) <br>
- [邮件发送 API 参考](references/email-send-api.md) <br>
- [邮件任务列表 API 参考](references/email-task-list-api.md) <br>
- [邮件任务明细列表 API 参考](references/email-task-record-list-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; paid email sending actions require explicit user confirmation before execution.] <br>

## Skill Version(s): <br>
1.0.2 (source: server evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
