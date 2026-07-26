## Description: <br>
Funding Rate Arbitrage helps agents draft and tune Freqtrade and Hyperliquid perpetual funding-rate strategies that seek to capture positive or negative funding carry. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[superior-ai](https://clawhub.ai/user/superior-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and trading-system builders use this skill to produce strategy guidance, sample Freqtrade code, Hyperliquid futures configuration, tuning notes, and common pitfalls for funding-rate carry backtests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Trading strategy guidance and historical backtest results may not predict future performance. <br>
Mitigation: Run fresh backtests, review assumptions, and validate risk limits before using any generated strategy in live trading. <br>
Risk: Incorrect exchange or pair configuration can produce missing funding data or misleading zero-trade results. <br>
Mitigation: Confirm that the target market is a Hyperliquid perpetual pair using the documented futures pair format before relying on the strategy output. <br>
Risk: Future versions could add credentials, network access, file mutation, or background behavior not present in the clean scan evidence. <br>
Mitigation: Review the displayed instructions, requested permissions, and security scan results at install time for each release. <br>


## Reference(s): <br>
- [Freqtrade DataProvider](https://www.freqtrade.io/en/stable/strategy-customization/) <br>
- [Hyperliquid Funding Mechanics](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/funding) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, configuration] <br>
**Output Format:** [Markdown with Python and JSON code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes strategy logic, configuration requirements, tunable parameters, variants, and operational pitfalls.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
