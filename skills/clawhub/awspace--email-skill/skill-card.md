## Description:

Email management and automation for sending messages with attachments across SMTP providers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[awspace](https://clawhub.ai/user/awspace)

### License/Terms of Use:

MIT

## Use Case:

Developers and OpenClaw users use this skill to configure SMTP credentials and send plain text or HTML email, including CC, BCC, test messages, and file attachments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send workspace files and sensitive text to external recipients.

Mitigation: Require manual review of recipients, message body, and attachments before sending.

Risk: SMTP credentials may be exposed if stored in a workspace configuration file.

Mitigation: Prefer environment variables or a secret manager, and use a dedicated low-privilege sending account.

Risk: Email transport can be weakened if TLS or SSL is disabled.

Mitigation: Keep TLS or SSL enabled for SMTP connections.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/awspace/skills/email-skill)
- [Google Account Security](https://myaccount.google.com/security)
- [OpenClaw Documentation](https://docs.openclaw.ai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples, shell commands, Python snippets, and JSON command output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python 3 and configured SMTP credentials.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
