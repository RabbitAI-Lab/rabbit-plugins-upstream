## Description:

CLI for crypto portfolio tracking, market data, and CEX history. Use when the user asks about crypto prices, wallet balances, portfolio values, Coinbase/Binance holdings, or Polymarket predictions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arein](https://clawhub.ai/user/arein)

### License/Terms of Use:


## Use Case:

Developers and external users use this skill to run an onchain CLI for cryptocurrency market data, wallet balances, portfolio values, CEX balances and trade history, and Polymarket market lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exchange API keys, wallet-linked financial data, or exchange history could be exposed through prompts, logs, or local configuration.

Mitigation: Use read-only or scoped exchange API keys, keep ~/.config/onchain/config.json5 private, and avoid pasting secrets or sensitive financial history into prompts or logs.

Risk: Rapid market, wallet, or exchange queries may encounter third-party API rate limits.

Mitigation: Use the skill's timeout option, check exit codes, and add delays between rapid calls as described in the artifact guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/arein/skills/test)
- [DeBank API](https://cloud.debank.com/)
- [Helius](https://helius.xyz/)
- [Coinbase API settings](https://www.coinbase.com/settings/api)
- [Binance API management](https://www.binance.com/en/my/settings/api-management)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash code blocks and CLI command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI supports JSON output for agent-friendly parsing.]

## Skill Version(s):

0.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
