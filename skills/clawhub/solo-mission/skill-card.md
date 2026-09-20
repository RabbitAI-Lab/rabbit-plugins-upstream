## Description:

Guides agents through creating and managing SOLO Mission Platform missions, hiring participants, handling conversations, and funding or recovering on-chain escrow workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wj-solo](https://clawhub.ai/user/wj-solo)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and developers use this skill to operate SOLO Mission Platform workflows, including mission setup, participant hiring, conversation management, off-chain settlement, Solana escrow funding, and recovery of stuck on-chain missions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate autonomous marketplace, mission payment, and escrow workflows with live credentials or wallet-signing access.

Mitigation: Review before installing, use a dedicated workspace with limited mission funds, and verify every on-chain transaction path before signing.

Risk: Chain-specific funding instructions may conflict between Solana and older Base/EscrowVault paths.

Mitigation: Prefer the Solana funding tools for new missions and do not rely on the conflicting media_review Base createTask snippet for Solana missions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wj-solo/skills/solo-mission)
- [SOLO Mission Platform REST API Reference](references/rest-api.md)
- [SOLO Mission Platform Solana Wallet Reference](references/solana-wallet.md)
- [SOLO Mission Platform Stuck Mission Recovery](references/stuck-recovery.md)
- [SOLO Mission Platform On-Chain Reference](references/onchain.md)
- [SOLO Mission Platform Wallet Setup](references/wallet-setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, API calls, Configuration]

**Output Format:** [Markdown guidance with JSON examples and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include mission state updates, API request bodies, and wallet or escrow verification steps.]

## Skill Version(s):

1.1.21 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
