## Description:

Solo Mission helps an agent create and manage SOLO Mission Platform missions, hire participants, coordinate conversations, and handle off-chain or Base Sepolia escrow settlement and refund flows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wj-solo](https://clawhub.ai/user/wj-solo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external operators use this skill to run SOLO Mission Platform workflows from an agent session, including mission creation, participant hiring, conversation follow-up, media-review coordination, and payment or refund handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can manage SOLO missions, participants, conversations, local monitoring state, and media uploads through an external service.

Mitigation: Review mission parameters, participant actions, local state paths, and media file paths before allowing the agent to create, update, upload, hire, settle, or cancel.

Risk: On-chain mission flows can sign Base Sepolia escrow, refund, and emergency-refund transactions.

Mitigation: Require explicit approval for each transaction and verify the chain ID, contract address, task ID, recipient wallet, and amount before signing.

Risk: Wallet secrets could be exposed if entered into chat or stored as plaintext files.

Mitigation: Keep private keys out of chat and plaintext files, use environment or managed signing only at the signing step, and unset or rotate secrets after use.

Risk: The documented Foundry installation path uses a curl-to-bash setup command.

Mitigation: Use a verified installation method for Foundry before enabling on-chain flows.

## Reference(s):

- [SOLO Mission REST API Reference](references/rest-api.md)
- [SOLO Mission On-Chain Reference](references/onchain.md)
- [SOLO Mission Stuck Mission Recovery](references/stuck-recovery.md)
- [SOLO Mission Wallet Setup](references/wallet-setup.md)
- [SOLO Mission API](https://api.mission.projectsolo.ai)
- [SOLO Mission Platform](https://solomission.ai)
- [ClawHub Skill Page](https://clawhub.ai/wj-solo/skills/solo-mission)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May persist local mission state and call external SOLO Mission API, upload, and Base Sepolia transaction workflows when configured by the operator.]

## Skill Version(s):

1.1.10 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
