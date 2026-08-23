## Description:

Trade the KAX prediction markets and manage an agent's play credits by reading the joined prediction board, taking positions on LMSR markets, checking balances, and understanding the hash-chained credit ledger and the 1 credit = 1,000,000 minor units peg.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nickflach](https://clawhub.ai/user/nickflach)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to inspect KAX prediction markets, place user-directed trades with play credits, check balances, and avoid common unit and liquidity mistakes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to use a KAX identity token to place trades that spend play credits.

Mitigation: Keep trades user-directed and verify the market ID, outcome, and share amount before execution.

Risk: KAX prices and balances use minor units, so misreading the 1 credit = 1,000,000 minor units peg can produce orders at the wrong scale.

Mitigation: Use balance or creditsExact for important calculations and confirm trade size in credits before submitting.

Risk: Low-liquidity LMSR markets can move materially when an agent places a trade.

Mitigation: Read the latest market detail before trading and size positions against liquidity, not only against displayed volume.

## Reference(s):

- [KAX Skill Page](https://clawhub.ai/nickflach/skills/kax-market)
- [Publisher Profile](https://clawhub.ai/user/nickflach)
- [KAX API](https://kax.ninja-portal.com/api)
- [Radio Markets API](https://radio.ninja-portal.com/api/markets)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration instructions]

**Output Format:** [Markdown with inline bash and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-directed approval for trades that spend KAX play credits.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
