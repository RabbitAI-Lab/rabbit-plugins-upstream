## Description: <br>
Helps an agent write a profit-laddered grid-style trading strategy for Superior Trade, including Freqtrade strategy code, configuration guidance, and caveats about true order-book grid bots. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[superior-ai](https://clawhub.ai/user/superior-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and trading-strategy authors use this skill to draft a Freqtrade-compatible range-fade strategy with laddered entries, partial take-profits, and configuration notes. It is most relevant when a user asks for grid trading, ladder buys, scaling into drawdowns, or related position-adjustment strategies. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated trading strategies and backtest claims may be misunderstood or used with real capital before their assumptions and loss exposure are reviewed. <br>
Mitigation: Review the financial assumptions, run dry-run or paper trading first, and deploy only after validating risk controls against the intended market and capital limits. <br>
Risk: Exchange credentials or live trading access could be exposed if users place secrets directly in generated code or configuration. <br>
Mitigation: Keep exchange credentials outside generated code, use secret-management practices supported by the trading runtime, and limit account permissions where possible. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/superior-ai/grid-trading) <br>
- [Freqtrade adjust_trade_position documentation](https://www.freqtrade.io/en/stable/strategy-callbacks/#adjust-trade-position) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown with Python and JSON code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include trading assumptions, backtest caveats, and risk-control recommendations.] <br>

## Skill Version(s): <br>
1.5.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
