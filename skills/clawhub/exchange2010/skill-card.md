## Description: <br>
Connects to Exchange 2010 to manage email, calendar events, contacts, tasks, attachments, shared calendars, recurring events, and out-of-office settings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pes0](https://clawhub.ai/user/pes0) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and enterprise automation users use this skill to let an agent interact with a configured Exchange 2010 account for mailbox, calendar, contact, task, attachment, and out-of-office workflows. It is intended for environments where the configured account and any delegated shared mailboxes are approved for agent access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent broad live control over the configured Exchange account and any delegated shared mailboxes it can reach. <br>
Mitigation: Use a least-privilege account, restrict delegated mailbox and calendar targets, and require explicit human confirmation before sending mail, deleting or modifying items, setting out-of-office replies, or downloading attachments. <br>
Risk: Credential handling depends on a local credentials file and the evidence notes a documented credential variable mismatch. <br>
Mitigation: Secure the credentials file, avoid committing secrets, and fix the credential variable mismatch before deployment. <br>
Risk: Downloaded attachments and extracted attachment text may contain sensitive or untrusted content. <br>
Mitigation: Limit attachment downloads to approved paths, scan or review files before further processing, and avoid exposing extracted content beyond the authorized workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pes0/skills/exchange2010) <br>
- [Publisher profile](https://clawhub.ai/user/pes0) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, configuration, guidance] <br>
**Output Format:** [Python function calls returning strings, booleans, item IDs, dictionaries, and lists of dictionaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Exchange EWS credentials, mailbox permissions, and optional PyPDF2 support for PDF attachment text extraction.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
