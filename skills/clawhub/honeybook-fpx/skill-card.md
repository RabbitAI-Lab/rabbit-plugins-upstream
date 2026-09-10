## Description:

Read HoneyBook client-portal data such as contracts, invoices, proposals, payment methods, and workspace status from a shell with fpx and curl using a captured signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve HoneyBook portal records from a shell when the MCP server is unavailable or unnecessary. It is intended for users who already have authorized browser access to the relevant HoneyBook portal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reuses live HoneyBook session credentials to access sensitive client, contract, invoice, message, and payment-method data.

Mitigation: Install only when this access is acceptable, use a dedicated HoneyBook account where possible, avoid shared machines, avoid persisting session captures or API responses in /tmp, and revoke browser or session access after use.

Risk: The artifact includes a message-sending path that can send a real email even though the skill is framed mainly around reading data.

Mitigation: Use message-sending steps only when a real email is intended, and prefer preview-capable tooling before sending.

## Reference(s):

- [HoneyBook request examples](artifact/references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/honeybook-fpx)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON data from HoneyBook APIs; users should filter responses to the fields they need.]

## Skill Version(s):

0.10.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
