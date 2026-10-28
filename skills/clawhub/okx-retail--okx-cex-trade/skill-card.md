## Description:

Helps agents manage OKX spot, swap, futures, options, and event-contract orders, positions, and trading controls through the OKX CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[okx-retail](https://clawhub.ai/user/okx-retail)

### License/Terms of Use:

MIT-0

## Use Case:

Traders and their authorized agents use this skill to prepare, confirm, execute, and check OKX orders across spot and derivatives markets, including event contracts. It requires configured credentials and a selected live or demo trading mode.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live orders, leverage changes, position closes, or cancellations can affect real funds.

Mitigation: Start in demo mode and explicitly review each action and its trading mode before approval.

Risk: Trading requires access to OKX credentials.

Mitigation: Configure credentials through the OKX setup flow rather than sharing them in chat.

Risk: Troubleshooting trading errors may inspect adjacent account settings or active bots.

Mitigation: Limit such checks to the reported issue and require explicit approval before changing orders, positions, or bots.

## Reference(s):

- [OKX website](https://www.okx.com)
- [ClawHub skill release](https://clawhub.ai/okx-retail/skills/okx-cex-trade)
- [Trading workflows](artifact/references/workflows.md)
- [Command and output conventions](artifact/references/templates.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text and Markdown with OKX CLI commands and order confirmations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Labels trading mode and checks order results after writes.]

## Skill Version(s):

1.4.9 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
