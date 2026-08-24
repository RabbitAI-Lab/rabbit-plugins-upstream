## Description:

Crypto DRT scalping - Dealing Range Theory on 12 crypto pairs (TRX, BNB, BTC, LINK, AVAX, DOGE, SOL, NEAR, XRP, LDO, ADA, ETH), all 7 days, with historical backtest context and separate play-money account rules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to apply a Dealing Range Theory scalping plan to crypto pairs, review historical backtest expectations, and optionally fetch paid live DRT signals. The skill is trading guidance, not a guarantee of future performance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The paid signal client can charge per use and sends a spending-capable API key to a hard-coded remote service.

Mitigation: Use the paid signal client only intentionally, verify the provider, wallet, pricing, and endpoint independently, and use a tightly limited API key where available.

Risk: A spending-capable API key could be exposed if HTTP transport is enabled.

Mitigation: Keep HTTPS transport enabled and do not set X402_ALLOW_HTTP=1 for a spending-capable key.

Risk: Backtest results and trading-plan expectations may not match future market performance.

Mitigation: Treat the content as trading guidance, validate signals independently, and follow the skill's separate play-money account and loss-limit rules.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/northcap-group/skills/crypto-drt-scalping)
- [Publisher profile](https://clawhub.ai/user/northcap-group)
- [Live signal API endpoint](https://186.240.156.169:8791)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API calls]

**Output Format:** [Markdown guidance with bash command examples and optional JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional live signal calls require X402_API_KEY and may charge per request.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
