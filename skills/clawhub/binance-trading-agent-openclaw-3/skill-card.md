## Description: <br>
Automates Binance USDS-M Futures trading with market analysis, indicator calculation, dynamic risk management, and order execution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kritsanan1](https://clawhub.ai/user/kritsanan1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and trading automation operators use this skill to analyze Binance USDS-M Futures markets and run an automated Python agent that can size and place long or short futures orders. Evaluate it with testnet or restricted credentials before any live account use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can place leveraged Binance USDS-M Futures orders, which may create financial loss if connected to a live account. <br>
Mitigation: Keep FUTURES_TESTNET enabled until reviewed, use restricted or testnet API keys, and require human confirmation before live trading. <br>
Risk: Runtime safeguards and risk disclosure are incomplete for production trading authority. <br>
Mitigation: Add explicit position, leverage, symbol, order-size, and loss limits before production use. <br>
Risk: The skill requires Binance API credentials and account access. <br>
Mitigation: Store keys in environment variables or a secret manager, use least-privilege permissions, and avoid logging secrets or full account responses. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kritsanan1/skills/binance-trading-agent-openclaw-3) <br>
- [Source repository](https://github.com/kritsanan1/binance-trading-agent-openclaw) <br>
- [Publisher profile](https://clawhub.ai/user/kritsanan1) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, API calls] <br>
**Output Format:** [Python commands, log messages, and Binance Futures API requests] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Defaults to BTCUSDT on a 1h timeframe with 10x leverage, 1% risk per trade, and FUTURES_TESTNET enabled.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
