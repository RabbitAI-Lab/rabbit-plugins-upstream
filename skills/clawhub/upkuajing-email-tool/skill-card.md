## Description:

Run bulk corporate cold-email campaigns and monitor delivery, open, click, and read status through UpKuaJing Open Platform scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External sales, export, sourcing, and cross-border commerce teams use this skill to send UpKuaJing email campaigns, review campaign task lists, and inspect recipient-level status records. Agents can also guide account setup, balance checks, and paid-send confirmation before executing fee-bearing sends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send paid emails through UpKuaJing.

Mitigation: Review recipient lists and costs, then require explicit user confirmation before any fee-bearing email send.

Risk: The skill depends on a local UPKUAJING_API_KEY.

Mitigation: Keep the API key private, store it only in the expected environment or local configuration, and avoid exposing it in prompts, logs, or reports.

Risk: Error reports can include troubleshooting context from failed API calls.

Mitigation: Ask for user confirmation before reporting abnormal responses and avoid including secrets or customer data in report context.

Risk: The release advertises lead-finding language that is not implemented by these scripts.

Mitigation: Present this skill as an email sending and tracking integration, not as a standalone lead discovery tool.

## Reference(s):

- [Email Send API](references/email-send-api.md)
- [Email Task List API](references/email-task-list-api.md)
- [Email Task Record List API](references/email-task-record-list-api.md)
- [Skill Error Report API](references/skill-error-report-api.md)
- [UpKuaJing Homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [UpKuaJing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html)
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/upkuajing-email-tool)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, json, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; paid email sends require explicit user confirmation before execution.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
