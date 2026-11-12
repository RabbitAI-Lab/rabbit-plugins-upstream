## Description:

Paid x402 endpoint: $0.007 USDC per call on Base. Returns APEX proprietary alpha score for current market opportunity quality.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

External agents can request a paid APEX market opportunity score to help rank opportunities and inform trade evaluation. The skill describes using the score before trade entry; it should be treated as one input to a decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an EVM wallet private key to authorize paid requests, so exposing the key could put wallet funds at risk.

Mitigation: Supply the key through a trusted secret store or protected environment variable, and keep only the funds needed for intended calls in the wallet.

Risk: Each request incurs a USDC charge, and the documented early-adopter price is time-limited.

Mitigation: Check the current price and wallet balance before enabling repeated calls; set a request or spending limit where possible.

Risk: An alpha score may not reflect all factors relevant to a trade or its risk.

Mitigation: Evaluate the score alongside independent market and risk checks instead of using it as the sole basis for deploying capital.

## Reference(s):

- [APEX Alpha Score endpoint](https://apexrunner.ai/signals/apex-alpha-score)
- [ClawHub skill release](https://clawhub.ai/kynto2001-ctrl/skills/apex-alpha-score)
- [Combined Alpha](https://apexrunner.ai/signals/combined-alpha)
- [Agent Conviction Score](https://apexrunner.ai/signals/agent-conviction-score)

## Skill Output:

**Output Type(s):** [API response, JSON]

**Output Format:** [JSON market opportunity score and accompanying fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Retrieved through a paid x402 GET request; requires an EVM wallet private key and USDC on Base.]

## Skill Version(s):

1.0.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
