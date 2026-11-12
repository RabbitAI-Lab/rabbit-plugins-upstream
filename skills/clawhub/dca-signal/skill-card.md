## Description:

Paid x402 endpoint: $0.007 USDC per call on Base. Returns DCA entry signal with gate status, regime, and F&G conditions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill at the start of a DCA decision cycle to retrieve a live entry signal and check its gate, market regime, and Fear & Greed conditions before placing orders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Each signal request incurs a charge, and repeated polling can increase the total cost.

Mitigation: Check the current per-call price and set a request limit or spending budget before use.

Risk: Paid requests use an EVM wallet private key supplied through EVM_PRIVATE_KEY.

Mitigation: Protect the key in a secure environment variable and use a dedicated wallet funded only for intended payments.

Risk: A DCA signal may influence real trading decisions, but it does not establish that an order is suitable for a particular portfolio.

Mitigation: Check the reported gate conditions and apply independent portfolio and risk limits before placing orders.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/kynto2001-ctrl/skills/dca-signal)
- [DCA signal endpoint](https://apexrunner.ai/signals/dca-signal)
- [Related Fear & Greed signal](https://apexrunner.ai/signals/fear-greed)
- [Related portfolio heat signal](https://apexrunner.ai/signals/portfolio-heat)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [JSON signal response with gate status, market regime, Fear & Greed conditions, and a DCA entry signal.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live signal retrieved through a paid request; the listed release price is $0.007 USDC per call.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
