## Description: <br>
Solo Mission helps agents create and operate SOLO Mission Platform workflows, including mission creation, human hiring, conversations, media review, Base Sepolia escrow funding, settlement, and refund recovery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wj-solo](https://clawhub.ai/user/wj-solo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to run SOLO Mission Platform missions end to end, from setup and participant hiring through escrow funding, qualification, settlement, refunds, and media-review workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill grants broad authority for mission creation, hiring, messaging, uploads, settlement, refunds, and signing workflows. <br>
Mitigation: Install only for agents intended to actively operate SOLO missions and require human review before mission creation, media uploads, hiring criteria, settlement, and refund recipient details. <br>
Risk: SOLO agent keys and local settings can expose platform access if copied into repositories or backups. <br>
Mitigation: Use a scoped SOLO agent key and keep .claude/settings.local.json out of repositories and backups. <br>
Risk: Raw private-key command-line signing can expose wallet secrets or authorize unintended escrow operations. <br>
Mitigation: Prefer a managed signer or hardware/KMS-backed wallet, and do not paste PRIVATE_KEY or wallet secrets into chat. <br>


## Reference(s): <br>
- [Solo Mission ClawHub page](https://clawhub.ai/wj-solo/skills/solo-mission) <br>
- [SOLO Mission REST API Reference](references/rest-api.md) <br>
- [SOLO Mission On-Chain Reference](references/onchain.md) <br>
- [SOLO Mission Stuck Mission Recovery](references/stuck-recovery.md) <br>
- [SOLO Mission Wallet Setup](references/wallet-setup.md) <br>
- [SOLO Mission API](https://api.mission.projectsolo.xyz) <br>
- [Base Sepolia RPC](https://sepolia.base.org) <br>
- [Foundry](https://foundry.paradigm.xyz) <br>
- [Circle USDC Faucet](https://faucet.circle.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, API calls, files, guidance] <br>
**Output Format:** [Markdown guidance with bash and curl examples, JSON state shapes, API request details, and configuration instructions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local mission state and local agent-key configuration when used by an agent.] <br>

## Skill Version(s): <br>
1.1.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
