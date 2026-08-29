## Description:

This skill sends bulk international SMS through Upkuajing, supports one-way or two-way messaging, and retrieves task and delivery-status details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External business users, marketers, sales teams, operators, and customer-support teams use this skill to send international SMS campaigns or notifications and review message task status and delivery records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores API keys in a local plaintext file at ~/.upkuajing/.env.

Mitigation: Keep the file private, prefer environment variables where appropriate, restrict local file permissions, and never share the key in prompts, logs, or reports.

Risk: SMS operations can expose recipient phone numbers, message content, account data, and billing activity to Upkuajing services.

Mitigation: Use only approved customer data, minimize sensitive content, and confirm the user trusts Upkuajing for the relevant recipient and account information.

Risk: Sending SMS messages and creating recharge orders can affect billing.

Mitigation: Check current pricing and obtain explicit user confirmation before any paid SMS send or recharge action.

Risk: Raw API logging, if enabled, can record request and response data locally.

Mitigation: Leave raw API logging disabled unless needed; if enabled, protect and redact logs before sharing or retaining them.

Risk: Optional error reports can include operational context from failed API calls.

Mitigation: Submit error reports only after user confirmation and exclude secrets, phone numbers, SMS content, and other customer data unless explicitly approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/upkuajing-sms-tool-zh)
- [Upkuajing homepage](https://www.upkuajing.com)
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html)
- [SMS send API reference](references/sms-send-api.md)
- [SMS task list API reference](references/sms-task-list-api.md)
- [SMS task record list API reference](references/sms-task-record-list-api.md)
- [Skill error report API reference](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; SMS send operations may incur charges and return task, request, billing, and delivery-status data.]

## Skill Version(s):

1.0.4 (source: SKILL.md metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
