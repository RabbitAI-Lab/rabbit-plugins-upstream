## Description:

Fetch a pre-transaction risk score and advisory recommendation for tokens on Solana, Base, Ethereum, Arbitrum, BSC, and HyperEVM before the user trades, swaps, or provides liquidity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[babyscaphe](https://clawhub.ai/user/babyscaphe)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use Bitfence before token swaps, DEX trades, staking, or liquidity actions involving unfamiliar tokens to request an advisory risk score and recommendation. The skill is read-only and helps users review risk before deciding whether to proceed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid API calls may spend USDC on Base mainnet.

Mitigation: Inform the user about pricing and obtain consent before the first paid risk check in a session.

Risk: Contextual checks may disclose position size and portfolio size.

Mitigation: Use the contextual endpoint only after the user opts in to sharing that additional context.

Risk: Risk scores and recommendations are advisory and may not guarantee trading safety.

Mitigation: Surface warnings, confidence, reasoning, and any circuit-breaker flags clearly so the user can make the final decision.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/babyscaphe/skills/bitfence)
- [Bitfence website](https://www.bitfence.ai)
- [Bitfence API root](https://api.bitfence.ai)

## Skill Output:

**Output Type(s):** [API Calls, Analysis, Guidance]

**Output Format:** [JSON risk reports summarized as concise user-facing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include advisory recommendation, risk score, confidence, reasoning, circuit-breaker flags, degraded-source details, and contextual position guidance when the user opts in.]

## Skill Version(s):

0.7.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
