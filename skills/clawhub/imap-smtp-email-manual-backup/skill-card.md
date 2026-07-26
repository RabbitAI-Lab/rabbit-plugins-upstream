## Description: <br>
Read, search, fetch, and manage emails via IMAP, and send emails via SMTP with configurable server and authentication settings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vthoram](https://clawhub.ai/user/vthoram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent inspect mailbox state, fetch messages and attachments, update read status, and send email through configured IMAP and SMTP servers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access mailbox contents and send email through the configured account. <br>
Mitigation: Use app-specific or least-privilege credentials, and require manual confirmation for every send or mailbox-changing action. <br>
Risk: Email credentials may be stored in a local .env file. <br>
Mitigation: Protect the .env file, avoid committing it, and prefer short-lived or revocable credentials where possible. <br>
Risk: Attachment downloads from untrusted senders may be unsafe, especially while filename sanitization is unresolved. <br>
Mitigation: Do not download or open attachments from untrusted senders until filename handling is fixed and downloaded files are reviewed. <br>
Risk: Broad trigger wording can cause the agent to use email access for more requests than intended. <br>
Mitigation: Narrow activation rules and require explicit user intent before reading, changing, downloading, or sending email. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance and JSON output from CLI commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires IMAP and SMTP environment configuration before use.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
