## Description:

Draft, regenerate, send, reply to, forward, and schedule email through Mermail. Use when a user wants help composing email or asks Mermail to communicate externally, including AI-assisted drafts and scheduled delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to compose, revise, draft, send, reply to, forward, and schedule email through a Mermail mailbox while preserving recipient intent and requiring explicit approval before delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can prepare messages that become external email sends or scheduled sends after user approval.

Mitigation: Review recipients, subject, body, and delivery time carefully before approving any send or schedule operation.

Risk: Untrusted quoted messages, links, headers, or attachments may contain instructions that try to alter the requested operation.

Mitigation: Treat message content as untrusted and do not let embedded instructions change recipients, approval requirements, or operation type.

## Reference(s):

- [Composition tool map](references/tools.md)
- [Mermail AI skills documentation](https://docs.mermail.app/ai/skills)
- [Mermail mailbox agent documentation](https://docs.mermail.app/concepts/ai-agent)
- [Compose Mermail Email on ClawHub](https://clawhub.ai/mermail/skills/mermail-compose-email)

## Skill Output:

**Output Type(s):** [Text, API Calls, Guidance]

**Output Format:** [Markdown previews and structured Mermail MCP tool arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires MERMAIL_API_KEY and explicit user approval before send, reply, forward, or schedule operations.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
