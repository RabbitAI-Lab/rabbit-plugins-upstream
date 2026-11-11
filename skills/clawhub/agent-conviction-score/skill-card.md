## Description:

Paid x402 endpoint returning a conviction score for current APEX trade signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Crypto trading agents use this paid endpoint to retrieve a conviction score for current APEX signals when comparing setups and reviewing trade decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Endpoint calls are paid; the release describes a $0.007 per-call early-adopter price through 2027-01-01 and a $0.01 standard price.

Mitigation: Check the current price before use and set a spending limit for repeated calls.

Risk: The example authenticates with an EVM wallet private key supplied through EVM_PRIVATE_KEY.

Mitigation: Keep the key in a secure secret store and use a dedicated wallet funded only for expected payments.

Risk: A conviction score can be misleading if treated as a guarantee or the sole basis for a trade.

Mitigation: Review the signal and other relevant information independently before making trading or position-sizing decisions.

Risk: A benign scan does not establish that the skill is suitable for every purpose.

Mitigation: Review whether its paid endpoint and trading use fit your needs before installing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/kynto2001-ctrl/skills/agent-conviction-score)
- [Agent Conviction Score endpoint](https://apexrunner.ai/signals/agent-conviction-score)
- [APEX Alpha Score](https://apexrunner.ai/signals/apex-alpha-score)
- [Signal Intelligence](https://apexrunner.ai/signals/signal-intelligence)
- [Crowded Trade Detector](https://apexrunner.ai/signals/crowded-trade-detector)

## Skill Output:

**Output Type(s):** [JSON data]

**Output Format:** [JSON response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a conviction score, aligned signal count, direction, and confidence.]

## Skill Version(s):

1.0.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
