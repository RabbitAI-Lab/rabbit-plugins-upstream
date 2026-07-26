## Description: <br>
StrategyLens helps agents turn quantitative trading and futures literature into Chinese strategy explanations, Python/pandas backtest templates, parameter notes, citations, and risk disclaimers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yingzi6776-cmd](https://clawhub.ai/user/yingzi6776-cmd) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze quantitative trading, futures, options, risk, and market microstructure strategies, then produce Chinese explanations and local backtest templates for historical research. It is intended for educational analysis and backtesting workflows, not personalized investment advice or live trading. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may mistake historical backtest output for personalized investment advice or live-trading guidance. <br>
Mitigation: Present outputs as research and education only, include risk disclaimers, and keep broker or order-entry tools separate. <br>
Risk: Configured market-data sources may return incomplete, stale, or unsuitable data for the requested symbol or date range. <br>
Mitigation: Verify the data source, symbol, date range, and required OHLCV fields before interpreting strategy results. <br>
Risk: Backtests can be misleading because of overfitting, future leakage, missing transaction costs, leverage, or futures margin risk. <br>
Mitigation: Use out-of-sample checks, guardrail scripts, transaction-cost assumptions, and explicit leverage or margin warnings. <br>


## Reference(s): <br>
- [StrategyLens ClawHub Skill Page](https://clawhub.ai/yingzi6776-cmd/skills/strategylens-quant-kit) <br>
- [StrategyLens Homepage](https://clawhub.ai/skill/strategylens) <br>
- [Quantitative and Futures Literature Index](references/literature.md) <br>
- [Classic Quantitative and Futures Strategy Library](references/strategies.md) <br>
- [Systematic Futures Mainline](references/systematic_main.md) <br>
- [Risk Management](references/risk_management.md) <br>
- [Options and Derivatives](references/options_volatility.md) <br>
- [High-Frequency Trading and Market Microstructure](references/hft_microstructure.md) <br>
- [Quantitative Foundations](references/quant_foundations.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown prose with Python/pandas code snippets and optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes citations, parameter notes, risk disclaimers, and historical backtest outputs when market data is supplied.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
