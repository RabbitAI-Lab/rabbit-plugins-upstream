## Description:

Paid x402 endpoint: $0.007 USDC per call on Base. Returns comprehensive grid health score with recommendations for optimisation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Crypto trading grid operators can call the paid endpoint to review current grid performance, consider parameter changes, and include a health score in weekly reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Calls incur a USDC payment, and the skill requires an EVM private key for x402 authorization.

Mitigation: Confirm the endpoint and current price before calling it, and use a dedicated wallet with only the funds needed for the request; keep its private key in a secure secret store.

## Reference(s):

- [Grid Health Score endpoint](https://apexrunner.ai/signals/grid-health-score)
- [Related Grid Health signal](https://apexrunner.ai/signals/grid-health)
- [Related Grid Levels signal](https://apexrunner.ai/signals/grid-levels)
- [APEX Runner](https://apexrunner.ai)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Recommendations, Guidance]

**Output Format:** [JSON response containing a score, grade, and recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each call requires an EVM wallet key and incurs a USDC charge: $0.007 per call through 2027-01-01 under the early-adopter discount, with a $0.01 standard price.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
