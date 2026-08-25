## Description:

支持发送个性化邮件，自动追踪邮件打开、点击及回复数据，助力企业高效开展跨境客户触达与海外营销推广，适用于外贸开发、客户跟进与跨境私域运营。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External sales and marketing teams use this skill to send personalized outbound email through Upkuajing and review task-level delivery, open, click, read, and reply status. It supports foreign-trade customer outreach, cross-border ecommerce email marketing, and follow-up analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Email sending can incur charges through Upkuajing.

Mitigation: Confirm current pricing and get explicit user approval before sending email or creating a recharge order.

Risk: The skill reads or creates a local UPKUAJING_API_KEY and may store it in ~/.upkuajing/.env.

Mitigation: Treat the .env file and API key as secrets and avoid exposing them in prompts, logs, or shared outputs.

Risk: Outbound marketing email can be sent to multiple recipients through the provider API.

Mitigation: Review recipients, subject, content, and reply address with the user before executing a send request.

Risk: Exception reports may include request context for provider-side troubleshooting.

Mitigation: Only submit an error report after user confirmation and keep the context limited to what is needed for diagnosis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/upkuajing-email-tool-zh)
- [Upkuajing homepage](https://www.upkuajing.com)
- [Upkuajing API pricing](https://www.upkuajing.com/web/openapi/price.html)
- [邮件发送 API 参考](references/email-send-api.md)
- [邮件任务列表 API 参考](references/email-task-list-api.md)
- [邮件任务明细列表 API 参考](references/email-task-record-list-api.md)
- [Agent调用Skill异常上报 API 参考](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and an UPKUAJING_API_KEY; email sending can be billable.]

## Skill Version(s):

1.0.4 (source: server evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
