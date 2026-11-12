## Description:

Identifies price levels with dense liquidation clusters through a paid x402 endpoint costing $0.007 USDC per call on Base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

External traders and agents use this signal to identify dense liquidation zones when assessing risk levels, stop losses, and position sizing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Each request spends USDC from the configured wallet.

Mitigation: Check the current per-call price and wallet balance before requesting the signal.

Risk: The request uses the EVM_PRIVATE_KEY environment variable to authorize payment.

Mitigation: Store the private key in a secure secret store and do not expose it in logs or output.

## Reference(s):

- [Liquidation Magnet signal](https://apexrunner.ai/signals/liquidation-magnet)
- [Liquidation Pressure signal](https://apexrunner.ai/signals/liquidation-pressure)
- [Crowded Trade Detector signal](https://apexrunner.ai/signals/crowded-trade-detector)
- [APEX Runner](https://apexrunner.ai)

## Skill Output:

**Output Type(s):** [JSON, Analysis]

**Output Format:** [JSON response with liquidation levels, a risk label, and distance percentage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Real-time signal data returned by the paid endpoint]

## Skill Version(s):

1.0.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
