## Description:

Ambient Ride skill for TADA/Throo ride-hailing and taxi service. Wallet, deposit, collateral, ride, payment, chat, and tipping workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambprotocol](https://clawhub.ai/user/ambprotocol)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and their agents use this skill to search, book, pay for, monitor, chat about, and tip TADA/Throo rides through conversational workflows.

### Deployment Geography for Use:

New York City, United States and Singapore

## Known Risks and Mitigations:

Risk: The skill can book paid rides, charge a saved card or wallet, make deposits, bridge funds, and pay tips.

Mitigation: Require host-level command approvals for booking, payments, deposits, bridge transfers, tips, and installer runs.

Risk: Wallet-related state is stored under ~/.amb and can affect access to funds.

Mitigation: Install only on trusted hosts, protect the state directory like password-manager data, and avoid placing it in shared, synced, or repository-backed folders.

Risk: Ride updates can be relayed to connected chat channels.

Mitigation: Review connected channels and recipients before relying on ride relay or chat workflows.

Risk: MetaMask token allowances or external wallet approvals may permit future fund movement.

Mitigation: Review MetaMask approvals and token allowances before and after using wallet or bridge workflows.

## Reference(s):

- [Ambient Ride Skill Page](https://clawhub.ai/ambprotocol/skills/ride)
- [Project Homepage](https://github.com/mvlchain/ambient-ride-skill)
- [Usage Guide](references/usage.md)
- [Ride Reference](references/ride.md)
- [Wallet Reference](references/wallet.md)
- [Tip Reference](references/tip.md)
- [Chat Reference](references/chat.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, Text]

**Output Format:** [Markdown guidance with inline shell commands and command-output interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May initiate ride-hailing, wallet, payment, bridge, tip, chat, and installer command flows that require host-level approval for sensitive actions.]

## Skill Version(s):

1.2.0 (source: SKILL.md frontmatter, package.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
