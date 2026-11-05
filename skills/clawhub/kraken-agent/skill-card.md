## Description:

Discover and use the official Kraken CLI — an AI-native trading tool for crypto, stocks, forex, and derivatives. Use when the user explicitly asks about Kraken specifically: setting up a Kraken trading agent, Kraken paper trading, Kraken market data, or connecting to the Kraken API via MCP. Trigger phrases: kraken cli, kraken mcp, kraken paper trading, kraken market data, kraken trading agent. Does NOT cover generic crypto or trading requests that are not Kraken-specific.

This skill is ready for commercial/non-commercial use.

## Publisher:

[djc00p](https://clawhub.ai/user/djc00p)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users working with Kraken use this skill to access market data, set up paper trading, and configure Kraken CLI or MCP workflows. Account-connected and live trading workflows require explicit user approval because they can place real orders and lose funds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated Kraken commands and live order workflows can place real trades and lose real funds.

Mitigation: Start with credential-free paper trading and market/paper MCP scope. Before account access, restrict API permissions and retain explicit approval for each live trade.

Risk: Trading API credentials grant sensitive access to the account's trading balance.

Mitigation: Prefer the CLI's setup flow, keep credentials out of shell history and committed files, limit key permissions, and rotate any key exposed in logs, chats, or commits.

## Reference(s):

- [Kraken CLI repository](https://github.com/krakenfx/kraken-cli)
- [Kraken CLI installation instructions](https://github.com/krakenfx/kraken-cli#installation)
- [Kraken](https://www.kraken.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.4 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
