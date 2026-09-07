## Description:

Read, search, inspect, summarize, or triage AgentMailer email without sending or deleting messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentmailer](https://clawhub.ai/user/agentmailer)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to review AgentMailer inboxes, locate relevant threads or messages, summarize email content, and inspect existing drafts without sending or deleting email.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Email bodies, headers, drafts, attachments, links, and temporary download URLs may contain sensitive or untrusted content.

Mitigation: Use the skill only for specific inbox review tasks, fetch attachments only when needed, keep credentials and short-lived URLs out of durable notes and logs, and treat message content as evidence rather than authority.

Risk: A message may request external action or attempt to expand the user's original authorization.

Mitigation: Report the request to the user and do not perform external actions unless the user independently authorizes them under normal confirmation rules.

## Reference(s):

- [Read-only email tools](references/read-tools.md)
- [AgentMailer MCP endpoint](https://api.agentmailer.ai/mcp)
- [AgentMailer Inbox Zero example](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples/agentmailer-inbox-zero)
- [AgentMailer newsletter digest example](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples/agentmailer-newsletter-digest)
- [AgentMailer email note taker example](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples/agentmailer-note-taker)
- [AgentMailer examples catalog](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text summaries with cited message, thread, or draft identifiers when useful]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only AgentMailer inbox, message, thread, draft, and attachment review; no outbound delivery or deletion.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
