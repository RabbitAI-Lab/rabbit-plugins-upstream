## Description:

Helps agents research Hyperliquid perpetual futures, assess funding and position risk, and submit or cancel orders only with fresh user confirmation and a user-signed request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic)

### License/Terms of Use:

MIT-0

## Use Case:

Traders and agents use this skill to scan Hyperliquid perpetual markets, compare strategies, size positions against risk limits, and prepare user-authorized order or cancellation requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Perpetual-futures orders and cancellations can cause significant financial loss, especially with leverage and fees.

Mitigation: Review each proposed order or cancellation, verify leverage and fees, and require fresh manual confirmation and a user wallet signature before submission. Never share private keys or seed phrases.

## Reference(s):

- [FarmDash Futures Strategist on ClawHub](https://clawhub.ai/parmasanandgarlic/skills/farmdash-futures-strategist)
- [FarmDash agent documentation](https://www.farmdash.one/agents)
- [FarmDash Futures Strategist skill manual](https://www.farmdash.one/openclaw-skills/farmdash-futures-strategist/SKILL.md)
- [FarmDash OpenAPI contract](https://www.farmdash.one/agents/openapi.yaml)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Market and risk summaries, structured strategy objects, and proposed signed-order or cancellation details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an explicit no-trade recommendation; execution requires a separate current user confirmation and wallet signature.]

## Skill Version(s):

1.0.28 (source: ClawHub release metadata; skill frontmatter: 3.4.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
