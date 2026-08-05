## Description: <br>
B2B Outreach helps agents run outbound B2B workflows that collect Google Maps merchant leads, validate phone numbers, email addresses, and domains, send bulk email or SMS, and monitor delivery and reply status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sales, sourcing, export, and CRM teams use this skill to collect merchant prospects, validate contact data, send B2B outreach through email or SMS, and review campaign delivery status. It is intended for lawful outreach with appropriate permission, consent, and account balance controls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bulk email, SMS, and merchant harvesting can create legal, consent, deliverability, and reputation risk. <br>
Mitigation: Use the skill only with lawfully sourced contacts, clear permission or a compliant outreach basis, and reviewer-approved message content. <br>
Risk: Send, search, and validation operations can spend account balance. <br>
Mitigation: Confirm pricing and expected volume before paid operations, and require explicit user confirmation before executing billable sends, searches, or validation checks. <br>
Risk: Contact lists, message content, and validation targets are transmitted to UpKuaJing's API. <br>
Mitigation: Avoid unnecessary sensitive data, disclose the external processing path to users, and review data handling requirements before use. <br>
Risk: The required API key is stored in the user's UpKuaJing environment file and can authorize paid operations. <br>
Mitigation: Protect file access, avoid sharing the key, and rotate or revoke the key if it may have been exposed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/b2b-outreach) <br>
- [UpKuaJing homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [Detailed price description](https://www.upkuajing.com/web/openapi/price.html) <br>
- [Email Send API](references/email-send-api.md) <br>
- [Email Task List API](references/email-task-list-api.md) <br>
- [Email Task Record List API](references/email-task-record-list-api.md) <br>
- [SMS Send API](references/sms-send-api.md) <br>
- [SMS Task List API](references/sms-task-list-api.md) <br>
- [SMS Task Record List API](references/sms-task-record-list-api.md) <br>
- [Merchants Search API](references/merchants-search-api.md) <br>
- [Country List API](references/country-list-api.md) <br>
- [Province List API](references/province-list-api.md) <br>
- [City List API](references/city-list-api.md) <br>
- [Phone Validity API](references/validity-phone-api.md) <br>
- [Email Validity API](references/validity-email-api.md) <br>
- [Domain Validity API](references/validity-domain-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Guidance, API Calls] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces commands for Python scripts that send or query outreach tasks, validate contact data, search merchants, inspect account status, and configure the required API key.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md metadata and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
