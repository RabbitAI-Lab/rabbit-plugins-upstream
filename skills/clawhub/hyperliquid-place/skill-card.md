## Description:

Place, cancel, or close Hyperliquid perps when the user explicitly asks to trade, place, cancel, close, or execute.

This skill is ready for commercial/non-commercial use.

## Publisher:

[polyparlay](https://clawhub.ai/user/polyparlay)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent submit, cancel, or close Hyperliquid perpetual futures orders after explicit trading intent. It also provides setup and balance/position guidance for the pinned local MCP trading rail.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can submit leveraged mainnet Hyperliquid trades with real funds and no final confirmation after coin, side, and sizeUsd are stated.

Mitigation: Use testnet for practice, require explicit mainnet selection, and require the user to state leverage, order type, and price or slippage limits before any live order.

Risk: The skill relies on a pinned npm package for the local MCP trading rail.

Mitigation: Review the pinned dependency before installation and install it only in the skill scripts directory.

Risk: Trading setup may involve exporting an agent private key into the shell environment.

Mitigation: Use a low-value agent wallet and avoid exporting high-value keys into broad shell environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/polyparlay/skills/hyperliquid-place)
- [Hyperliquid app](https://app.hyperliquid.xyz)
- [Pinned @hypelens/hypelens-agent-rail 0.1.21 package](https://registry.npmjs.org/@hypelens/hypelens-agent-rail/-/hypelens-agent-rail-0.1.21.tgz)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls]

**Output Format:** [Markdown with inline shell commands and tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct an agent to use Hyperliquid trading tools that place, cancel, or close live orders.]

## Skill Version(s):

1.3.39 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
