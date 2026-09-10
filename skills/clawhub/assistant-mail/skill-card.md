## Description:

Assistant Mail helps agents connect to managed email mailboxes through MCP using API key authentication, allowlists, consent controls, retention, and send caps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[assistantmail](https://clawhub.ai/user/assistantmail)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to configure agents for Assistant Mail mailbox access, message retrieval, replies, sending, recipient management, and usage checks through MCP.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API key exposure could allow mailbox operations through Assistant Mail.

Mitigation: Treat ASSISTANT_MAIL_API_KEY like a password, store it only in the agent runtime's secret mechanism, and rotate it if exposure is suspected.

Risk: Agent-accessible tools include sending, replying to, reading, and deleting mail-related data.

Mitigation: Review the exposed MCP tools before deployment and use allowlists, consent controls, and send caps to limit agent behavior.

Risk: Using the wrong mailboxId could direct operations at an unintended mailbox within the authorized account.

Mitigation: List mailboxes through the API, persist the intended mailboxId, and confirm it before send, read, update, or delete operations.

## Reference(s):

- [Assistant Mail documentation](https://assistant-mail.ai/docs)
- [ClawHub assistant-mail skill page](https://clawhub.ai/assistantmail/skills/assistant-mail)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls]

**Output Format:** [Markdown with inline shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes MCP server setup, environment variable guidance, mailbox identifiers, and tool-call examples.]

## Skill Version(s):

1.0.4 (source: evidence.release.version, released 2026-09-09T23:25:19Z)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
