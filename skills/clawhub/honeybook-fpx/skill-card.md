## Description:

Guides agents in reading HoneyBook client-portal contracts, invoices, proposals, payment methods, and workspace status using a captured browser session and shell commands without the HoneyBook MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect HoneyBook client-portal files, project status, and saved payment methods from a shell without running the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Captured HoneyBook sessions expose credentials and private portal data to shell-level access.

Mitigation: Use only in a trusted environment; restrict session captures to private, owner-only temporary storage and delete them promptly.

Risk: Full API responses can contain sensitive client and vendor information.

Mitigation: Select only the fields needed and avoid storing raw responses in shared temporary directories.

Risk: The included message-sending workflow emails a real vendor despite the skill's read-oriented purpose.

Mitigation: Do not send messages unless explicitly authorized; preview the content before sending.

## Reference(s):

- [HoneyBook FPX on ClawHub](https://clawhub.ai/chrischall/skills/honeybook-fpx)
- [Request examples](references/requests.md)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read responses can contain sensitive client and vendor data.]

## Skill Version(s):

1.2.6 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
