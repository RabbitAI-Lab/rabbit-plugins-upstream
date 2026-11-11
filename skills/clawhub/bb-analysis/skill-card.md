## Description:

Paid x402 endpoint returning Bollinger Band analysis with squeeze detection and breakout probability for $0.007 USDC per call on Base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Crypto traders and agents use this skill to retrieve live Bollinger Band squeeze, band-position, and breakout-probability signals when evaluating breakout or mean-reversion setups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Calls spend USDC, and invoking the skill requires access to an EVM private key.

Mitigation: Keep the key in a secure secret store, use a wallet funded only for intended calls, and confirm the per-call price before invoking the endpoint.

## Reference(s):

- [APEX Runner Bollinger analysis endpoint](https://apexrunner.ai/signals/bb-analysis)
- [ClawHub bb-analysis release](https://clawhub.ai/kynto2001-ctrl/skills/bb-analysis)
- [APEX Runner mean-reversion scan](https://apexrunner.ai/signals/mean-reversion-scan)
- [APEX Runner volume analysis](https://apexrunner.ai/signals/volume-analysis)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Analysis]

**Output Format:** [JSON signal response with squeeze status, band position, and breakout probability]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each call costs $0.007 USDC through 2027-01-01 under the stated early-adopter discount; the documented standard price is $0.01 per call. Requires an EVM wallet private key and USDC on Base mainnet.]

## Skill Version(s):

1.0.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
