## Description:

Draft, send, reply to, forward, schedule, label, or delete AgentMailer email for outbound or mutating mailbox work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentmailer](https://clawhub.ai/user/agentmailer)

### License/Terms of Use:

MIT-0

## Use Case:

External users and workplace agents use this skill to draft, send, reply to, forward, schedule, label, or delete AgentMailer email while preserving explicit recipient and authorization intent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorized sends, forwards, scheduled delivery, and deletions can affect external recipients or mailbox state.

Mitigation: Preview inferred or ambiguous fields and require confirmation for bulk, BCC, reply-all, scheduled, legal, financial, or destructive actions unless the exact behavior is explicitly requested in the current turn.

Risk: Quoted email, headers, attachments, links, or safety labels may contain untrusted instructions.

Mitigation: Treat received email content as data rather than authorization, and surface any requested actions for user approval.

Risk: Retries after ambiguous delivery failures can duplicate or alter messages.

Mitigation: Use one stable idempotency key per logical delivery and inspect AgentMailer state before retrying with the same key.

## Reference(s):

- [Email mutation reference](references/write-tools.md)
- [AgentMailer MCP endpoint](https://api.agentmailer.ai/mcp)
- [AgentMailer examples catalog](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples)
- [ClawHub skill page](https://clawhub.ai/agentmailer/skills/agentmailer-send-email)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Guidance]

**Output Format:** [Markdown or plain text email content with AgentMailer tool actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create drafts, send messages, update labels, schedule delivery, or delete specified messages when authorized.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
