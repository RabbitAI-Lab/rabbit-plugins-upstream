## Description:

Helps users review and manage OKX Earn balances, savings, staking, Dual Investment, Flash Earn, and AutoEarn through the OKX CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[okx-retail](https://clawhub.ai/user/okx-retail)

### License/Terms of Use:

MIT-0

## Use Case:

OKX users and their agents use this skill to compare Earn products, check holdings, and, with authorization, subscribe, redeem, or change earning settings on a live account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Earn purchases, redemptions, transfers, and AutoEarn changes can affect real funds without clear final consent.

Mitigation: Before every live account action, show the amount, asset, product, and consequences; obtain separate explicit confirmation after that summary.

Risk: The Dual Investment workflow can execute a purchase immediately after obtaining a quote.

Mitigation: Do not treat a request to proceed as final consent; show the live purchase terms and obtain a separate confirmation before execution.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/okx-retail/skills/okx-cex-earn)
- [OKX](https://www.okx.com)
- [Simple Earn command reference](references/savings-commands.md)
- [Dual Investment command reference](references/dcd-commands.md)
- [On-chain Earn command reference](references/onchain-commands.md)
- [AutoEarn command reference](references/autoearn-commands.md)
- [Flash Earn command reference](references/flash-earn-commands.md)
- [Earn workflows](references/workflows.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Analysis]

**Output Format:** [Markdown summaries, tables, and confirmation prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live account actions require explicit user confirmation.]

## Skill Version(s):

1.4.9 (source: skill metadata and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
