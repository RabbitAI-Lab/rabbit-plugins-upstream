## Description:

Ambient Ride skill for TADA/Throo ride-hailing and taxi service. Wallet, deposit, collateral, ride, payment, chat, and tipping workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambprotocol](https://clawhub.ai/user/ambprotocol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use Ambient Ride to let an agent search, book, pay for, monitor, chat during, and tip for TADA/Throo rides in supported cities, with member-card and wallet-based USDC payment flows.

### Deployment Geography for Use:

New York City, United States, and Singapore

## Known Risks and Mitigations:

Risk: The skill can spend real money through ride booking, wallet payment, fund bridging, deposits, withdrawals, and tips.

Mitigation: Use host-level command approval for amb commands that book rides, send transactions, bridge funds, deposit or withdraw collateral, tip, or otherwise move money.

Risk: Installation can add a global CLI and may require shell PATH changes.

Mitigation: Review installation commands before execution and require explicit approval before editing shell profile files.

Risk: Local Ambient state under ~/.amb contains wallet-related material and ride state.

Mitigation: Treat ~/.amb as sensitive local data; do not sync, publish, or share it, and protect it like credential material.

Risk: The ride relay runs in the background to stream ride and chat events.

Mitigation: Run the relay only for active rides and review host process controls so relay sessions can be stopped when no longer needed.

## Reference(s):

- [Ambient Ride on ClawHub](https://clawhub.ai/ambprotocol/skills/ride)
- [Ambient Ride homepage](https://github.com/mvlchain/ambient-ride-skill)
- [TADA/Throo Ride Skill Usage Guide](references/usage.md)
- [Ride Reference](references/ride.md)
- [Wallet & Authentication Reference](references/wallet.md)
- [Tip Reference](references/tip.md)
- [Chat Reference](references/chat.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, Text]

**Output Format:** [Markdown guidance with inline shell commands and structured command-output handling]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct an agent to run amb CLI commands for installation, wallet setup, ride booking, payment, chat, tipping, and event relay workflows.]

## Skill Version(s):

1.1.0 (source: frontmatter, package.json, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
