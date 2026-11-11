## Description:

Provides BTC dominance percentage and trend direction from a paid x402 endpoint on Base ($0.007 USDC per call).

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Crypto traders and portfolio agents use the BTC dominance signal to inform BTC versus altcoin allocation and spot possible altcoin season or capital rotation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Each request costs USDC and uses an EVM private key; unintended or repeated requests can spend wallet funds.

Mitigation: Confirm the per-call price and intended request frequency, protect the private key, and use a wallet funded only for intended calls.

## Reference(s):

- [BTC dominance endpoint](https://apexrunner.ai/signals/btc-dominance)
- [ClawHub skill release](https://clawhub.ai/kynto2001-ctrl/skills/btc-dominance)
- [APEX Runner](https://apexrunner.ai)
- [Altcoin season signal](https://apexrunner.ai/signals/altcoin-season)
- [Capital rotation signal](https://apexrunner.ai/signals/capital-rotation-signal)

## Skill Output:

**Output Type(s):** [JSON, API Calls]

**Output Format:** [JSON with BTC dominance percentage, trend direction, and altcoin-season status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an EVM wallet private key and charges USDC per request.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
