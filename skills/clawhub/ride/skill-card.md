## Description: <br>
Ambient Ride skill for TADA/Throo ride-hailing and taxi service. Wallet, deposit, collateral, ride, payment, chat, and tipping workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ambprotocol](https://clawhub.ai/user/ambprotocol) <br>

### License/Terms of Use: <br>
MIT No Attribution <br>


## Use Case: <br>
External users and developers use Ambient Ride to let an agent arrange TADA/Throo trips in supported markets, including ride search, booking, payment, driver chat, receipts, and tips. The skill is intended for live ride-hailing workflows where the user approves sensitive ride, wallet, and payment steps. <br>

### Deployment Geography for Use: <br>
New York, United States and Singapore <br>

## Known Risks and Mitigations: <br>
Risk: The skill can book rides, charge cards or wallets, move USDC, manage collateral, withdraw funds, bridge assets, and tip drivers. <br>
Mitigation: Use host-level confirmation gates for every ride request, tip, card charge, deposit, withdrawal, and bridge transfer. <br>
Risk: The skill stores sensitive wallet, account, ride, and movement-history state under the Ambient Ride state directory. <br>
Mitigation: Treat the state directory as sensitive, restrict access to it, and review debug bundles before sharing them. <br>
Risk: The security review notes consent and privacy gaps around live ride, wallet, account, and location data. <br>
Mitigation: Review the skill before connecting real payment cards, Privy wallets, or live ride accounts, and keep user approval explicit for sensitive actions. <br>


## Reference(s): <br>
- [Ambient Ride repository](https://github.com/mvlchain/ambient-ride-skill) <br>
- [Usage Reference](references/usage.md) <br>
- [Ride Reference](references/ride.md) <br>
- [Wallet Reference](references/wallet.md) <br>
- [Chat Reference](references/chat.md) <br>
- [Tip Reference](references/tip.md) <br>
- [TADA](https://tada.global) <br>
- [Throo](https://ridethroo.ai) <br>
- [Privy](https://privy.io) <br>
- [x402](https://www.x402.org) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Markdown, Text] <br>
**Output Format:** [Markdown and plain text with inline shell commands and CLI JSON handling guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may create local state, initiate ride actions, and return links, receipts, payment status, ride status, and driver chat updates.] <br>

## Skill Version(s): <br>
1.0.1 (source: SKILL.md frontmatter and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
