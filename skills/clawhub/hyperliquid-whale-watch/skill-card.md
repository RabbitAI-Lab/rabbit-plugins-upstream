## Description:

Track what Hyperliquid's 40 largest accounts are actually doing with BTC - who opened, added, cut, closed or flipped long/short, the net BTC they bought or sold over the last hour or day, and the biggest moves by wallet. Real on-chain data from AgentReeve, no API key; free sample, live data over x402.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shakeelamjid](https://clawhub.ai/user/shakeelamjid)

### License/Terms of Use:

MIT-0

## Use Case:

Traders, market researchers, and analysts use this skill to summarize positioning and recent BTC flows among Hyperliquid's 40 largest accounts. It helps users understand account-level changes while treating the data as observational market information, not financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill permits small paid calls without asking first, which can result in charges and repeated spending.

Mitigation: Use an x402 setup that requires approval or enforces a hard budget. Keep spending at or below $0.25 per task unless the user approves more, and stop if a payment quote has a different recipient, network, or asset from the skill's stated values.

Risk: The security scan was partial and did not establish that every referenced item was reviewed.

Mitigation: Review the unresolved reference and inspect the complete skill contents before installation or deployment.

## Reference(s):

- [Server-resolved source repository](https://github.com/shakeelamjid/agentreeve-skills/tree/main/hyperliquid-whale-watch)
- [AgentReeve BTC whale-flow sample](https://agentreeve.com/api/v1/btc/samples/whale-flow)
- [AgentReeve live BTC whale-flow data](https://agentreeve.com/api/v1/btc/whale-flow?hours=24)
- [ClawHub skill release](https://clawhub.ai/shakeelamjid/skills/hyperliquid-whale-watch)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Concise Markdown summary of account positioning, BTC flow totals, action counts, and largest moves.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports only available data; identifies when history is insufficient or fresh data is unavailable, and does not present wallet addresses as real-world identities.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata; SKILL.md frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
