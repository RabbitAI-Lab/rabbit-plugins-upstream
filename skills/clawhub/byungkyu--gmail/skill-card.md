## Description: <br>
Gmail API integration with managed OAuth for reading, sending, and managing emails, threads, labels, and drafts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to access a connected Gmail account through Maton-managed OAuth for message triage, drafting, sending, label and thread management, and profile lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Connected Gmail access can expose email content or modify messages, drafts, labels, and threads. <br>
Mitigation: Install only for accounts where Maton-mediated Gmail access is acceptable, use a dedicated or least-privilege Google account where possible, and confirm sends or modifications before execution. <br>
Risk: When multiple Gmail accounts are linked, requests can target the wrong mailbox. <br>
Mitigation: Specify the intended Maton connection whenever more than one Gmail account is connected. <br>
Risk: A retained Maton OAuth connection or API key can continue to authorize Gmail access. <br>
Mitigation: Protect MATON_API_KEY as a secret and revoke the Maton OAuth connection when it is no longer needed. <br>


## Reference(s): <br>
- [ClawHub Gmail Skill](https://clawhub.ai/byungkyu/skills/gmail) <br>
- [Gmail API Overview](https://developers.google.com/gmail/api/reference/rest) <br>
- [Gmail Messages: List](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/list) <br>
- [Gmail Messages: Send](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/send) <br>
- [Gmail Drafts: Create](https://developers.google.com/gmail/api/reference/rest/v1/users.drafts/create) <br>
- [Maton CLI Manual](https://cli.maton.ai/manual) <br>
- [Related API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, API calls, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, API paths, JSON payloads, and Python/JavaScript code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, and a Maton-managed Gmail OAuth connection.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
