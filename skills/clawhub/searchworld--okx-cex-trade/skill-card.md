## Description:

Enables agents to place, cancel, amend, monitor, and manage OKX CEX spot, swap, futures, options, algo, leverage, and event-contract orders through the OKX CLI with configured API credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to prepare and execute OKX CEX trading workflows, including order placement, cancellation, amendments, leverage changes, position management, and event-contract trading. It is intended for users who have configured OKX credentials and understand whether each action is in demo or live mode.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through live exchange write actions that may place orders, change leverage, close positions, or otherwise affect real funds.

Mitigation: Prefer demo mode first, keep OKX API permissions as narrow as the exchange allows, and require explicit confirmation before every write action.

Risk: The event-contract workflow can cross into directional UP/DOWN trading recommendations.

Mitigation: Treat directional recommendations as trading advice, present the basis and uncertainty to the user, and require the user to choose or confirm the direction before any order is placed.

Risk: The security summary notes market-data use despite execution-only routing boundaries.

Mitigation: Route market data, balances, P&L, positions, fees, and transfers to the dedicated market or portfolio skills before using this skill for trading actions.

Risk: Credential exposure or stale authentication could lead to account misuse or failed trading commands.

Mitigation: Never accept credentials in chat; guide setup through okx config init, verify credential status before authenticated commands, and stop for re-authentication when authentication errors occur.

## Reference(s):

- [OKX Homepage](https://www.okx.com)
- [Trade Workflows & Examples](references/workflows.md)
- [Spot Command Reference](references/spot-commands.md)
- [Swap / Perpetual Command Reference](references/swap-commands.md)
- [Futures / Delivery Command Reference](references/futures-commands.md)
- [Options Command Reference](references/options-commands.md)
- [Event Contract Commands](references/event-commands.md)
- [Event Contract Workflows](references/event-workflows.md)
- [MCP Tool Reference & Output Conventions](references/templates.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API Calls]

**Output Format:** [Markdown with inline bash code blocks and CLI command sequences]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed okx CLI binary and configured OKX API or OAuth credentials; trading mode must be resolved as demo or live before authenticated commands.]

## Skill Version(s):

1.4.4 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
