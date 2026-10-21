## Description:

Helps agents use a user-configured MetaTrader 5 HTTP bridge to inspect account and market data, run backtests, and perform explicitly confirmed trading and terminal operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and traders with their own configured mt5-httpapi server use this skill to query MetaTrader 5 accounts, prices, and backtests, and to request individually confirmed trade or terminal actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trades and live Expert Advisor deployments can cause irreversible financial loss.

Mitigation: Start with a demo account and require exact per-action confirmation of the account and trade or deployment details before live changes.

Risk: An exposed bridge without authentication can allow unauthorized account access or trades.

Mitigation: Set a strong API token and keep the endpoint on loopback or behind strong access controls.

Risk: Terminal restarts, WebRequest changes, and file writes or deletions can disrupt or alter live trading.

Mitigation: Confirm the selected terminal and exact operation before performing each change.

## Reference(s):

- [Setup guide](references/setup.md)
- [mt5-httpapi project](https://github.com/psyb0t/mt5-httpapi)
- [Chart deployments guide](https://github.com/psyb0t/mt5-httpapi/blob/master/docs/chart-deployments.md)
- [File API guide](https://github.com/psyb0t/mt5-httpapi/blob/master/docs/files.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with curl examples and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided MT5_API_URL and a token when server authentication is enabled.]

## Skill Version(s):

4.30.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
