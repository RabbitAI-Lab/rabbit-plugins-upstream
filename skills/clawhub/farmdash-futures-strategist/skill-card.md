## Description:

Helps agents research Hyperliquid perpetual futures, assess funding and position risk, and submit user-approved, signed orders or cancellations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic)

### License/Terms of Use:

MIT-0

## Use Case:

Traders and agent operators use this skill to review Hyperliquid market conditions, compare strategy and sizing options, and prepare explicitly approved perpetual futures orders or cancellations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Leveraged perpetual futures trades can cause real financial loss.

Mitigation: Review the proposed asset, size, leverage, margin impact, and risk limits before signing each order or cancellation.

Risk: Sharing wallet secrets could compromise funds.

Mitigation: Never provide private keys or seed phrases; use fresh, locally signed EIP-712 requests.

Risk: Builder fees or affiliate routes may compensate FarmDash.

Mitigation: Review disclosed fees and choose the canonical Hyperliquid route if preferred.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/parmasanandgarlic/skills/farmdash-futures-strategist)
- [FarmDash Agent Hub](https://www.farmdash.one/agents)
- [FarmDash agent integration documentation](https://www.farmdash.one/docs)
- [FarmDash futures API contract](https://www.farmdash.one/agents/openapi.yaml)
- [FarmDash fees](https://www.farmdash.one/fees)

## Skill Output:

**Output Type(s):** [Text, Guidance, API calls]

**Output Format:** [Markdown trade analysis and structured API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May present no-trade recommendations; orders and cancellations require fresh user signatures and confirmation.]

## Skill Version(s):

1.0.27 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
