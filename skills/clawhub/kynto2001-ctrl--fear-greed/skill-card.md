## Description:

Paid x402 endpoint: $0.007 USDC per call on Base. Returns composite Fear & Greed index with source and staleness metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Agents supporting users who assess crypto market risk appetite can retrieve a composite Fear & Greed signal, with source and staleness metadata, before considering DCA entries or position sizing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Each request incurs a USDC charge and uses an EVM wallet private key for x402 payment authorization.

Mitigation: Keep EVM_PRIVATE_KEY out of prompts and logs, use a wallet funded only for intended calls, and check the endpoint price before making requests.

## Reference(s):

- [Fear & Greed endpoint](https://apexrunner.ai/signals/fear-greed)
- [ClawHub fear-greed release](https://clawhub.ai/kynto2001-ctrl/skills/fear-greed)
- [APEX Runner](https://apexrunner.ai)
- [APEX Runner fg-micro signal](https://apexrunner.ai/signals/fg-micro)
- [APEX Runner dca-signal](https://apexrunner.ai/signals/dca-signal)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Analysis]

**Output Format:** [JSON response containing an index value, classification, source, and timestamp]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A paid x402-authenticated request; response includes source and staleness metadata.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
