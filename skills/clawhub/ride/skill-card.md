## Description:

Ambient Ride skill for TADA/Throo ride-hailing and taxi service. Wallet, deposit, collateral, ride, payment, chat, and tipping workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambprotocol](https://clawhub.ai/user/ambprotocol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use Ambient Ride to arrange TADA/Throo rides in supported cities, including wallet setup, ride search, booking, payment, driver chat, and tipping.

### Deployment Geography for Use:

New York City, United States, and Singapore

## Known Risks and Mitigations:

Risk: The skill can install a payment-capable CLI and initiate booking, payment, tipping, deposit, and bridge-transfer actions.

Mitigation: Install only from the trusted Ambient/TADA publisher and keep host-level command approval enabled for installer runs and money-moving actions.

Risk: The skill stores local wallet-related material and ride state under the Ambient state directory.

Mitigation: Protect the Ambient state directory like wallet or password-manager data and avoid unnecessary sharing or backup exposure.

Risk: Configured external notification or webhook channels can receive ride details.

Mitigation: Set notification and webhook variables only when those destinations are intended to receive ride information.

Risk: MetaMask MVL deposits may involve max-token-allowance behavior.

Mitigation: Review the allowance behavior before using MetaMask MVL deposits and rely on explicit approval for deposit steps.

## Reference(s):

- [Ambient Ride GitHub Homepage](https://github.com/mvlchain/ambient-ride-skill)
- [Usage Guide](references/usage.md)
- [Ride Reference](references/ride.md)
- [Wallet & Authentication Reference](references/wallet.md)
- [Chat Reference](references/chat.md)
- [Tip Reference](references/tip.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with inline shell commands and JSON command-output interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent output may include clickable authentication links, ride status updates, payment confirmations, and user-facing prompts for approvals.]

## Skill Version(s):

1.3.0 (source: frontmatter, package.json, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
