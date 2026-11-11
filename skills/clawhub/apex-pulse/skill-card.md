## Description:

Paid x402 endpoint: $0.007 USDC per call on Base. Returns APEX system heartbeat — confirms live trading is active and healthy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

External users and trading agents use the paid APEX heartbeat endpoint to check whether the live system is active and confirm signal freshness before relying on related signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Each request incurs a fee and uses an EVM wallet private key for x402 payment.

Mitigation: Check the current per-call price, use a wallet funded only for the intended calls, and keep EVM_PRIVATE_KEY in secret storage.

Risk: The external endpoint and its links were outside the security scan scope.

Mitigation: Verify the endpoint and payment terms before sending authenticated requests or relying on its response.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/kynto2001-ctrl/skills/apex-pulse)
- [APEX Pulse endpoint](https://apexrunner.ai/signals/apex-pulse)
- [APEX Market Tick](https://apexrunner.ai/signals/market-tick)
- [APEX Grid Health](https://apexrunner.ai/signals/grid-health)
- [APEX Portfolio Heat](https://apexrunner.ai/signals/portfolio-heat)

## Skill Output:

**Output Type(s):** [API Calls, JSON]

**Output Format:** [JSON heartbeat response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One paid response per request.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
