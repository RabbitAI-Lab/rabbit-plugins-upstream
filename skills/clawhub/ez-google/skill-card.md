## Description: <br>
ez-google provides agent-friendly Google Workspace CLI tools for Gmail, Calendar, Drive, Docs, Sheets, Slides, Contacts, and Chat through hosted OAuth. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[araa47](https://clawhub.ai/user/araa47) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users use this skill to let an agent inspect, create, update, send, and delete Google Workspace resources after OAuth authorization. It is suited for mailbox, calendar, document, spreadsheet, presentation, contact, Drive, and Chat automation tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad, persistent access to Gmail, Drive, Calendar, Docs, Sheets, Slides, Contacts, and Google Chat through a third-party OAuth flow. <br>
Mitigation: Review the Google consent screen carefully, prefer a dedicated or low-risk Google account, and revoke the OAuth grant when the work is complete. <br>
Risk: Write, delete, send, and bulk Gmail operations can change or remove user data at scale. <br>
Mitigation: Review proposed commands and queries before execution, and avoid `bulk-trash -y` unless the target query has been explicitly verified. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/araa47/skills/ez-google) <br>
- [Hosted OAuth service](https://ezagentauth.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and CLI text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Google OAuth authorization; command output may include Google Workspace data.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
