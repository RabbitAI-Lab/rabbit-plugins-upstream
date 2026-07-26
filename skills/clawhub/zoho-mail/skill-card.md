## Description: <br>
Zoho Mail API integration with managed OAuth for sending, receiving, searching, and managing email messages, folders, labels, and attachments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent work with a connected Zoho Mail account through Maton-managed OAuth, including reading mail, sending replies, searching messages, and organizing folders and labels. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access sensitive email, folder, account, and organization information through the connected Zoho Mail account. <br>
Mitigation: Install only when Maton-mediated Zoho Mail access is acceptable, keep MATON_API_KEY out of shared logs, and remove the Maton connection when it is no longer needed. <br>
Risk: Write operations can send email or modify messages, folders, labels, and attachments. <br>
Mitigation: Confirm the target resource and intended effect with the user before every send, delete, move, label, folder, or attachment action. <br>
Risk: Multiple Zoho Mail connections can route actions to the wrong account if the connection is ambiguous. <br>
Mitigation: Use the Maton-Connection header when more than one active Zoho Mail connection exists. <br>


## Reference(s): <br>
- [Zoho Mail API Overview](https://www.zoho.com/mail/help/api/overview.html) <br>
- [Zoho Mail API Index](https://www.zoho.com/mail/help/api/) <br>
- [Email Messages API](https://www.zoho.com/mail/help/api/email-api.html) <br>
- [Getting Started with Zoho Mail API](https://www.zoho.com/mail/help/api/getting-started-with-api.html) <br>
- [Maton](https://maton.ai) <br>
- [Publisher Profile](https://clawhub.ai/user/byungkyu) <br>
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoho-mail) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown with API paths, JSON examples, and Python or JavaScript code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, and a connected Zoho Mail OAuth account.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
