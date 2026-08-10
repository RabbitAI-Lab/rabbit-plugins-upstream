## Description: <br>
Backtests 13 technical indicators on SPY and QQQ using five-year daily data, ranking single, pair, and triple-indicator strategies by return, Sharpe ratio, and drawdown. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[plato-1](https://clawhub.ai/user/plato-1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, quantitative analysts, and finance-focused agent users can use this skill to run technical-indicator backtests for SPY and QQQ, compare indicator combinations, and inspect return, Sharpe ratio, drawdown, and win-rate results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may fetch market data and create output files during backtesting. <br>
Mitigation: Run it from a dedicated project directory or virtual environment and review expected network and file-write behavior before use. <br>
Risk: The inspected artifact references scripts/indicator_backtest.py, but that script was not included. <br>
Mitigation: Confirm the referenced script is available and review it before relying on generated commands or results. <br>
Risk: Backtest results can be misread as predictive trading guidance. <br>
Mitigation: Treat outputs as exploratory analysis and validate assumptions, data quality, and strategy behavior independently before making financial decisions. <br>


## Reference(s): <br>
- [Indicator Lab ClawHub listing](https://clawhub.ai/plato-1/skills/indicator-lab) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Markdown, Analysis] <br>
**Output Format:** [Markdown with inline shell commands and backtest result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May depend on market data fetched over the network and may create local output files.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence.release.version, artifact/claw.json, target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
