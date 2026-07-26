## Description: <br>
Trade stocks, ETFs, options, and crypto through Alpaca's REST API using curl-based commands, with support for orders, positions, account activity, portfolio history, market data, watchlists, and corporate actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lacymorrow](https://clawhub.ai/user/lacymorrow) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agent users use this skill to inspect Alpaca account state, retrieve market data, and prepare or submit Alpaca trading API requests for equities, ETFs, options, and crypto. It is intended for users who intentionally connect an Alpaca account and can review trading actions before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can place, modify, cancel, exercise, or close brokerage positions, including live trading if configured for Alpaca's live endpoint. <br>
Mitigation: Keep paper trading as the default, use restricted or paper API keys where possible, and require explicit readback confirmation before POST, PATCH, DELETE, option exercise, cancel-all, or close-all actions. <br>
Risk: Configurable base URLs and account credentials can expose brokerage access if pointed at untrusted endpoints or handled carelessly. <br>
Mitigation: Do not point the base URL at non-Alpaca domains, store API keys in environment variables, and avoid logging or sharing credential-bearing command output. <br>
Risk: Market data and trading workflow output could be mistaken for financial advice. <br>
Mitigation: Present data and proposed request bodies for user review, avoid financial advice, and leave trading decisions to the user. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/lacymorrow/skills/alpaca-trading) <br>
- [Alpaca Trading README](artifact/README.md) <br>
- [Alpaca REST API Reference](artifact/references/api.md) <br>
- [Alpaca](https://alpaca.markets) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON request bodies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands call Alpaca REST endpoints with environment-provided credentials and default to paper trading unless live trading is explicitly configured.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
