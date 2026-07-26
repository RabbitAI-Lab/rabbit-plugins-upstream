## Description: <br>
Manages OKX Earn products through the okx CLI, including Simple Earn, Flash Earn, On-chain Earn, Dual Investment, and AutoEarn. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[numpy0001](https://clawhub.ai/user/numpy0001) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External OKX users and agents use this skill to inspect Earn balances and products, prepare confirmed subscriptions or redemptions, set lending rates, monitor staking orders, interact with Dual Investment products, and manage AutoEarn through authenticated okx CLI commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authenticated OKX Earn actions can move or lock real funds, convert assets, stop earnings, or change live balances. <br>
Mitigation: Use only with the intended authenticated OKX profile and review each confirmation carefully before Dual Investment, on-chain staking, redemptions, transfers, or recurring Earn changes. <br>
Risk: The skill requires sensitive OKX authentication through OAuth or API-key profiles. <br>
Mitigation: Configure access through okx config init or an existing local profile; never paste API keys, secrets, or tokens into chat. <br>
Risk: Some Earn products include lockups, early-redemption limits, structured-product settlement, or on-chain protocol risk. <br>
Mitigation: Confirm product terms, settlement currency, lock period, redemption constraints, penalties, and protocol exposure before executing write commands. <br>


## Reference(s): <br>
- [OKX](https://www.okx.com) <br>
- [AutoEarn Command Reference](references/autoearn-commands.md) <br>
- [DCD Command Reference](references/dcd-commands.md) <br>
- [Flash Earn Command Reference](references/flash-earn-commands.md) <br>
- [On-chain Earn Command Reference](references/onchain-commands.md) <br>
- [Simple Earn Command Reference](references/savings-commands.md) <br>
- [Response Templates](references/templates.md) <br>
- [Earn Workflows](references/workflows.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands, confirmation summaries, and tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Query commands should use JSON output where available; write operations are presented as confirmation summaries before execution.] <br>

## Skill Version(s): <br>
1.3.8 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
