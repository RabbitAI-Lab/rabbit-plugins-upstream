## Description:

Send global bulk SMS with two-way replies, monitor delivery status through task reports, and support cross-border outreach campaigns for business users.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External business, marketing, sales, operations, and support teams use this skill to send paid SMS messages, inspect SMS task status, and review delivery records through the UpKuaJing Open Platform API. Agents should confirm paid sends with the user and handle recipient data, message bodies, and API keys as sensitive data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SMS sends can incur fees and contact external recipients.

Mitigation: Confirm the recipient list, message content, and cost-bearing action with the user before running any SMS send command.

Risk: SMS recipient data, message bodies, and API keys are sensitive.

Mitigation: Keep UPKUAJING_API_KEY private, store it only in the expected environment or ~/.upkuajing/.env file, and avoid including sensitive values in logs or error reports.

Risk: Error reports can accidentally include sensitive request or response details.

Mitigation: Ask for user confirmation before reporting an abnormal API call and redact phone numbers, message bodies, tokens, and other sensitive data from the report context.

## Reference(s):

- [SMS Send API](references/sms-send-api.md)
- [SMS Task List API](references/sms-task-list-api.md)
- [SMS Task Record List API](references/sms-task-record-list-api.md)
- [Skill Error Report API](references/skill-error-report-api.md)
- [UpKuaJing Homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [UpKuaJing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html)
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/upkuajing-sms-tool)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; SMS sends can incur fees and should require explicit user confirmation.]

## Skill Version(s):

1.0.4 (source: server evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
