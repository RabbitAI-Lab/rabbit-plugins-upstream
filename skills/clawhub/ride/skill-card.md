## Description:

Ambient Ride skill for TADA/Throo ride-hailing and taxi service. Wallet, USDC bridge status and recovery, deposit, collateral, ride, payment, chat, and tipping workflows; use it for wallet balances, starting and resuming USDC bridges, and bridge progress.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambprotocol](https://clawhub.ai/user/ambprotocol)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill through supported agents to search, book, pay for, monitor, chat during, and tip for TADA/Throo rides. It also guides wallet setup, USDC bridge recovery, and collateral flows for users who choose crypto payment.

### Deployment Geography for Use:

New York City, Singapore, Phnom Penh, Siem Reap, Sihanoukville, and Kampot.

## Known Risks and Mitigations:

Risk: The skill can book rides and initiate card or wallet payment flows.

Mitigation: Use host-level command approvals for ride booking, payment, wallet transactions, and any action that moves funds or commits travel.

Risk: Local state can include ride records, logs, diagnostics, and built-in wallet recovery material.

Mitigation: Protect the configured state directory, use the wallet passphrase controls, and avoid debug logging unless needed for troubleshooting.

Risk: Installation uses a mutable global CLI and the ride relay can run as a background process.

Mitigation: Install only when the publisher is trusted, require explicit approval for install and background relay commands, and monitor or stop relays when a ride workflow ends.

Risk: Optional webhook and Telegram sinks can send ride details outside the local agent session.

Mitigation: Enable notification sinks only after user consent, use trusted endpoints or chats, and configure webhook signing secrets when webhooks are used.

Risk: Ride, place, payment, wallet, and telemetry operations share relevant trip or account data with external services.

Mitigation: Use the skill only when the user accepts those data flows and avoid saving sensitive places unless the user wants faster repeat rides.

## Reference(s):

- [Ambient Ride repository](https://github.com/mvlchain/ambient-ride-skill)
- [TADA/Throo Ride Skill Usage Guide](references/usage.md)
- [Ride Reference](references/ride.md)
- [Wallet & Authentication Reference](references/wallet.md)
- [Explicit member payments](references/member-payment.md)
- [Chat Reference](references/chat.md)
- [Tip Reference](references/tip.md)
- [TADA](https://tada.global)
- [Throo](https://ridethroo.ai)
- [x402 payment standard](https://www.x402.org)
- [Privy](https://privy.io)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented CLI results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts for user approval before install, payment, wallet, and ride-booking actions.]

## Skill Version(s):

1.5.0 (source: frontmatter, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
