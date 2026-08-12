## Description:

Read-only Polymarket BTC 5-minute market scanner that reports candidate complementary-price edges; it never places orders, moves funds, or charges users.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whh110112](https://clawhub.ai/user/whh110112)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and market observers use this skill to run a read-only scan of Polymarket BTC 5-minute Up/Down markets and identify candidate complementary-price edges for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat candidate price edges as financial advice or guaranteed profit.

Mitigation: Present scanner output as informational market data only and require human review before any separate trading decision.

Risk: Future modifications could add wallet keys, trading credentials, order execution, billing, or secret handling.

Mitigation: Keep this skill read-only and require a separate security review before installing or using any version that adds those capabilities.

Risk: Displayed edges can be affected by fees, slippage, latency, partial fills, market rules, settlement disputes, and platform terms.

Mitigation: Review candidate edges against current market depth, fees, regional rules, and Polymarket terms before acting outside this skill.

## Reference(s):

- [Polymarket API Read-only Reference](references/api-reference.md)
- [BTC 5-minute Candidate Spread Explanation](references/trading-strategy.md)
- [ClawHub Skill Page](https://clawhub.ai/whh110112/skills/polymarket-btc-5m-arbitrage)
- [Polymarket Gamma API](https://gamma-api.polymarket.com)
- [Polymarket CLOB API](https://clob.polymarket.com)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; scanner output can be human-readable text or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only market observations for human review; no orders, payments, file writes, or secret handling.]

## Skill Version(s):

1.0.2 (source: frontmatter, config.json, changelog, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
