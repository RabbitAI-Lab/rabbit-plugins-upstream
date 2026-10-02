## Description:

Helps agents use a user-configured MetaTrader 5 HTTP bridge to inspect account and market data, run backtests, and submit explicitly confirmed trading actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and traders who already run mt5-httpapi can inspect their MetaTrader account, retrieve market data and backtest results, and request trades with explicit confirmation for each action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trading requests can open, modify, cancel, or close real-money positions.

Mitigation: Start with a demo account; show the account, broker, symbol, side, volume, price, stop-loss, and take-profit, then obtain explicit confirmation for each mutation.

Risk: An exposed bridge without authentication could permit unauthorized account access and trading.

Mitigation: Set a strong API token and keep the bridge bound to localhost or behind strong authentication.

Risk: A wrong broker or account selection could direct a trade to an unintended account.

Mitigation: Verify the broker and account shown by the server before every mutating action.

## Reference(s):

- [ClawHub release](https://clawhub.ai/psyb0t/skills/mt5-httpapi)
- [mt5-httpapi project and documentation](https://github.com/psyb0t/mt5-httpapi)
- [Setup guide](references/setup.md)
- [Wickworks indicator reference](https://github.com/psyb0t/docker-wickworks#available-indicators)
- [mt5-httpapi OpenClaw plugin](https://github.com/psyb0t/mt5-httpapi/tree/main/.agents/plugins/mt5-httpapi)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance, Configuration]

**Output Format:** [Markdown with shell commands and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided MT5_API_URL and, when authentication is enabled, MT5_API_TOKEN.]

## Skill Version(s):

4.15.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
