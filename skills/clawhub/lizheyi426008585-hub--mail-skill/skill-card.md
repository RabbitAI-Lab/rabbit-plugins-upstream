## Description: <br>
Full access to Exchange 2010/2013 EWS for managing emails, folders, attachments, calendar events, contacts, tasks, and out-of-office settings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lizheyi426008585-hub](https://clawhub.ai/user/lizheyi426008585-hub) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and developers use this skill to let an agent work with Exchange 2010/2013 mailboxes, calendars, contacts, tasks, attachments, and out-of-office settings through EWS. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires broad Exchange mailbox authority and handles live mailbox credentials. <br>
Mitigation: Install only from a trusted publisher, use a least-privilege mailbox where possible, protect the .env.credentials file, and avoid reusing non-Exchange passwords. <br>
Risk: The skill can send mail, modify mailbox data, and manage calendar, task, contact, and out-of-office state. <br>
Mitigation: Require explicit user confirmation before sending mail or making Exchange changes. <br>
Risk: Attachment downloads from untrusted senders may expose unsafe files until filename sanitization is fixed. <br>
Mitigation: Download attachments only from trusted messages and keep downloads in a restricted safe directory. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lizheyi426008585-hub/skills/mail-skill) <br>
- [Publisher profile](https://clawhub.ai/user/lizheyi426008585-hub) <br>
- [Artifact skill documentation](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Text, Code, Files, Configuration] <br>
**Output Format:** [Python function calls returning mailbox data, calendar data, contact data, task data, status strings, and downloaded attachment files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires live Exchange credentials and can read, send, update, or delete Exchange data.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter reports 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
