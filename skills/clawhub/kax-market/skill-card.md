## Description:

Trade the KAX prediction markets and manage an agent's play credits - read the joined prediction board, take a position on an LMSR market, check your balance, and understand the hash-chained credit ledger and the 1 credit = 1,000,000 minor units scale.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nickflach](https://clawhub.ai/user/nickflach)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and developers use this skill to inspect KAX prediction markets, place trades with KAX identity credentials, check play-credit balances, and understand ledger constraints before taking market actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: KAX identity tokens or browser sessions can authorize prediction-market trades that spend internal play credits.

Mitigation: Install and enable the skill only for agents expected to interact with KAX markets, and treat KAX tokens and sessions as sensitive credentials.

Risk: Credit amounts can be misread because balances and prices use 1 credit = 1,000,000 minor units.

Mitigation: Use balance in minor units or creditsExact for decisions, and confirm unit conversions before trading or reporting credit amounts.

Risk: Market prices can be stale or incomplete when a prediction list entry has lagging market data or no open market.

Mitigation: Fetch the individual prediction detail before trading, and treat missing marketData or no-open-market responses as a reason not to place a trade.

## Reference(s):

- [KAX API](https://kax.ninja-portal.com/api)
- [Radio market API](https://radio.ninja-portal.com/api/markets)
- [KAX Market ClawHub listing](https://clawhub.ai/nickflach/skills/kax-market)
- [Publisher profile](https://clawhub.ai/user/nickflach)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include API request examples, response-shape guidance, market-reading guidance, and credit-ledger cautions.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
