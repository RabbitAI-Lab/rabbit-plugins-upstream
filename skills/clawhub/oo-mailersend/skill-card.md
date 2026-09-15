## Description:

Enables agents to handle MailerSend read, create, update, and transactional email tasks through the OOMOL oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect MailerSend schemas, read MailerSend account data, and send transactional email through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes direct execution of remote installer scripts.

Mitigation: Review the installer path before installing, prefer verified oo CLI releases or package-manager installs, and use version and integrity checks where available.

Risk: The send_email action sends transactional email and can affect external recipients.

Mitigation: Confirm exact recipients, content, and sending account before allowing send_email to run.

## Reference(s):

- [ClawHub MailerSend Skill](https://clawhub.ai/oomol/skills/oo-mailersend)
- [MailerSend Homepage](https://www.mailersend.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions return JSON data with execution metadata when run through the oo CLI.]

## Skill Version(s):

1.0.3 (source: artifact frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
