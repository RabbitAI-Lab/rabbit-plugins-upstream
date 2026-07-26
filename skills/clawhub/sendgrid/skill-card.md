## Description: <br>
SendGrid API integration with managed OAuth for sending email, managing contacts, templates, suppressions, statistics, sender identities, unsubscribe groups, and SendGrid API keys. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to connect an agent to SendGrid through Maton for transactional or marketing email workflows, contact and list management, template work, suppression handling, sender administration, statistics review, and API key management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Email sending delivers messages to real recipients. <br>
Mitigation: Confirm recipients, sender, subject, and content with the user before sending. <br>
Risk: Write operations can change SendGrid contacts, lists, templates, sender identities, suppressions, unsubscribe groups, OAuth connections, or API keys. <br>
Mitigation: Require explicit user approval for each create, update, or delete request and state the target resource and intended effect. <br>
Risk: API key management can create long-lived credentials that persist beyond the current session. <br>
Mitigation: Only perform API key management when explicitly requested, and never display created key values. <br>
Risk: Suppression removals can resume mail to addresses that previously bounced, blocked, failed validation, unsubscribed, or reported spam. <br>
Mitigation: Keep suppression removals narrow and deliberate, and verify the affected addresses with the user before execution. <br>


## Reference(s): <br>
- [SendGrid Skill on ClawHub](https://clawhub.ai/byungkyu/skills/sendgrid) <br>
- [SendGrid API Documentation](https://www.twilio.com/docs/sendgrid/api-reference) <br>
- [Mail Send API](https://www.twilio.com/docs/sendgrid/api-reference/mail-send) <br>
- [Marketing Campaigns API](https://www.twilio.com/docs/sendgrid/api-reference/contacts) <br>
- [Suppressions Overview](https://www.twilio.com/docs/sendgrid/api-reference/suppressions-suppressions) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline JSON, Python, JavaScript, and shell examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MATON_API_KEY and an active SendGrid OAuth connection through Maton for live API calls.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
