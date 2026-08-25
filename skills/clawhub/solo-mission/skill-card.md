## Description:

Solo Mission helps an agent create and monitor SOLO Mission Platform work, hire humans, manage conversations, fund or recover Base Sepolia escrow, and settle participant rewards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wj-solo](https://clawhub.ai/user/wj-solo)

### License/Terms of Use:

MIT-0

## Use Case:

External operators and developers use this skill to run SOLO Mission Platform workflows end to end, including mission creation, participant hiring, conversation management, media review, and reward settlement through manual transfer or Base Sepolia escrow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct an agent to operate SOLO missions end to end, including external API calls, participant actions, mission settlement, and mission-wide changes.

Mitigation: Require operator review and explicit confirmation before creating, settling, cancelling, refunding, or otherwise applying mission-wide actions.

Risk: On-chain flows require Sponsor wallet signing authority and may expose funds to incorrect or premature transactions.

Mitigation: Use a dedicated Base Sepolia testnet wallet, avoid reusing wallet secrets, prefer a managed signer or hardware/KMS boundary, and confirm every on-chain transaction before signing.

Risk: Private keys or wallet secrets could be mishandled if provided through chat or stored insecurely.

Mitigation: Do not paste private keys into chat; provide wallet credentials only through environment or signer configuration, and stop execution when required signing variables are missing.

Risk: Media review workflows can upload local media paths selected by the agent or operator.

Mitigation: Review each media file path before upload and confirm that the files are intended for the mission.

Risk: Interrupted sessions can leave on-chain missions requiring refund or recovery actions.

Mitigation: Run the documented session-start scan for stuck missions and resolve required sponsor actions before starting new work.

## Reference(s):

- [SOLO Mission Platform skill page](https://clawhub.ai/wj-solo/skills/solo-mission)
- [SOLO Mission Platform API](https://api.mission.projectsolo.ai)
- [SOLO Mission Platform site](https://solomission.ai)
- [REST API Reference](references/rest-api.md)
- [On-Chain Reference](references/onchain.md)
- [Stuck Mission Recovery](references/stuck-recovery.md)
- [Wallet Setup](references/wallet-setup.md)
- [Base Sepolia RPC](https://sepolia.base.org)
- [Circle Faucet](https://faucet.circle.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples and inline bash, curl, jq, and Foundry cast commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce mission state guidance, API request bodies, wallet setup steps, and transaction command sequences for operator review.]

## Skill Version(s):

1.1.11 (source: ClawHub release metadata; artifact frontmatter version: 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
