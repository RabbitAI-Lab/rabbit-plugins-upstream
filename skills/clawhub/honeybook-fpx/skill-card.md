## Description:

Guides agents in reading HoneyBook client-portal contracts, invoices, proposals, payment methods, and workspace status using a browser-captured session and shell commands without the HoneyBook MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect a signed-in client's HoneyBook portal records from the shell when the HoneyBook MCP server is unavailable or unnecessary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Captured browser session tokens could grant access to sensitive client-portal data if exposed.

Mitigation: Use a trusted machine, avoid saving tokens or responses to shared temporary files, and promptly delete any captured session files.

Risk: The skill describes a message-sending path that can email a vendor despite its read-oriented purpose.

Mitigation: Require explicit human review and approval before sending any message or running other write actions.

## Reference(s):

- [HoneyBook FPX ClawHub release](https://clawhub.ai/chrischall/skills/honeybook-fpx)
- [HoneyBook request examples](references/requests.md)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON query examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only examples cover portal files, workspaces, and payment methods; message sending is a separate external action.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
