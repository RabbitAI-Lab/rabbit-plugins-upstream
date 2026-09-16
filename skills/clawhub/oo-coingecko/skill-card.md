## Description:

CoinGecko (coingecko.com). Use this skill for CoinGecko search and read-only market data requests through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to search CoinGecko and retrieve coin metadata, prices, market charts, OHLC candles, tickers, global market data, token contract lookups, and GeckoTerminal-style onchain data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents remote installer commands that execute downloaded code and can change the local machine.

Mitigation: Review the skill before installing if the oo CLI is not already present, and prefer a verified, pinned, or package-manager-based installation process.

Risk: CoinGecko access is brokered through an OOMOL-connected account with server-side credential injection.

Mitigation: Authenticate and connect CoinGecko only when you intentionally want OOMOL to broker access for these read-oriented queries.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-coingecko)
- [CoinGecko Homepage](https://www.coingecko.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON with data and meta.executionId fields.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
