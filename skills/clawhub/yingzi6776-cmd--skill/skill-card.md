## Description: <br>
StrategyLens helps agents turn English quantitative-finance and futures strategy material into Chinese explanations, runnable Python/pandas backtest templates, parameter guidance, and literature citations, with optional historical market data lookup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yingzi6776-cmd](https://clawhub.ai/user/yingzi6776-cmd) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and research-oriented finance analysts can use this skill to interpret quantitative trading literature, generate example backtest code, explain strategy parameters, and cite source works. It is intended for education and analysis, not broker integration, trading authority, or investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Quantitative strategy explanations and example backtests could be mistaken for investment advice or live trading signals. <br>
Mitigation: Treat outputs as research and education only; require independent review before relying on any result and do not use the skill for live trading. <br>
Risk: Historical backtests can be misleading because of overfitting, future leakage, missing transaction costs, or unsuitable market data. <br>
Mitigation: Validate assumptions, include realistic costs and out-of-sample checks, and document data source, symbol, period, and parameters for each backtest. <br>
Risk: Market-data lookup may expose user-selected symbols, time ranges, or data-source choices to the configured data provider. <br>
Mitigation: Use only approved data sources and avoid entering account credentials, broker tokens, or confidential trading plans. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yingzi6776-cmd/skills/skill) <br>
- [StrategyLens homepage](https://clawhub.ai/skill/strategylens) <br>
- [Quant and futures strategy library](references/strategies.md) <br>
- [Systematic futures and trading literature modules](references/systematic_main.md) <br>
- [Quant and futures literature map](references/literature.md) <br>
- [Risk management reference](references/risk_management.md) <br>
- [Options and volatility reference](references/options_volatility.md) <br>
- [High-frequency trading and market microstructure reference](references/hft_microstructure.md) <br>
- [Quantitative foundations reference](references/quant_foundations.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown with Chinese explanations and Python/pandas code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use a configured market-data MCP for historical prices; does not request broker credentials or place trades.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
