## Description:

Guides agents to read HoneyBook client-portal data from a signed-in browser session using fpx and shell commands without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and authorized HoneyBook clients use this skill to inspect vendor-shared contracts, invoices, proposals, payment methods, and workspace status from a shell without deploying an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser session tokens and saved HoneyBook responses can expose sensitive account, vendor, or payment information.

Mitigation: Use only accounts and vendors you are authorized to access; treat session credentials as passwords, avoid saving captures or responses in /tmp, and delete any saved JSON promptly.

Risk: The message-sending flow emails a vendor for real.

Mitigation: Do not invoke it unless you intend to send a real message; review the recipient and content before sending.

Risk: Browser site access exposes a signed-in session to the fpx CLI and ContextMint Bridge.

Mitigation: Review the CLI and extension source or verified release before granting access to HoneyBook and portal domains.

## Reference(s):

- [HoneyBook request examples](references/requests.md)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [Fetchproxy extension background](https://github.com/chrischall/fetchproxy#extension)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authorized, signed-in HoneyBook portal session; signing and payment require user action in the browser.]

## Skill Version(s):

1.2.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
