## Description: <br>
Read and manage email via IMAP, including checking unread messages, fetching message content, searching mailboxes, and marking messages as read or unread. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mvarrieur](https://clawhub.ai/user/mvarrieur) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents with user-authorized mailbox access use this skill to inspect IMAP mailboxes, retrieve message details, search recent or filtered mail, and update read state for workflow automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles private mailbox contents and IMAP credentials. <br>
Mitigation: Install only for mailboxes the agent is allowed to access, use a dedicated app or Bridge-generated password, and ensure the local .env file is gitignored and chmod 600. <br>
Risk: Disabling certificate validation can expose remote IMAP sessions to interception. <br>
Mitigation: Keep certificate validation enabled for normal IMAP servers and only set IMAP_REJECT_UNAUTHORIZED=false for a trusted local ProtonMail Bridge. <br>
Risk: The example cron workflow can forward email summaries to an iMessage destination. <br>
Mitigation: Remove or replace the delivery target unless forwarding mailbox summaries to that destination is explicitly intended. <br>
Risk: Less-secure Gmail access weakens account protection. <br>
Mitigation: Use Gmail app passwords with two-factor authentication instead of less-secure app access. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mvarrieur/skills/imap-email) <br>
- [Publisher profile](https://clawhub.ai/user/mvarrieur) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration, guidance] <br>
**Output Format:** [JSON from the IMAP CLI, with Markdown setup and usage guidance in the skill documentation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-provided IMAP credentials and network access to the configured mail server; outputs may include private email metadata, snippets, message bodies, and attachment metadata.] <br>

## Skill Version(s): <br>
1.0.3 (source: ClawHub release metadata and skill.json; package.json is 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
