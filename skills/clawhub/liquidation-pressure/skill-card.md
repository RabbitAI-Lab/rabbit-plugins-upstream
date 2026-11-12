## Description:

Paid x402 endpoint: $0.007 USDC per call on Base. Returns aggregate liquidation pressure score across tracked perpetuals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Traders and market analysts use the skill to check aggregate liquidation pressure across tracked perpetual markets as a market-stress overlay and before considering leveraged positions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Each request authorizes a USDC payment from the configured Base wallet.

Mitigation: Confirm the current price and use a wallet funded only for the calls you intend to make; keep its private key in a secret store and out of logs.

Risk: The aggregate liquidation signal may be used to inform leveraged trading decisions.

Mitigation: Treat the response as one market-stress input, check that it is current, and apply independent trading and position-risk controls.

## Reference(s):

- [Liquidation Pressure signal endpoint](https://apexrunner.ai/signals/liquidation-pressure)
- [Liquidation Magnet signal](https://apexrunner.ai/signals/liquidation-magnet)
- [Crowded Trade Detector signal](https://apexrunner.ai/signals/crowded-trade-detector)
- [ClawHub skill release](https://clawhub.ai/kynto2001-ctrl/skills/liquidation-pressure)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Guidance]

**Output Format:** [JSON response with a pressure score, at-risk USD estimate, and qualitative level]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A paid request costs $0.007 USDC per call on Base under the documented early-adopter price.]

## Skill Version(s):

1.0.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
