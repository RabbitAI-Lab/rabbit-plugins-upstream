## Description:

Expose a local @moneydevkit/agent-wallet as a Nostr Wallet Connect (NIP-47) wallet-service for a systemd user service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kristapsk](https://clawhub.ai/user/kristapsk)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run a self-hosted Nostr Wallet Connect bridge that lets NWC clients request invoices or payments from a local self-custodial Lightning wallet.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bridge is a remotely reachable wallet control surface, and any valid NWC URI can authorize wallet queries, invoice creation, or spending.

Mitigation: Keep state.json and generated NWC URIs secret, use tiny budgets, and deploy only where the operator is prepared to manage wallet-access credentials.

Risk: Auto-registration can add unknown Nostr pubkeys as authorized connections when enabled.

Mitigation: Keep NWC_AUTO_REGISTER disabled for normal use and create explicit connections with known clients.

Risk: The security evidence says the documented receive/send permission split is not enforced by the code.

Mitigation: Do not rely on connection names as spending controls until allow_methods is checked before wallet actions; review permissions manually and limit funds at risk.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kristapsk/skills/agent-wallet-nwc-bridge)
- [README.md](README.md)
- [SKILL.md](SKILL.md)
- [nwc.env.example](nwc.env.example)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JavaScript, systemd unit, and environment configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes operational security guidance for NWC secrets, budgets, and auto-registration.]

## Skill Version(s):

1.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
