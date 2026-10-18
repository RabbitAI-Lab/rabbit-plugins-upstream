## Description:

Guides an agent in using a user-deployed MetaTrader 5 HTTP bridge to inspect account and market data, run backtests, and perform explicitly confirmed trading and terminal actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and traders who already operate mt5-httpapi use this skill to query their MetaTrader 5 accounts and market data, run backtests, and manage explicitly authorized orders, positions, and chart deployments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Orders, position changes, and chart deployments can affect real brokerage accounts.

Mitigation: Test with a demo account first; confirm the exact account and trade or deployment details before every mutation, and never retry a trade without fresh confirmation.

Risk: An unauthenticated or exposed bridge can disclose account state and permit unauthorized trades.

Mitigation: Set a strong API token and keep the bridge on localhost or behind strong access controls.

Risk: Terminal shutdown, restart, and MT5 file changes can disrupt trading or running strategies.

Mitigation: Require explicit confirmation of the target terminal and operation before restarting or changing MT5 files.

## Reference(s):

- [mt5-httpapi project homepage (declared in skill metadata)](https://github.com/psyb0t/mt5-httpapi)
- [mt5-httpapi setup guide](references/setup.md)
- [Chart deployments documentation](https://github.com/psyb0t/mt5-httpapi/blob/master/docs/chart-deployments.md)
- [File API documentation](https://github.com/psyb0t/mt5-httpapi/blob/master/docs/files.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with curl and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-configured MT5_API_URL and curl; a token is required when server authentication is enabled.]

## Skill Version(s):

4.29.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
