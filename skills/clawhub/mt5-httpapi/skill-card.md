## Description:

HTTP client for a user-deployed mt5-httpapi MetaTrader 5 bridge that lets an agent inspect account, market data, technical analysis, history, orders, positions, terminal state, and backtest endpoints after MT5_API_URL is configured.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, traders, and agent operators use this skill to connect an agent to their own mt5-httpapi deployment for MetaTrader 5 account inspection, market-data retrieval, technical-analysis requests, order and position management, terminal control, and backtest retrieval. Mutating trade and terminal actions require explicit per-action confirmation from the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trade-mutating order and position endpoints can affect a real brokerage account and may be irreversible.

Mitigation: Require explicit confirmation for each mutating action, including symbol, side, volume, SL/TP, account login, and broker URL before sending the request.

Risk: An mt5-httpapi server without an API token can expose account state and trading controls to anyone who can reach it.

Mitigation: Use a strong API token, keep MT5_API_URL pointed at a trusted local or access-controlled endpoint, and avoid exposing unauthenticated instances.

Risk: Wrong-account routing can send a terminal or trading action to a different configured broker/account path.

Mitigation: Display and confirm the selected broker, account, and terminal operation before terminal control or trade mutation.

Risk: Credential discovery from local files can expose broker secrets or stale tokens.

Mitigation: Read MT5_API_TOKEN only from the user-provided environment variable or ask the user directly; do not search workspace files for credentials.

Risk: Automatic retries or bulk actions can duplicate orders or close unintended positions.

Mitigation: Stop after errors or timeouts, report the result, and require fresh user confirmation before retrying or acting on a batch.

## Reference(s):

- [mt5-httpapi setup](references/setup.md)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/mt5-httpapi)
- [mt5-httpapi homepage](https://github.com/psyb0t/mt5-httpapi)
- [OpenClaw mt5-httpapi plugin](https://github.com/psyb0t/mt5-httpapi/tree/main/.agents/plugins/mt5-httpapi)
- [wickworks indicator catalog](https://github.com/psyb0t/docker-wickworks#available-indicators)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown with inline shell commands, HTTP request examples, JSON response interpretation, and confirmation prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ordinary use requires curl, a user-provided MT5_API_URL, and MT5_API_TOKEN when the server is configured for authentication.]

## Skill Version(s):

4.12.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
