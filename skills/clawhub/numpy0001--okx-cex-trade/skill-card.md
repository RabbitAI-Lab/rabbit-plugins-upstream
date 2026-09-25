## Description:

Guides an agent through OKX CEX trading workflows for spot, perpetual swap, delivery futures, options, and event contracts, including placing, canceling, amending, and monitoring orders with required API credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[numpy0001](https://clawhub.ai/user/numpy0001)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent prepare and run OKX trading CLI commands for order management across spot, swaps, futures, options, and event contracts. It is intended for authenticated trading workflows and requires explicit care around demo versus live mode.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide live trading actions where unintended orders, market orders, leverage changes, batch cancels, or full position closes may affect real funds.

Mitigation: Use demo mode first, confirm live or demo mode before every trade, and require explicit user confirmation before high-impact order or leverage operations.

Risk: Credential and profile inspection is part of the workflow, and exposed API credentials would create account risk.

Mitigation: Do not accept credentials in chat, verify that profile output redacts secrets, and use restricted OKX API keys with withdrawals disabled and IP allowlisting where available.

Risk: The server security summary reports conflicting safeguards that could allow unintended live trades.

Mitigation: Review the skill before installing, keep trading mode visible in responses, and verify active profile selection before any authenticated command.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/numpy0001/skills/okx-cex-trade)
- [OKX homepage](https://www.okx.com)
- [OKX CEX Trading CLI](artifact/SKILL.md)
- [Trade Workflows & Examples](artifact/references/workflows.md)
- [Spot Command Reference](artifact/references/spot-commands.md)
- [Swap / Perpetual Command Reference](artifact/references/swap-commands.md)
- [Futures / Delivery Command Reference](artifact/references/futures-commands.md)
- [Options Command Reference](artifact/references/options-commands.md)
- [Event Contract Commands](artifact/references/event-commands.md)
- [Event Contract Workflows](artifact/references/event-workflows.md)
- [MCP Tool Reference & Output Conventions](artifact/references/templates.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OKX CLI configuration and authenticated credentials before trading commands can run.]

## Skill Version(s):

1.3.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
