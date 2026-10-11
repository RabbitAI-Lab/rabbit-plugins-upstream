## Description:

Helps agents use a user-deployed mt5-httpapi bridge to inspect MetaTrader 5 accounts and market data, run backtests, and carry out explicitly confirmed trading and terminal actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and traders who already run mt5-httpapi use this skill to query their MetaTrader 5 accounts, retrieve market data, inspect backtests, and request precisely specified trading or terminal operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Orders, position changes, and live expert deployments can affect a real brokerage account.

Mitigation: Start with a demo account and require exact, account-specific confirmation before each trading or deployment action.

Risk: An exposed or unauthenticated API can disclose account data and allow unauthorized trades.

Mitigation: Set a strong API token and keep the service on localhost or behind strong access controls.

Risk: Terminal-control and sensitive file changes can interrupt trading or alter executable strategy behavior.

Mitigation: Confirm the target terminal and exact operation or file change before proceeding.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/mt5-httpapi)
- [mt5-httpapi project homepage](https://github.com/psyb0t/mt5-httpapi)
- [mt5-httpapi setup guide](artifact/references/setup.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with API response summaries and optional curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a user-provided MT5_API_URL; state-changing actions require explicit per-action confirmation.]

## Skill Version(s):

4.28.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
