## Description:

Guides an agent through authenticated OKX CEX trading workflows for spot, swaps, futures, options, and event contracts, including order placement, cancellation, amendment, monitoring, take-profit, stop-loss, trailing stops, leverage, and position management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate OKX CEX trading tasks through the OKX CLI after credentials and live/demo mode are confirmed. It is intended for order-management workflows, not standalone market data, portfolio balance, or trading bot workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use OKX credentials to submit, amend, cancel, and close real trades.

Mitigation: Prefer demo mode first, require explicit live or demo mode selection, and require order-detail confirmation before every write operation.

Risk: One event-contract workflow weakens the live/demo and authentication preflight.

Mitigation: Run the credential/profile check before event-contract writes and require explicit confirmation of instrument, side, outcome, size, order type, and price when applicable.

Risk: Derivative order sizes can be misread when contract face value or USDT sizing mode is ambiguous.

Mitigation: Verify contract face value before swap, futures, or option orders, and ask whether USDT amounts mean notional value or margin cost before placing the order.

## Reference(s):

- [OKX homepage](https://www.okx.com)
- [Trade workflows and examples](references/workflows.md)
- [MCP tool reference and output conventions](references/templates.md)
- [Spot command reference](references/spot-commands.md)
- [Swap and perpetual command reference](references/swap-commands.md)
- [Futures and delivery command reference](references/futures-commands.md)
- [Options command reference](references/options-commands.md)
- [Event contract command reference](references/event-commands.md)
- [Event contract workflows](references/event-workflows.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Markdown]

**Output Format:** [Markdown with inline shell commands and parameter guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the OKX CLI and user-configured OKX credentials; authenticated write operations depend on confirmed live or demo mode.]

## Skill Version(s):

1.4.6 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
