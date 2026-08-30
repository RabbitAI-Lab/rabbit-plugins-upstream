## Description:

B2B outreach toolkit for sending bulk cold email and global SMS, harvesting Google Maps merchant leads, validating contact information, and monitoring outreach delivery status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External sales, export, trading, sourcing, and growth teams use this skill to collect business leads, validate contact channels, send outreach, and review delivery or reply status. It is intended for authorized B2B outreach workflows where users confirm applicable anti-spam, privacy, SMS, and platform requirements before use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bulk email, SMS, and merchant harvesting can be misused or can violate anti-spam, SMS, privacy, or platform rules.

Mitigation: Use only for authorized outreach with appropriate consent or lawful basis, and confirm applicable rules before collecting contacts or sending messages.

Risk: Contact data, message content, and optional error-report details may be sent to UpKuaJing APIs.

Mitigation: Review recipients, message content, and any error-report payload before execution, and avoid sending sensitive or unnecessary personal data.

Risk: Send, search, and validation actions may incur fees.

Mitigation: Confirm pricing and obtain explicit user approval before running billable operations.

Risk: The skill performs a version check that security evidence describes as under-disclosed.

Mitigation: Review network behavior before installation and account for outbound requests to UpKuaJing services during API use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/b2b-outreach)
- [Publisher Profile](https://clawhub.ai/user/upkuajing)
- [UpKuaJing Homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [UpKuaJing Pricing](https://www.upkuajing.com/web/openapi/price.html)
- [Email Send API](references/email-send-api.md)
- [Email Task List API](references/email-task-list-api.md)
- [Email Task Record List API](references/email-task-record-list-api.md)
- [SMS Send API](references/sms-send-api.md)
- [SMS Task List API](references/sms-task-list-api.md)
- [SMS Task Record List API](references/sms-task-record-list-api.md)
- [Merchants Search API](references/merchants-search-api.md)
- [Country List API](references/country-list-api.md)
- [Province List API](references/province-list-api.md)
- [City List API](references/city-list-api.md)
- [Phone Validity API](references/validity-phone-api.md)
- [Email Validity API](references/validity-email-api.md)
- [Domain Validity API](references/validity-domain-api.md)
- [Skill Error Report API](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; send, search, and validation operations may incur fees and require user confirmation.]

## Skill Version(s):

1.0.1 (source: server release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
