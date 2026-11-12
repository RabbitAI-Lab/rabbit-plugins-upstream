## Description:

Paid x402 endpoint: $0.007 USDC per call on Base. Returns lightweight Fear & Greed index snapshot for high-frequency polling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Agents that need frequent market-sentiment checks can call this paid endpoint to retrieve a lightweight Fear & Greed snapshot. It can be used for polling or as one input to trade-decision workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Each request is a paid call and uses an EVM wallet private key; frequent polling can increase charges. The linked service pages were outside the scan’s scope.

Mitigation: Use a dedicated wallet with a limited USDC balance, confirm the current endpoint and price, and set a polling limit before making repeated calls.

## Reference(s):

- [ClawHub fg-micro release](https://clawhub.ai/kynto2001-ctrl/skills/fg-micro)
- [APEX Runner fg-micro endpoint](https://apexrunner.ai/signals/fg-micro)
- [APEX Runner fear-greed signal](https://apexrunner.ai/signals/fear-greed)
- [APEX Runner regime-micro signal](https://apexrunner.ai/signals/regime-micro)

## Skill Output:

**Output Type(s):** [JSON, API data]

**Output Format:** [Compact JSON containing a Fear & Greed value, label, and timestamp]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returned by a paid x402 request; polling frequency affects total cost.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
