## Description:

Solo Mission helps agents create and manage SOLO Mission Platform work, including human hiring, conversations, media uploads, Base Sepolia and Solana escrow funding, settlement, and refund recovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wj-solo](https://clawhub.ai/user/wj-solo)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use this skill to run SOLO Mission Platform workflows, hire humans for tasks, manage participant conversations, and coordinate off-chain or escrow-backed payouts. It is suited to agents that need guided API, wallet, and recovery procedures for mission operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can authorize wallet signing and escrow operations for SOLO missions.

Mitigation: Use a dedicated low-balance wallet and prefer hardware, KMS, or managed signing instead of raw PRIVATE_KEY use.

Risk: The skill may persist API credentials or local settings used by the agent.

Mitigation: Treat .claude/settings.local.json and any SOLO_AGENT_KEY storage as secret-bearing material that must not be committed or shared.

Risk: The skill supports external media uploads and participant interactions.

Mitigation: Keep uploads in an explicit staging folder and review mission actions before allowing automated marketplace operations.

Risk: The security review marks the release as suspicious because it combines several high-authority operations.

Mitigation: Install only after reviewing the requested authority over missions, participant communications, uploads, and escrow recovery.

## Reference(s):

- [SOLO Mission Skill Page](https://clawhub.ai/wj-solo/skills/solo-mission)
- [SOLO Mission Platform API](https://api.mission.projectsolo.ai)
- [SOLO Mission Platform](https://solomission.ai)
- [REST API Reference](references/rest-api.md)
- [On-Chain Reference](references/onchain.md)
- [Solana Wallet Reference](references/solana-wallet.md)
- [Stuck Mission Recovery](references/stuck-recovery.md)
- [Wallet Setup](references/wallet-setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API Calls, JSON]

**Output Format:** [Markdown guidance with shell commands, API request examples, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local mission state and secret-bearing local settings when used by an agent.]

## Skill Version(s):

1.1.13 (source: server release metadata; skill frontmatter metadata.version is 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
