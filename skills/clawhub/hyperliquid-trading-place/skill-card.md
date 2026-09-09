## Description:

Place, cancel, or close Hyperliquid perps when the user explicitly asks to trade/place/cancel/close/execute.

This skill is ready for commercial/non-commercial use.

## Publisher:

[polyparlay](https://clawhub.ai/user/polyparlay)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to help place, cancel, or close Hyperliquid perpetual futures orders only after explicit trading intent. It also supports setup and sizing checks before trade execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default network can use mainnet real funds for perpetual futures trading.

Mitigation: Use testnet first when possible and confirm network, size, side, leverage, and order type before approving any trade.

Risk: Trading setup may require an agent private key.

Mitigation: Keep the agent private key protected and do not provide or request private keys unless the user explicitly chooses to configure trading.

Risk: Live fills disclose and charge a 1bp builder fee to a specific builder address.

Mitigation: Verify the 1bp builder fee and address before signing approval payloads.

Risk: The skill can place, cancel, or close positions when invoked through its trading tools.

Mitigation: Only use trade execution tools after explicit user intent to trade, place, cancel, close, or execute.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/polyparlay/skills/hyperliquid-trading-place)
- [Hyperliquid App](https://app.hyperliquid.xyz)
- [Hypelens Agent Rail npm package](https://registry.npmjs.org/@hypelens/hypelens-agent-rail/-/hypelens-agent-rail-0.1.21.tgz)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with inline shell commands and tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May involve MCP tool calls for Hyperliquid setup, balances, positions, order placement, cancellation, and closing.]

## Skill Version(s):

1.0.9 (source: server release metadata and scripts/package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
