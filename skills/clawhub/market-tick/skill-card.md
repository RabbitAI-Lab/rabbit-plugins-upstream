## Description:

Paid x402 endpoint: $0.014 USDC per call on Base. Returns BTC, ETH and SOL prices, market regime, Fear & Greed, and a momentum label.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading agents can make a paid request for BTC, ETH and SOL prices, a BTC market regime and momentum label, and a Fear & Greed value. The response can support market monitoring or serve as a lightweight input to a trading workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Each request costs $0.014 USDC and requires an EVM wallet private key for payment authorization.

Mitigation: Keep EVM_PRIVATE_KEY in a secret store and limit the wallet balance to the calls you intend to make.

Risk: Market prices and labels may be used as inputs to automated trading decisions.

Mitigation: Check the returned values and timestamp before acting on them, and apply the trading workflow's own safeguards.

## Reference(s):

- [Market Tick endpoint](https://apexrunner.ai/signals/market-tick)
- [BTC Price Tick](https://apexrunner.ai/signals/btc-price-tick)
- [APEX Pulse](https://apexrunner.ai/signals/apex-pulse)
- [Volume Analysis](https://apexrunner.ai/signals/volume-analysis)

## Skill Output:

**Output Type(s):** [API Calls, JSON]

**Output Format:** [JSON response containing prices, market labels, sentiment, and a timestamp]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live endpoint response; unavailable inputs may result in HTTP 503.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
