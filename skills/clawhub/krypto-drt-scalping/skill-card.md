## Description:

Crypto DRT Scalping provides a crypto DRT scalping strategy and local backtest reference for selected crypto pairs, with optional paid x402 live-signal calls that require X402_API_KEY and contact an external endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to review crypto DRT scalping rules, risk controls, and historical backtest claims, then optionally run a paid live-signal script for selected symbols. The skill is most appropriate for users who understand crypto trading risk, paid API calls, and the difference between historical backtests and future performance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional live-signal script can make paid x402 calls using a spending-capable API key.

Mitigation: Run it only after reviewing the premium section, confirming the cost, and using a tightly limited X402_API_KEY.

Risk: The packaged runnable path sends X402_API_KEY to a hardcoded external endpoint unless X402_BASE is changed.

Mitigation: Use the default endpoint only if you trust its operator, or set X402_BASE to a verified HTTPS service endpoint before running the script.

Risk: Historical backtest results and stated win rates may not predict live trading outcomes.

Mitigation: Treat the strategy as informational guidance, use separate play-money limits, and review all trades manually before taking action.

Risk: Sending the paid API key over plain HTTP could expose a spending-capable credential.

Mitigation: Keep HTTPS enabled and do not set X402_ALLOW_HTTP=1 unless the risk is intentional and separately controlled.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/northcap-group/skills/krypto-drt-scalping)
- [Publisher profile](https://clawhub.ai/user/northcap-group)
- [Premium x402 signal endpoint](https://186.240.156.169:8791)
- [x402 API key reference](https://github.com/MohamedAbdisamed/x402-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, code, JSON]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional premium live-signal output depends on an external paid x402 endpoint and a spending-capable X402_API_KEY.]

## Skill Version(s):

1.0.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
