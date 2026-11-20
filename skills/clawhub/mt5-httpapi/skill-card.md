## Description:

Connects agents to a user-configured MetaTrader 5 HTTP bridge for market and account data, analysis, backtest results, and explicitly confirmed trading or chart deployment actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and traders with a running, configured mt5-httpapi instance use the skill to retrieve market and account information, technical analysis, and backtest results. It can also manage orders, positions, terminals, and chart deployments when the user explicitly confirms each consequential action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates the skill suspicious with medium confidence and incomplete evidence, citing reported capabilities beyond its stated HTTP client scope, including tunnel setup and local file operations.

Mitigation: Review the full reported scope, especially live trading, deployment actions, tunnel setup, and file access, before installation or exposure; unresolved scanner paths leave the assessment incomplete.

Risk: Order, position, and chart deployment operations can change a live account or start an Expert Advisor that trades on its own.

Mitigation: Require fresh, per-action confirmation that identifies the account and exact operation and trade parameters before each mutation.

Risk: An API instance without authentication, or one exposed to untrusted networks, can expose account data and permit trading actions.

Mitigation: Set a strong API token and keep the service bound to loopback or behind an authenticated proxy; require access controls when using a public tunnel.

## Reference(s):

- [Setup and security guidance](artifact/references/setup.md)
- [Project documentation](https://github.com/psyb0t/mt5-httpapi)
- [Chart deployment operator guide](https://github.com/psyb0t/mt5-httpapi/blob/master/docs/chart-deployments.md)
- [File API operator guide](https://github.com/psyb0t/mt5-httpapi/blob/master/docs/files.md)
- [Technical analysis indicator catalog](https://github.com/psyb0t/docker-wickworks#available-indicators)
- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [ClawHub skill listing](https://clawhub.ai/psyb0t/skills/mt5-httpapi)

## Skill Output:

**Output Type(s):** [API responses, Analysis, Guidance, Shell commands, Configuration]

**Output Format:** [JSON and text responses, with Markdown guidance and inline shell commands; some endpoints return images or HTML reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Response content depends on the requested endpoint; some actions affect a live brokerage account or running Expert Advisor.]

## Skill Version(s):

4.34.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
