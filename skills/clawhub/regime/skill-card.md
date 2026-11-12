## Description:

Paid x402 endpoint: $0.007 USDC per call on Base. Returns full market regime classification: TRENDING, RANGING, CHOPPY, or CRISIS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Crypto traders and agents use this paid market signal to classify current conditions as trending, ranging, choppy, or crisis before selecting or routing a trading strategy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Each request charges USDC, and the client uses an EVM wallet private key.

Mitigation: Protect EVM_PRIVATE_KEY, limit the wallet balance used for calls, and confirm the current per-call price before use.

Risk: Crypto trading signals may not suit every user or strategy.

Mitigation: Assess suitability before installing or relying on the signal, and apply independent trading risk controls.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/kynto2001-ctrl/skills/regime)
- [Regime signal endpoint](https://apexrunner.ai/signals/regime)
- [Regime Micro signal](https://apexrunner.ai/signals/regime-micro)
- [Regime Confluence signal](https://apexrunner.ai/signals/regime-confluence)
- [Regime Transition signal](https://apexrunner.ai/signals/regime-transition)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Analysis]

**Output Format:** [JSON response containing regime, confidence, coin, and timestamp]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A paid x402 request uses USDC on Base and an EVM wallet private key. The skill states a $0.007 USDC early-adopter price through 2027-01-01 and a $0.01 standard price.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
