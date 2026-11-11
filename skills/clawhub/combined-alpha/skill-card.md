## Description:

Paid x402 endpoint: $0.007 USDC per call on Base. Returns combined alpha signal merging momentum, mean-reversion, and sentiment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this endpoint to retrieve a paid combined crypto signal for analysis or as a tie-breaker among competing signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Each request incurs a USDC payment, so repeated or unintended calls can add up.

Mitigation: Confirm the current price and limit call frequency or wallet spending before use.

Risk: The skill uses an EVM private key to authorize wallet payments.

Mitigation: Keep the key in a secrets manager and use a dedicated wallet funded only for intended calls.

Risk: A live trading signal may be incomplete or wrong and does not guarantee an outcome.

Mitigation: Treat the response as one input, and independently review it before making trading decisions.

## Reference(s):

- [Combined Alpha endpoint](https://apexrunner.ai/signals/combined-alpha)
- [Apex Composite signal](https://apexrunner.ai/signals/apex-composite)
- [Signal Intelligence](https://apexrunner.ai/signals/signal-intelligence)

## Skill Output:

**Output Type(s):** [API Calls, JSON]

**Output Format:** [JSON signal response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A paid request costs $0.007 USDC per call through 2027-01-01; requests use an EVM wallet on Base.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
