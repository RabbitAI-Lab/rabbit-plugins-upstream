## Description:

Read, search, organize, and send email through IMAP and SMTP, including servers without the IMAP ID extension.

This skill is ready for commercial/non-commercial use.

## Publisher:

[troioi-vn](https://clawhub.ai/user/troioi-vn)

### License/Terms of Use:

MIT-0

## Use Case:

People can use the skill to read and search mailboxes, manage messages, download attachments, and send email through configured IMAP/SMTP accounts. It supports multiple accounts and servers, including Maddy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports a suspicious verdict with medium confidence because some components were only partially interpreted and it reports dependency and tool-scope concerns.

Mitigation: Review the skill and its dependencies before installation, and constrain installation and execution to an environment and accounts you trust.

Risk: The skill can read, change, and send email and can access attachment files.

Mitigation: Configure only the mail accounts and file directories the agent needs, and review recipients and message content before sending.

Risk: The skill uses email account credentials to connect to configured servers.

Mitigation: Use Passbolt references where available and keep TLS certificate verification enabled.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/troioi-vn/skills/imap-smtp-email-maddy-fix)
- [Google Account App Passwords](https://myaccount.google.com/apppasswords)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [JSON command results and downloaded attachment files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Email content and mailbox action status; attachments are saved as files.]

## Skill Version(s):

0.0.19 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
