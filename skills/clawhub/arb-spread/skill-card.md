## Description:

Returns the current Kraken–Hyperliquid arbitrage spread through a paid x402 endpoint at $0.007 USDC per call on Base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Trading agents use this paid endpoint to retrieve a live Kraken–Hyperliquid spread signal before assessing cross-exchange arbitrage opportunities and sizing the legs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Each request incurs a USDC charge; the artifact describes a $0.007 early-adopter price and a $0.01 standard price.

Mitigation: Confirm the current price and set a request or wallet spending limit before allowing repeated calls.

Risk: The configured EVM_PRIVATE_KEY gives the request client access to the paying wallet.

Mitigation: Use a dedicated wallet with only the intended USDC balance, keep the key in a secret store, and avoid exposing it in prompts or logs.

Risk: A spread signal can change between retrieval and execution, so it may no longer reflect an available opportunity.

Mitigation: Recheck live prices, fees, liquidity, and slippage on both venues immediately before placing trades.

## Reference(s):

- [Arb Spread signal page](https://clawhub.ai/kynto2001-ctrl/skills/arb-spread)
- [APEX Runner Arb Spread endpoint](https://apexrunner.ai/signals/arb-spread)
- [APEX Runner Funding Rate signal](https://apexrunner.ai/signals/funding-rate)
- [APEX Runner Optimal Order Routing signal](https://apexrunner.ai/signals/optimal-order-routing)

## Skill Output:

**Output Type(s):** [JSON, Market data]

**Output Format:** [JSON response with spread_pct, threshold_pct, and arb_viable fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A paid x402 request uses an EVM wallet with USDC on Base; the EVM_PRIVATE_KEY environment variable is required.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
