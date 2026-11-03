## Description:

Manages OKX Simple Earn, Flash Earn, On-chain Earn, Dual Investment, and AutoEarn through the okx CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[okx-retail](https://clawhub.ai/user/okx-retail)

### License/Terms of Use:

MIT

## Use Case:

OKX users can use the skill to review earn balances, rates, products, and orders, and to manage subscriptions, redemptions, and AutoEarn settings through the okx CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Instructions to use live mode without mentioning it could leave users unaware that real funds are involved.

Mitigation: Identify the live account and product, amount, and consequences before acting, and obtain explicit user approval for each transaction.

Risk: Contradictory redemption instructions could cause an investment to be redeemed before the user approves the action.

Mitigation: Use read-only information for previews, pause if instructions conflict, and require approval before executing a redemption.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/okx-retail/skills/okx-cex-earn)
- [OKX website](https://www.okx.com)
- [Simple Earn command reference](artifact/references/savings-commands.md)
- [Dual Investment command reference](artifact/references/dcd-commands.md)
- [On-chain Earn command reference](artifact/references/onchain-commands.md)
- [AutoEarn command reference](artifact/references/autoearn-commands.md)
- [Flash Earn command reference](artifact/references/flash-earn-commands.md)
- [Multi-step workflows](artifact/references/workflows.md)
- [Response templates](artifact/references/templates.md)

## Skill Output:

**Output Type(s):** [Shell commands, Markdown, Guidance]

**Output Format:** [Markdown summaries and tables with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Authenticated results may include account balances and earn orders; write commands can move funds into or out of earn products.]

## Skill Version(s):

1.5.0 (source: ClawHub release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
