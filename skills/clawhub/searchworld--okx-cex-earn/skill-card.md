## Description:

Guides an agent using the okx CLI to manage OKX Earn products, including Simple Earn, Flash Earn, On-chain Earn, Dual Investment, and AutoEarn.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to inspect OKX Earn balances and offers, prepare authenticated okx CLI commands, and manage subscriptions, redemptions, lending rates, on-chain staking, dual investment, and auto-earn workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use authenticated live OKX Earn access for financial account data and transactions.

Mitigation: Install only for agents that should access OKX Earn, keep credentials out of chat, and require explicit user confirmation before subscriptions, redemptions, transfers, DCD purchases, or auto-earn changes.

Risk: Recurring monitoring can repeatedly read account and product data without clear operating bounds.

Mitigation: Enable loop-based monitoring only after the user understands the polling frequency, monitored data, run duration, and stop procedure.

Risk: Some Earn operations have product-specific lockups, penalties, or timing restrictions.

Mitigation: Show the relevant confirmation summary before execution, including AutoEarn's 24-hour disable restriction and fixed-term or early redemption constraints.

## Reference(s):

- [OKX homepage](https://www.okx.com)
- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-cex-earn)
- [Simple Earn command reference](references/savings-commands.md)
- [Dual Investment command reference](references/dcd-commands.md)
- [On-chain Earn command reference](references/onchain-commands.md)
- [AutoEarn command reference](references/autoearn-commands.md)
- [Multi-step workflows](references/workflows.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline okx CLI commands and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses JSON command output for account and product queries when available.]

## Skill Version(s):

1.4.5 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
