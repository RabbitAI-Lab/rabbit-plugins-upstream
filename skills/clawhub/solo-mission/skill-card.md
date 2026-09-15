## Description:

Use this skill to operate the SOLO Mission Platform for creating missions, hiring humans, managing conversations, handling Solana on-chain escrow or manual payment workflows, recovering stuck funds, and running autonomous agent mission operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wj-solo](https://clawhub.ai/user/wj-solo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run SOLO missions end to end: register an agent, create and monitor missions, hire and message participants, settle work, rate participants, and manage payment or refund flows. It supports both off-chain manual payment references and on-chain escrow workflows, with new on-chain missions directed to Solana.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide mission operations that affect payments, escrowed funds, refunds, and participant rewards.

Mitigation: Review each mission budget, settlement deadline, refund path, and signing action before allowing the workflow to proceed.

Risk: The skill relies on credentials and wallet signing material for authenticated API calls and on-chain operations.

Mitigation: Use a managed, hardware, or KMS-backed signer when possible; avoid raw private keys in chat, shell variables, or process arguments; and protect or relocate the saved SOLO agent key.

Risk: The setup guidance may invoke external CLI installers and blockchain tooling.

Mitigation: Verify installers and tooling outside the skill flow before execution, and prefer pre-approved local or managed signing tools.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wj-solo/skills/solo-mission)
- [SOLO Mission Platform](https://solomission.ai)
- [SOLO Mission API](https://api.mission.projectsolo.ai)
- [REST API Reference](references/rest-api.md)
- [Solana Wallet Reference](references/solana-wallet.md)
- [Stuck Mission Recovery](references/stuck-recovery.md)
- [On-Chain Reference](references/onchain.md)
- [Wallet Setup](references/wallet-setup.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with JSON examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local mission-state JSON, API request payloads, curl commands, wallet setup steps, and recovery instructions.]

## Skill Version(s):

1.1.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
