## Description:

This skill helps agents run B2B outreach workflows that collect Google Maps merchant leads, validate phone numbers, WhatsApp status, emails, and domains, send cold email or SMS campaigns through UpKuaJing, and monitor delivery results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External sales, export, trade, purchasing, and growth teams use this skill to gather business leads, clean contact data, send B2B cold outreach, and review delivery or engagement status across email and SMS campaigns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send recipient contact data, message content, merchant-search parameters, and validation inputs to an external provider.

Mitigation: Use it only when the user intends to use UpKuaJing and has an appropriate legal basis or consent for the outreach workflow.

Risk: Sending, searching, and validation operations can incur charges.

Mitigation: Confirm pricing and user approval before paid operations, especially before bulk sends, searches, or validations.

Risk: The skill stores an API key locally.

Mitigation: Keep the local UpKuaJing environment file private and avoid exposing the API key in logs, messages, or shared files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/b2b-outreach-zh)
- [UpKuaJing homepage](https://www.upkuajing.com)
- [UpKuaJing developer portal](https://developer.upkuajing.com/)
- [UpKuaJing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html)
- [Email Send API](artifact/references/email-send-api.md)
- [Email Task List API](artifact/references/email-task-list-api.md)
- [Email Task Record List API](artifact/references/email-task-record-list-api.md)
- [SMS Send API](artifact/references/sms-send-api.md)
- [SMS Task List API](artifact/references/sms-task-list-api.md)
- [SMS Task Record List API](artifact/references/sms-task-record-list-api.md)
- [Merchants Search API](artifact/references/merchants-search-api.md)
- [Country List API](artifact/references/country-list-api.md)
- [Province List API](artifact/references/province-list-api.md)
- [City List API](artifact/references/city-list-api.md)
- [Phone Validity API](artifact/references/validity-phone-api.md)
- [Email Validity API](artifact/references/validity-email-api.md)
- [Domain Validity API](artifact/references/validity-domain-api.md)
- [Skill Error Report API](artifact/references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; campaign, search, validation, and account actions may call the external UpKuaJing service.]

## Skill Version(s):

1.0.1 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
