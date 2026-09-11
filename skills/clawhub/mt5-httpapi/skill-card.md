## Description:

mt5-httpapi helps an agent use a user-deployed MetaTrader 5 HTTP bridge for account data, market data, technical analysis, history, backtest reports, and explicitly confirmed order, position, or terminal actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading operators use this skill after configuring a self-hosted mt5-httpapi endpoint so an agent can inspect account and market state, fetch server-side analysis and backtest artifacts, and carry out user-confirmed trade or terminal actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger order, position, and terminal actions that may affect real-money brokerage accounts.

Mitigation: Use demo accounts first and require explicit per-action confirmation that shows the account, broker path, symbol, side, volume, price, stop loss, and take profit before any mutation.

Risk: A remotely reachable endpoint without strong authentication can expose account state and allow trade changes.

Mitigation: Keep MT5_API_URL on localhost unless the deployment is secured with HTTPS, strong access controls, and a protected bearer token.

Risk: A wrong broker, account, or instance path can route an otherwise valid action to the wrong terminal.

Mitigation: Show the resolved broker, account, instance, and target URL path in every confirmation prompt for mutating actions.

Risk: Credential discovery from local configuration could expose broker passwords, login numbers, or API tokens.

Mitigation: Read MT5_API_TOKEN only from the user-provided environment variable or direct user input, and do not inspect repository configuration files for credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/mt5-httpapi)
- [mt5-httpapi homepage](https://github.com/psyb0t/mt5-httpapi)
- [Setup guide](references/setup.md)
- [wickworks technical analysis sidecar](https://github.com/psyb0t/docker-wickworks)
- [mt5-httpapi OpenClaw plugin](https://github.com/psyb0t/mt5-httpapi/tree/main/.agents/plugins/mt5-httpapi)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with curl command examples, JSON request and response shapes, and configuration snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided MT5_API_URL and uses MT5_API_TOKEN when the server is configured for bearer-token authentication.]

## Skill Version(s):

4.13.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
