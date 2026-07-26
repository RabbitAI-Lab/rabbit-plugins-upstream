## Description: <br>
Gmail API integration with managed OAuth for reading, sending, and managing emails, threads, labels, and drafts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seanford](https://clawhub.ai/user/seanford) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to work with Gmail through Maton-managed OAuth, including reading messages and threads, creating or sending drafts, sending email, and modifying labels or trashing messages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read, send, modify, and trash Gmail messages through a third-party gateway. <br>
Mitigation: Use it only when Maton is trusted for proxied Gmail access and require manual review before sending mail, sending drafts, changing labels, or trashing messages. <br>
Risk: An exposed Maton API key can grant access to the configured Gmail integration. <br>
Mitigation: Store MATON_API_KEY as a private secret, avoid printing it in logs, and rotate it if exposure is suspected. <br>
Risk: If multiple Gmail connections exist, the default connection may not be the intended mailbox. <br>
Mitigation: Choose the intended Gmail connection explicitly with the Maton-Connection header before making requests. <br>


## Reference(s): <br>
- [ClawHub Gmail Skill](https://clawhub.ai/seanford/skills/gmail) <br>
- [Gmail API Overview](https://developers.google.com/gmail/api/reference/rest) <br>
- [Gmail Messages: list](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/list) <br>
- [Gmail Messages: send](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/send) <br>
- [Gmail Drafts: create](https://developers.google.com/gmail/api/reference/rest/v1/users.drafts/create) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with HTTP endpoints and Python or JavaScript code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, and an active Gmail OAuth connection through Maton.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
