## Description:

Paid x402 endpoint: $0.007 USDC per call on Base. Returns volume profile analysis detecting accumulation or distribution patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and traders can request a live volume profile signal to assess accumulation or distribution, confirm breakouts with volume, and add context before momentum entries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Each request makes a paid USDC call; the documented early-adopter price is $0.007 per call through 2027-01-01, with a stated standard price of $0.01.

Mitigation: Check the current price and endpoint before sending a request, and keep only the amount you intend to spend in the calling wallet.

Risk: The skill requires an EVM private key to authorize payment.

Mitigation: Provide the key through a protected secret environment variable and use a dedicated wallet with limited funds.

Risk: Volume signals may inform cryptocurrency trading decisions but do not establish that a trade will be profitable.

Mitigation: Treat the response as one input, check it against independent analysis, and apply your own trading and risk limits.

## Reference(s):

- [ClawHub volume-analysis release](https://clawhub.ai/kynto2001-ctrl/skills/volume-analysis)
- [APEX Runner volume-analysis endpoint](https://apexrunner.ai/signals/volume-analysis)
- [Related signal: trend-confirmed](https://apexrunner.ai/signals/trend-confirmed)
- [Related signal: bb-analysis](https://apexrunner.ai/signals/bb-analysis)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, JSON]

**Output Format:** [JSON response containing a signal label and volume metrics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A paid request returns a signal, volume_ratio, and above_average value.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
