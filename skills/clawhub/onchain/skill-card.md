## Description: <br>
CLI for crypto portfolio tracking, market data, CEX history, and transaction lookups. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arein](https://clawhub.ai/user/arein) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and agent operators use this skill to run Onchain CLI commands for crypto prices, wallet balances, portfolio values, exchange history, transaction details, and prediction market summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Exchange API credentials could allow unwanted account access if configured with broad permissions or exposed through local files. <br>
Mitigation: Use newly created read-only Coinbase and Binance keys with trading and withdrawals disabled, protect local config files, and avoid committing .onchainrc.json5. <br>
Risk: Wallet lookups, exchange account data, and JSON output may expose financial identifiers in third-party APIs or agent logs. <br>
Mitigation: Review commands before use with real wallets or exchange accounts, limit shared outputs, and treat balances, addresses, transaction hashes, and account responses as sensitive. <br>


## Reference(s): <br>
- [Onchain CLI skill page](https://clawhub.ai/arein/skills/onchain) <br>
- [DeBank Cloud](https://cloud.debank.com/) <br>
- [Helius](https://helius.xyz/) <br>
- [Coinbase CDP](https://portal.cdp.coinbase.com/) <br>
- [Binance API management](https://www.binance.com/en/my/settings/api-management) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration guidance] <br>
**Output Format:** [Terminal text or JSON, often accompanied by shell command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses exit codes for success or failure; JSON output is intended for agent parsing.] <br>

## Skill Version(s): <br>
0.3.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
