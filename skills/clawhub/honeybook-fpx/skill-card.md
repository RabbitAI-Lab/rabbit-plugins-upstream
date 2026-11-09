## Description:

Read HoneyBook client-portal data (contracts, invoices, proposals, payment methods, workspace status) from a shell with the fpx CLI (@fetchproxy/cli) instead of running the honeybook-mcp server — capture a vendor session once via the signed-in browser tab, then curl api.honeybook.com directly. Use when you want HoneyBook data without the MCP, in a script, or on a machine where the MCP isn't installed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers who work with HoneyBook client portals can use this skill to retrieve contracts, invoices, proposals, workspace status, and payment-method data through shell commands and scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Session tokens and private HoneyBook records can be exposed through captured session data, shell variables, or saved responses.

Mitigation: Keep tokens in memory or owner-only temporary storage, minimize saved account data, and remove temporary files after use.

Risk: The examples include a workflow that sends real messages to a vendor.

Mitigation: Require explicit approval before sending any message and review its content and recipient.

Risk: Persistent browser pairing and copied HoneyBook tokens can continue to expose account access; revoking pairing does not invalidate an already copied token.

Mitigation: Review the browser extension's permissions and persistent pairing, restrict access to the required domains, and protect copied tokens as active credentials.

## Reference(s):

- [HoneyBook requests for fpx and curl](references/requests.md)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [Fetchproxy extension documentation](https://github.com/chrischall/fetchproxy#extension)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON query examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use a signed-in HoneyBook session and can return private client-portal records.]

## Skill Version(s):

1.3.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
