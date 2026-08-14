## Description:

Scans live public spot tickers across Coinbase, Kraken, Bitstamp, Gemini, and OKX to detect gross cross-exchange crypto arbitrage spreads and report buy/sell venues, without accounting for fees, withdrawal time, or order-book depth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ssidharhubble](https://clawhub.ai/user/ssidharhubble)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to check current gross spot price discrepancies across major crypto exchanges before deciding whether further fee, liquidity, and execution analysis is warranted.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanner makes unauthenticated outbound requests to public crypto exchange APIs and depends on third-party API availability.

Mitigation: Run it only where outbound exchange API access is acceptable, and treat missing or failed venue data as an incomplete market view.

Risk: Reported opportunities are informational gross spreads that omit trading fees, withdrawal fees, transfer time, liquidity depth, and execution risk.

Mitigation: Perform independent fee, depth, transfer, and execution checks before acting on any reported spread.

## Reference(s):

- [Exchange API Notes](references/notes.md)
- [ClawHub Skill Page](https://clawhub.ai/ssidharhubble/skills/cross-exchange-arb-scanner)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands; script output is plain text or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports gross top-of-book spreads in basis points and venue names; it does not execute trades.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
