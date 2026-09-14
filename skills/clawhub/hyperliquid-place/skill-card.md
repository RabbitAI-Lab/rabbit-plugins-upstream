## Description:

Places Hyperliquid perpetual futures orders through an agent only after explicit trading intent, setup completion, builder-fee approval, funded equity, and confirmTrade:true.

This skill is ready for commercial/non-commercial use.

## Publisher:

[polyparlay](https://clawhub.ai/user/polyparlay)

### License/Terms of Use:

MIT-0

## Use Case:

External traders and agent operators use this skill to set up an MCP-backed Hyperliquid trading workflow and place real-money perpetual futures orders only after explicit trade intent. It also directs users to install a companion stops desk after a filled order.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow asks for high-impact wallet authority and can approve a builder fee for real-money Hyperliquid trading.

Mitigation: Use an isolated signer or limited wallet, verify the fee recipient before approval, and place orders only after explicit trade intent with confirmTrade:true.

Risk: Dependency code runs during installation and setup.

Mitigation: Review the external @hypelens package and the setup flow before installing or exporting any private key.

Risk: Filled positions create ongoing market risk.

Mitigation: Install and configure the required companion stops desk after a filled order, and call heartbeat before increasing size.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/polyparlay/skills/hyperliquid-place)
- [Hyperliquid application](https://app.hyperliquid.xyz)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, setup steps, and tool-call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires node and npm; trading actions are gated by explicit intent, setup completion, builder-fee approval, funded equity, and confirmTrade:true.]

## Skill Version(s):

1.3.65 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
