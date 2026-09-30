## Description:

Helps agents send postal mail and manage inbound mail through mailbox.bot, including human-approved mailbox actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arbengine](https://clawhub.ai/user/arbengine)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let agents quote and send letters or postcards, search inbound mail, and propose mailbox actions for human approval.

### Deployment Geography for Use:

Global; physical agent mailboxes are located in California, and inbound forwarding requires a US destination.

## Known Risks and Mitigations:

Risk: Live sends, particularly legal or certified mail, can incur costs or have real-world consequences.

Mitigation: Test with a sandbox key first; require explicit human confirmation and review the cost and document preview before a live send.

Risk: Agent API keys may grant access to sensitive mail and funded sending.

Mitigation: Keep API keys out of prompts and logs, and use the appropriate sandbox or scoped key.

Risk: Scanning, forwarding, or discarding inbound mail affects private correspondence.

Mitigation: Review the quoted action and require the mailbox owner's approval before carrying it out.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/arbengine/skills/mailbox-bot)
- [MCP install guide](https://mailbox.bot/mcp-install)
- [API documentation](https://mailbox.bot/api-docs)
- [Public MCP tool catalog](https://mailbox.bot/api/mcp/tools-public)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with command and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports sandbox testing, cost quotes, and human approval for sensitive actions.]

## Skill Version(s):

5.2.0 (source: server release metadata, skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
