## Description:

Helps agents manage OKX Earn products through the okx CLI, including Simple Earn, Flash Earn, On-chain Earn, Dual Investment, and AutoEarn.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect OKX Earn balances and products, prepare authenticated okx CLI commands, and manage subscriptions, redemptions, rate settings, structured Dual Investment products, on-chain earn positions, and AutoEarn behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can authorize live OKX Earn actions that move, lock, lend, redeem, or otherwise affect funds.

Mitigation: Require the agent to show the exact product, amount, currency, account source, lockup or redemption terms, and live-account effect before execution, then wait for explicit confirmation.

Risk: Dual Investment can convert principal and yield at settlement, and early redemption depends on live quote and redemption-window behavior.

Mitigation: Explain trigger scenarios, settlement currency, indicative yield, live quote effects, and redemption windows before any Dual Investment purchase or early redemption.

Risk: AutoEarn and recurring monitors can repeatedly access portfolio data or enable ongoing earn behavior.

Mitigation: Confirm the currency, earn type, idle-fund effect, and 24-hour disable restriction before enabling AutoEarn; keep recurring monitors read-only until a separate execution confirmation is given.

## Reference(s):

- [OKX homepage](https://www.okx.com)
- [Simple Earn command reference](artifact/references/savings-commands.md)
- [Dual Investment command reference](artifact/references/dcd-commands.md)
- [On-chain Earn command reference](artifact/references/onchain-commands.md)
- [AutoEarn command reference](artifact/references/autoearn-commands.md)
- [Flash Earn command reference](artifact/references/flash-earn-commands.md)
- [Multi-step workflows](artifact/references/workflows.md)
- [Response templates and formatting reference](artifact/references/templates.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and rendered tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses JSON CLI output for authenticated reads and requires explicit confirmation before write actions.]

## Skill Version(s):

1.4.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
