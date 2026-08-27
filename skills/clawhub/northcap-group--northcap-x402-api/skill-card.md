## Description:

Provides pay-per-call crypto trading signals with entry, stop-loss and take-profit via the x402 standard (USDC on Ethereum). Live DRT/ICT signals for agents and traders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, agents, and traders use this skill to discover, pay for, and call a Northcap x402 API that returns crypto trading signal data with entry, stop-loss, take-profit, and risk-reward fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill describes paid API calls for a crypto-signal service.

Mitigation: Require explicit user approval, spending limits, and confirmation of pricing before any paid call is made.

Risk: Crypto trading signals can be inaccurate or unsuitable for a user's risk tolerance.

Mitigation: Do not let an agent make trading decisions without explicit user-defined trading limits and independent review.

Risk: The skill depends on a localhost service and payment details that must match the expected provider.

Mitigation: Confirm the local service, wallet, and pricing independently before sending an API key, transaction hash, or payment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/northcap-group/skills/northcap-x402-api)
- [Northcap Group publisher profile](https://clawhub.ai/user/northcap-group)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, JSON]

**Output Format:** [Markdown guidance with JSON API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides paid x402 API calls that require X402_API_KEY and return crypto signal records from a localhost service.]

## Skill Version(s):

1.0.10 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
