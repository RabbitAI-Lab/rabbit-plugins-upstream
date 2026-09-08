## Description:

Assistant Mail provides managed agent email for personal and small-team OpenClaw and Hermes use, with allowlist controls, consent gates, retention, send caps, mailbox ID access, and API-key authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[assistantmail](https://clawhub.ai/user/assistantmail)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and small-team operators use this skill to connect an agent to an Assistant Mail mailbox through MCP. The skill helps agents discover endpoint details, list mailboxes and messages, send or reply to email, manage approved recipients, and check usage under the service's allowlist and consent controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent with access to the Assistant Mail API key can read and manage the selected mailbox.

Mitigation: Install only when mailbox access is intended, keep the API key private, scope mailbox access carefully, and revoke or rotate the key when it is no longer needed.

Risk: Email sending or replies may reach unintended recipients if recipient controls are configured too broadly.

Mitigation: Use the service's recipient allowlist and consent controls, and review approved recipients before enabling outbound send behavior.

Risk: Mailbox email addresses may be mistaken for access credentials.

Mitigation: Treat the email address as a routing address only; require the correct mailboxId and a valid API key or JWT for mailbox operations.

## Reference(s):

- [Assistant Mail documentation](https://assistant-mail.ai/docs)
- [Assistant Mail ClawHub skill page](https://clawhub.ai/assistantmail/skills/assistant-mail)
- [Assistant Mail app](https://app.assistant-mail.ai/?utm_source=github&utm_medium=readme&utm_campaign=clawhub_readme_amplify)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls]

**Output Format:** [Markdown with inline shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes MCP tool names, environment variables, API-key handling notes, mailbox ID usage, and recipient allowlist guidance.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
