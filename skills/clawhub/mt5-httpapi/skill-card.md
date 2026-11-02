## Description:

Provides account and market data through a user-configured MetaTrader 5 HTTP bridge and performs live trading or chart operations only after per-action confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and MetaTrader 5 account operators use this skill to retrieve account, symbol, rate, tick, history, and backtest information from an explicitly configured bridge, and to manage trades or chart-based Expert Advisors when specifically authorized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trade, position, terminal, or live Expert Advisor changes can have real financial or service effects.

Mitigation: Show the affected account and exact operation details, require explicit confirmation for each action, and obtain fresh confirmation before retrying after an error or timeout.

Risk: An unauthenticated or exposed MT5 server can reveal account data and permit trade actions.

Mitigation: Use a trusted private endpoint with a strong token and HTTPS or authenticated access; start with a demo account and verify the deployed server's protections.

Risk: An approved Expert Advisor can continue trading after activation.

Mitigation: Leave optional deployment features disabled unless needed and confirm the target account, Expert Advisor, symbol, and settings before activation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/mt5-httpapi)
- [Project homepage (release metadata)](https://github.com/psyb0t/mt5-httpapi)
- [Setup guide](references/setup.md)

## Skill Output:

**Output Type(s):** [JSON, Text, Guidance]

**Output Format:** [Endpoint-dependent API data with concise text summaries and confirmation prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses depend on the selected endpoint; actions that can affect live trades or Expert Advisors require explicit, per-action user confirmation.]

## Skill Version(s):

4.31.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
