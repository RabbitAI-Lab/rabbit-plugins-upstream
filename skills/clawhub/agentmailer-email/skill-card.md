## Description:

Read, search, triage, draft, send, reply to, forward, label, or delete email in an AgentMailer inbox through MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentmailer](https://clawhub.ai/user/agentmailer)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent read, search, triage, draft, send, reply to, forward, label, and delete email in an AgentMailer inbox while requiring explicit confirmation for outbound and destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Outbound or scheduled email actions can contact external recipients.

Mitigation: Before sending, replying, forwarding, or sending a draft, restate the sender inbox, recipients, subject, and message content and obtain explicit confirmation in the current conversation.

Risk: Deleting messages, threads, or drafts can remove email data or cancel scheduled delivery.

Mitigation: Resolve the exact target before deletion, obtain explicit confirmation, and explain when deleting a draft also cancels a scheduled send.

Risk: Inbox contents, attachments, download URLs, credentials, and tokens can be sensitive.

Mitigation: Fetch attachments only when needed, treat download URLs as short-lived and sensitive, and keep credentials, authorization headers, and raw tokens out of prompts and tool output.

## Reference(s):

- [Email tool reference](references/email-tools.md)
- [AgentMailer MCP service](https://api.agentmailer.ai/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Guidance]

**Output Format:** [Markdown or plain text with structured confirmation details for email actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use AgentMailer MCP operations for inbox reads, drafts, sends, labels, attachments, and deletions according to the user's confirmed request.]

## Skill Version(s):

0.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
