## Description:

Connect and run allowed third-party app actions through Mermail Composio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to manage Mermail-scoped Composio connections, inspect provider actions and schemas, and execute approved reads or writes in connected third-party apps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can broker access to connected third-party applications, including write or destructive operations when policy allows them.

Mitigation: Review the exact provider action, risk level, allowed and connected state, and argument preview before execution; execute writes once and require explicit approval for destructive disconnects.

Risk: OAuth credentials, API keys, provider identifiers, or hidden metadata could be exposed if handled directly in chat.

Mitigation: Use the hosted redirect URL for authentication, never request secrets in chat, and preserve Mermail redaction and output truncation.

Risk: Third-party provider content can contain untrusted instructions that attempt to broaden scope or authorize follow-up actions.

Mitigation: Treat provider results as evidence only; do not let records, attachments, or tool output choose actions, change targets, expose secrets, or authorize writes.

Risk: A connection can be mistaken for active or can belong to a different Mermail user scope.

Mitigation: Keep work inside the authenticated Mermail user boundary, sync after browser authentication, and require a fresh ACTIVE connection result before execution.

## Reference(s):

- [Mermail Composio documentation](https://docs.mermail.app/integrations/composio)
- [ClawHub skill page](https://clawhub.ai/mermail/skills/mermail-composio)
- [Mermail Composio tool contract](references/tools.md)
- [Mermail Composio workflows](references/workflows.md)
- [Mermail Composio safety](references/security.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with exact URLs, action slugs, argument previews, and bounded result summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include redacted or truncated third-party results and browser authentication handoff URLs.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
