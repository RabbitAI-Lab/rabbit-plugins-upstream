## Description:

Automates SMTP email sending with provider presets, plain-text or HTML bodies, attachments, TLS/SSL configuration, recipient handling, and delivery-status output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operations teams, and workflow owners use this skill to send transactional, report, alert, or batch-notification emails through SMTP from an agent workflow after reviewing recipients, message content, attachments, and credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can transmit recipients, message bodies, and attachments to external SMTP services.

Mitigation: Confirm the recipient lists, body content, attachments, and sending account manually before each send, especially for batch or alert workflows.

Risk: SMTP credentials may be exposed if stored in plaintext configuration files.

Mitigation: Prefer environment variables or a secrets manager, keep credential files out of version control, and rotate credentials if exposure is suspected.

Risk: The skill requests broad agent tools for reading files and executing actions around email delivery.

Mitigation: Install only in environments where the agent is permitted to read attachment files and send email, and review the skill before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/email-skill)
- [Google account security and app passwords](https://myaccount.google.com/security)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SMTP configuration examples, recipient and attachment instructions, and delivery-result structures.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
