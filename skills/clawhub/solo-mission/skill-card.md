## Description:

Guides an agent through SOLO Mission Platform workflows for creating missions, hiring humans, managing conversations, handling Solana escrow or legacy Base escrow recovery, settling missions, refunding stuck funds, and rating participants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wj-solo](https://clawhub.ai/user/wj-solo)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and operators use this skill to run SOLO marketplace missions end to end, including participant recruitment, mission state tracking, payment setup, escrow settlement, and recovery actions when funds or missions are stuck.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct autonomous hiring and payment workflows, including escrow funding, settlement, and refund actions.

Mitigation: Install only when an agent is intended to manage SOLO missions and payment workflows, and require operator review before funding, settlement, or refund transactions.

Risk: Wallet guidance may expose funds if raw private keys are available to the agent process or pasted into chat.

Mitigation: Use a managed wallet, hardware-backed signer, KMS, or another signing boundary instead of exposing raw private keys to the agent process.

Risk: Installer snippets and local agent settings may create supply-chain or secret-handling exposure.

Mitigation: Avoid curl-to-shell installers where possible and protect `.claude/settings.local.json` because it can store the SOLO agent key.

Risk: The security review flags contradictory media-review Solana/Base funding instructions.

Mitigation: Manually review and correct media-review funding steps before use, especially where Solana and legacy Base flows intersect.

## Reference(s):

- [SOLO Mission Platform Skill](https://clawhub.ai/wj-solo/skills/solo-mission)
- [REST API Reference](references/rest-api.md)
- [Solana Wallet Reference](references/solana-wallet.md)
- [Stuck Mission Recovery](references/stuck-recovery.md)
- [Legacy Base On-Chain Reference](references/onchain.md)
- [Legacy Base Wallet Setup](references/wallet-setup.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON payloads and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce API request bodies, local state-file updates, wallet setup guidance, and transaction or refund procedure steps.]

## Skill Version(s):

1.1.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
