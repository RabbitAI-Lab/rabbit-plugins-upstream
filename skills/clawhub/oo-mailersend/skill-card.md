## Description:

MailerSend (mailersend.com). Use this skill for ANY MailerSend request -- reading, creating, and updating data. Whenever a task involves MailerSend, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate MailerSend through an OOMOL-connected account for reading account resources and sending transactional email.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path can execute a remote installer directly in the user's shell.

Mitigation: Review the oo CLI source and installation method before running the installer, and prefer the documented install guide when assessing the setup path.

Risk: The skill connects OOMOL to a MailerSend account through managed credentials.

Mitigation: Confirm that connecting OOMOL to MailerSend is acceptable before authorizing or repairing the account connection.

Risk: The send_email action sends real transactional email from the connected account.

Mitigation: Confirm the exact recipient, content, and purpose before allowing send_email to run.

## Reference(s):

- [MailerSend homepage](https://www.mailersend.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mailersend)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing MailerSend action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
