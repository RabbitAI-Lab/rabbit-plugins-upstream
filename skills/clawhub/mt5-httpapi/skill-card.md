## Description:

Helps agents inspect market and account data, run backtests, and manage trades through a user-configured MetaTrader 5 HTTP bridge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and traders who have configured mt5-httpapi use this skill to inspect brokerage accounts and market data, run backtests, and perform explicitly confirmed trade or terminal actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trade and position changes can cause irreversible losses on a live brokerage account or affect the wrong account.

Mitigation: Start with a demo account; verify the account and require explicit confirmation of the exact account, symbol, side, volume, and stop-loss/take-profit for every trade action or retry.

Risk: An exposed or unauthenticated HTTP bridge can grant others access to brokerage data and trade controls.

Mitigation: Keep the bridge local or behind strong authentication, configure a strong API token, and never expose an unauthenticated endpoint publicly.

Risk: Terminal restarts, chart deployments, EA uploads, and backtest runs can disrupt a terminal, start live automation, or consume resources and write artifacts.

Mitigation: Require explicit confirmation of the target and operation before terminal control or live deployment; confirm requested uploads and resource-consuming backtest runs.

## Reference(s):

- [mt5-httpapi setup guide](references/setup.md)
- [mt5-httpapi project page (linked in release metadata)](https://github.com/psyb0t/mt5-httpapi)
- [wickworks technical indicators](https://github.com/psyb0t/docker-wickworks#available-indicators)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with API examples and result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Backtests can produce local reports and logs when requested.]

## Skill Version(s):

4.18.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
