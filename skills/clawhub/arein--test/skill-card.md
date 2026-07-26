## Description: <br>
CLI for crypto portfolio tracking, market data, and CEX history. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arein](https://clawhub.ai/user/arein) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to query crypto market data, wallet balances, portfolio values, Coinbase and Binance account history, and Polymarket prediction-market data through the onchain CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive wallet and exchange account information. <br>
Mitigation: Use read-only exchange API keys with trading and withdrawals disabled, store secrets in protected environment variables or a secure config location, and query only accounts or wallets the user is authorized to inspect. <br>
Risk: The skill depends on a separate onchain CLI implementation and multiple external crypto data services. <br>
Mitigation: Confirm the CLI source is trusted before installation and account for upstream API rate limits or service errors when using the skill in agent workflows. <br>


## Reference(s): <br>
- [DeBank Cloud](https://cloud.debank.com/) <br>
- [Helius](https://helius.xyz/) <br>
- [Coinbase API Key Settings](https://www.coinbase.com/settings/api) <br>
- [Binance API Management](https://www.binance.com/en/my/settings/api-management) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Configuration guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON-oriented CLI usage] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Use --json for programmatic agent output; API responses may be rate limited by upstream services.] <br>

## Skill Version(s): <br>
0.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
