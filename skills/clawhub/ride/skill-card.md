## Description:

Ambient Ride skill for TADA/Throo ride-hailing and taxi service. Wallet, USDC bridge status and recovery, deposit, collateral, ride, payment, chat, and tipping workflows; use it for wallet balances, starting and resuming USDC bridges, and bridge progress.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambprotocol](https://clawhub.ai/user/ambprotocol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use Ambient Ride to search, book, pay for, monitor, chat about, and tip for real TADA/Throo rides through an agent. Developers and agent operators can also use it to configure wallet, bridge, deposit, collateral, and notification workflows around those rides.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install and delegate to a global Ambient CLI.

Mitigation: Require explicit installation approval and host-level command approvals for amb commands.

Risk: The skill can store and use persistent wallet and payment authority under the user's local state directory.

Mitigation: Avoid the built-in wallet on shared or synced machines and keep the local passphrase and state directory private.

Risk: The skill can perform real ride, card, wallet, bridge, deposit, and tip actions.

Mitigation: Review each action that spends money, moves funds, books a ride, or changes payment authority before approving it.

Risk: Optional webhook or Telegram notifications can send ride-related information to external destinations.

Mitigation: Enable notifications only for destinations the operator trusts and protect webhook secrets and bot tokens.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ambprotocol/skills/ride)
- [Ambient Ride homepage](https://github.com/mvlchain/ambient-ride-skill)
- [Usage reference](references/usage.md)
- [Ride reference](references/ride.md)
- [Wallet reference](references/wallet.md)
- [Chat reference](references/chat.md)
- [Tip reference](references/tip.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with CLI commands, links, status summaries, and user-facing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May trigger real ride, payment, wallet, bridge, deposit, tip, chat, notification, and background relay actions after user approval.]

## Skill Version(s):

1.4.0 (source: frontmatter, package.json, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
