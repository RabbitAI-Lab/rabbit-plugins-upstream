## Description:

Place Hyperliquid perps: order, cancel, and close positions via hl_place_order for OpenClaw/MCP with an agent wallet, automatic rounding, and 1bp builder fees on mainnet fills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[polyparlay](https://clawhub.ai/user/polyparlay)

### License/Terms of Use:

MIT-0

## Use Case:

External users and trading-focused developers use this skill to set up an agent wallet and place, cancel, or close Hyperliquid perpetual futures orders through OpenClaw/MCP. It is intended for live or testnet trading workflows, with explicit care around mainnet actions and wallet handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill defaults toward live Hyperliquid mainnet trading, where place, cancel, and close actions can affect real funds.

Mitigation: Prefer HYPELENS_NET=testnet for initial setup and require explicit user confirmation before any mainnet place, cancel, or close action.

Risk: The MCP package is installed through npx without a pinned version in the artifact instructions.

Mitigation: Pin and verify the package version before installation or execution.

Risk: The workflow may handle a trading private key through HYPELENS_AGENT_PK.

Mitigation: Use a dedicated low-balance agent wallet and avoid exposing unrelated environment variables to the runtime.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/polyparlay/skills/hyperliquid-place)
- [polyparlay publisher profile](https://clawhub.ai/user/polyparlay)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and MCP tool call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes wallet setup, network selection, order placement, cancellation, close-position, balance, and position workflow guidance.]

## Skill Version(s):

1.3.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
