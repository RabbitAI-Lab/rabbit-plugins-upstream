## Description:

This skill helps agents use an Evite MCP server to read invitations and hosted events, manage RSVPs and guest lists, message guests, and create or edit Evite events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People managing Evite invitations and event hosting can use this skill with an agent to inspect events, summarize RSVPs, manage guests, send messages, and prepare confirm-gated changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Evite MCP server can access and modify Evite events through the configured account.

Mitigation: Install only when that account access is acceptable and prefer scoped credentials where possible.

Risk: Raw Evite session cookies can grant account access if exposed.

Mitigation: Avoid pasting raw session cookies unless necessary and use email/password credentials when appropriate.

Risk: Guest messages, invitation sending, guest-list changes, or event cancellation could affect real invitees.

Mitigation: Review dry-run previews and require explicit confirmation before enabling write actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/evite)
- [evite-mcp npm package](https://www.npmjs.com/package/evite-mcp)
- [Evite](https://www.evite.com)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Shell commands, Text, Markdown]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normal operation depends on an Evite MCP server configured with Evite account credentials or a session cookie.]

## Skill Version(s):

1.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
