## Description:

Guides agents through OKX Earn CLI workflows for checking balances, browsing Earn products, and preparing confirmed live account actions for Simple Earn, Flash Earn, On-chain Earn, Dual Investment, and AutoEarn.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents managing OKX Earn accounts use this skill to select appropriate okx CLI commands, review balances and product options, and handle confirmed subscribe, redeem, rate-setting, staking, Dual Investment, and AutoEarn workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide live OKX Earn actions that affect real account funds.

Mitigation: Install only when live OKX Earn account automation is intended, use a least-privilege OKX profile, and require explicit user confirmation before write commands.

Risk: Dual Investment purchases may be complex and have a confirmation gap.

Mitigation: Before any quote-and-buy command, require the assistant to restate product ID, amount, currency, yield, term, conversion and settlement outcomes, then obtain a clear yes/no confirmation.

Risk: Long-running monitor commands can continue after they are no longer needed.

Mitigation: Stop any /loop monitors when monitoring is complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-cex-earn)
- [Publisher profile](https://clawhub.ai/user/searchworld)
- [OKX](https://www.okx.com)
- [AutoEarn command reference](references/autoearn-commands.md)
- [Dual Investment command reference](references/dcd-commands.md)
- [Flash Earn command reference](references/flash-earn-commands.md)
- [On-chain Earn command reference](references/onchain-commands.md)
- [Savings command reference](references/savings-commands.md)
- [Workflow reference](references/workflows.md)
- [Response template reference](references/templates.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses JSON output from okx CLI queries when presenting account and product data.]

## Skill Version(s):

1.4.8 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
