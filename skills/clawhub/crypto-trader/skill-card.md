## Description: <br>
Crypto Trader automates cryptocurrency trading workflows across eight strategies with multi-exchange connectivity, sentiment analysis, risk management, backtesting, paper trading, monitoring, and alerting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nandichi](https://clawhub.ai/user/nandichi) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to inspect crypto portfolios, run backtests, evaluate market sentiment, manage strategy lifecycle, and operate paper or live exchange-connected trading workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make or cancel live financial orders through broad agent-triggered commands without an enforceable confirmation gate in the runtime code. <br>
Mitigation: Keep CRYPTO_DEMO=true unless live trading is intentional, require explicit user confirmation before starting strategies, and review proposed order parameters before execution. <br>
Risk: Exchange API credentials can authorize trading activity. <br>
Mitigation: Use exchange API keys with withdrawal permissions disabled and limit permissions to the minimum trading access required. <br>
Risk: The emergency-stop command can cancel all open orders across configured exchanges. <br>
Mitigation: Use emergency stop only for deliberate stop-all situations and review configured exchanges before invoking it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nandichi/crypto-trader) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/nandichi) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [Risk limits configuration](artifact/config/risk_limits.yaml) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and structured JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and exchange API credentials; paper trading is the default when CRYPTO_DEMO is true.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
