## Description:

Paid x402 endpoint: $0.007 USDC per call on Base. Returns composite Fear & Greed index with source and staleness metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and crypto users use the Fear & Greed index to gauge overall market risk appetite, inform DCA timing, and calibrate position sizing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill signs per-call USDC payments using the configured wallet key, so unintended calls or exposed credentials could spend wallet funds.

Mitigation: Use a dedicated wallet with limited funds, protect EVM_PRIVATE_KEY, and enforce a per-call payment cap.

Risk: A market sentiment index may be stale or may not reflect an individual asset or trading situation.

Mitigation: Check the source and timestamp, and treat the index as context rather than the sole basis for a trade.

## Reference(s):

- [Fear & Greed signal endpoint](https://apexrunner.ai/signals/fear-greed)
- [ClawHub release page](https://clawhub.ai/kynto2001-ctrl/skills/fear-greed)
- [Related signal: fg-micro](https://apexrunner.ai/signals/fg-micro)
- [Related signal: dca-signal](https://apexrunner.ai/signals/dca-signal)

## Skill Output:

**Output Type(s):** [JSON]

**Output Format:** [JSON object containing an index value, classification, zone, source, and timestamp.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source and staleness metadata; retrieval requires an x402 USDC payment on Base.]

## Skill Version(s):

1.0.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
