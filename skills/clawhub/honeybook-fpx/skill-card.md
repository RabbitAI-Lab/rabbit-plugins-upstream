## Description:

Guides agents in reading HoneyBook client-portal contracts, invoices, proposals, payment methods, and workspace status using a captured browser session and shell commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and authorized HoneyBook clients use this skill to retrieve vendor-shared documents and account details from a signed-in client portal without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Captured browser session credentials can grant access to a HoneyBook account.

Mitigation: Use only accounts and vendors you are authorized to access; protect captured credentials and delete local copies promptly.

Risk: Saved session data, contracts, invoices, proposals, or payment-method responses can expose sensitive information.

Mitigation: Avoid shared temporary paths, logs, and shell history; retain only the data needed for the task.

Risk: The documented message-sending workflow can email a vendor for real.

Mitigation: Do not invoke it unless the account holder explicitly intends to send that message.

## Reference(s):

- [HoneyBook FPX ClawHub release](https://clawhub.ai/chrischall/skills/honeybook-fpx)
- [HoneyBook request examples](references/requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can return sensitive HoneyBook account records.]

## Skill Version(s):

1.2.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
