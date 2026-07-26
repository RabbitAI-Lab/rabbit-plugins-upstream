## Description: <br>
Lightweight email manager with IMAP/SMTP support, advanced search, folder management, and attachment detection. Works with Zoho, Gmail, Outlook, and any IMAP/SMTP provider. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jorgermp](https://clawhub.ai/user/jorgermp) <br>

### License/Terms of Use: <br>
ISC <br>


## Use Case: <br>
Developers and email power users use this skill to manage IMAP/SMTP mailboxes from an agent-assisted CLI, including sending mail, reading and searching messages, listing folders, moving messages, and checking attachment details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires mailbox credentials and can access the target mailbox. <br>
Mitigation: Use a dedicated app password or low-risk mailbox, and revoke the credential when the skill is no longer needed. <br>
Risk: The security evidence flags weakened IMAP certificate checks. <br>
Mitigation: Remove the rejectUnauthorized: false IMAP option before use. <br>
Risk: The skill can directly send email and move mailbox messages. <br>
Mitigation: Require manual confirmation before any send or move operation. <br>
Risk: Dependency versions need review before use. <br>
Mitigation: Review dependency versions and install with a lockfile. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jorgermp/skills/email-manager-lite) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [Zoho app passwords](https://accounts.zoho.eu/home#security/apppasswords) <br>
- [Google app passwords](https://myaccount.google.com/apppasswords) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and CLI output descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires mailbox credentials through EMAIL_USER and EMAIL_PASS and provider-specific IMAP/SMTP configuration.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata; artifact frontmatter, package.json, and changelog report 0.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
