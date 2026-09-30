## Description:

Helps agents query market and account data and, with explicit confirmation, manage trades through a user-deployed MetaTrader 5 HTTP bridge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and traders who already operate mt5-httpapi use this skill to retrieve account, market, history, and backtest data, and to request explicitly confirmed order or position actions on a selected MetaTrader 5 account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Order and position changes can affect real brokerage funds.

Mitigation: Start with a demo account and obtain fresh, action-specific confirmation before each live trade change.

Risk: An exposed or untrusted API endpoint can disclose account data or permit unauthorized trades.

Mitigation: Use only a trusted user-provided endpoint and set a strong API token before any non-local exposure.

Risk: Restarting or shutting down a terminal can interrupt trading access.

Mitigation: Confirm the target terminal and exact operation before taking terminal-control actions.

## Reference(s):

- [Setup guide](references/setup.md)
- [Project homepage (skill metadata)](https://github.com/psyb0t/mt5-httpapi)
- [wickworks technical analysis reference](https://github.com/psyb0t/docker-wickworks#available-indicators)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with inline curl commands and summaries of API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided MT5_API_URL and a token when server authentication is enabled.]

## Skill Version(s):

4.13.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
