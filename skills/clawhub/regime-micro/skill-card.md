## Description:

Paid x402 endpoint: $0.007 USDC per call on Base. Returns current market regime label at minimal cost for fast agent loops.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Developers building crypto-market agent loops use the endpoint for frequent regime checks, stable-regime filtering, or as a pre-filter before a confluence signal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Each endpoint request incurs a USDC charge, so frequent agent loops can accumulate spend.

Mitigation: Set request-frequency and spend limits, and check the endpoint's current price before running repeated calls.

Risk: The example uses an EVM private key to authorize payments; exposing that key could put the wallet at risk.

Mitigation: Keep the key in a protected secret store or environment, and use a dedicated wallet funded only for expected calls.

## Reference(s):

- [Regime Micro endpoint](https://apexrunner.ai/signals/regime-micro)
- [Regime signal](https://apexrunner.ai/signals/regime)
- [Regime Confluence signal](https://apexrunner.ai/signals/regime-confluence)
- [Trend Confirmed signal](https://apexrunner.ai/signals/trend-confirmed)
- [ClawHub release page](https://clawhub.ai/kynto2001-ctrl/skills/regime-micro)

## Skill Output:

**Output Type(s):** [API Calls, JSON]

**Output Format:** [JSON object containing compact market regime labels and a timestamp]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The response uses b, e, s, and a for regime labels and t for the timestamp.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
