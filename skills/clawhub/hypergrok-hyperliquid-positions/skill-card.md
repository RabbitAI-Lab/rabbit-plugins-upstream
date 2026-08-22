## Description:

Helps agents manage Hyperliquid perpetual position and margin workflows, including reading positions, changing leverage and isolated margin, checking liquidation risk and protection, closing positions, and cleaning up orphaned orders under ticket-gated write controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and trading-desk operators use this skill to help agents inspect Hyperliquid perpetual positions, margin usage, liquidation distance, and protection status, then prepare or execute approved position-management actions. Write actions are limited to Execution Trader workflows on approved tickets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can change leverage, margin, or close Hyperliquid positions.

Mitigation: Keep API credentials scoped, require approved tickets for write actions, and restrict execution to the Execution Trader role.

Risk: Using the wrong network can send actions to mainnet when testnet was intended.

Mitigation: Confirm network selection before mainnet use and treat the documented testnet default as a rehearsal setting, not proof that production actions are harmless.

Risk: Stale position or order data can close the wrong size or leave orphaned protection orders.

Mitigation: Read live position size immediately before closes, use reduce-only IOC semantics, and verify or cancel leftover TP/SL orders after position changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/galleonlabs/skills/hypergrok-hyperliquid-positions)
- [Hyperliquid Mainnet API Endpoint](https://api.hyperliquid.xyz)
- [Hyperliquid Testnet API Endpoint](https://api.hyperliquid-testnet.xyz)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell, Python, and TypeScript code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes account-state checks, margin and liquidation interpretation, and ticket-gated write-action examples for leverage, isolated margin, position closing, and order cleanup.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
