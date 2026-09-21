## Description:

Luckin Coffee operates an OOMOL-connected Luckin Coffee account for store discovery, product lookup, order previews, order status checks, order creation, and order cancellation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate a connected Luckin Coffee account: find stores, inspect products, preview prices, and, after confirmation, create or cancel orders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer scripts for the oo CLI.

Mitigation: Review the installer before use and prefer a trusted package or verified download for the oo CLI.

Risk: The skill can create real Luckin Coffee orders and cancel existing orders.

Mitigation: Confirm the exact payload, price, pickup details, and target order before creating or canceling an order.

Risk: Connector contracts can change and incorrect payloads could trigger unintended account or order actions.

Mitigation: Inspect the live action schema before every connector call and send only payload fields that match the current schema.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-luckin-coffee)
- [Luckin Coffee MCP Homepage](https://open.lkcoffee.com/mcp)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash, PowerShell, text, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live schema inspection before connector calls; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
