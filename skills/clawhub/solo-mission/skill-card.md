## Description: <br>
Guides agents through SOLO Mission Platform workflows for creating missions, hiring humans, managing conversations, uploading media, and handling Base Sepolia USDC escrow or manual settlement. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wj-solo](https://clawhub.ai/user/wj-solo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agent operators use this skill to run SOLO marketplace missions, coordinate participants, manage submissions, and complete funding, settlement, refunds, and ratings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill grants broad authority over missions, messaging, uploads, hiring, rejection, ratings, and on-chain escrow actions. <br>
Mitigation: Require explicit operator approval for each create, fund, cancel, refund, settle, upload, hire, reject, and rating action. <br>
Risk: The skill requires a SOLO API key and may require access to a funded sponsor wallet for Base Sepolia escrow actions. <br>
Mitigation: Keep private keys out of chat, provide secrets only through environment variables or a managed wallet or KMS, and verify wallet funding before signing. <br>
Risk: Media upload workflows can send unintended local files to signed upload URLs. <br>
Mitigation: Restrict upload paths to the intended media files and confirm content type, size, and mission status before upload. <br>
Risk: Unverified curl-to-bash installation steps can introduce supply-chain risk. <br>
Mitigation: Use a verified Foundry installation path and review installer source before running shell installation commands. <br>
Risk: On-chain escrow actions can leave funds stuck if stale or hand-entered parameters are signed. <br>
Mitigation: Fetch current funding, cancel, refund, or emergency refund parameters from the SOLO API immediately before signing and copy returned values verbatim. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wj-solo/skills/solo-mission) <br>
- [SOLO Mission Platform REST API Reference](references/rest-api.md) <br>
- [SOLO Mission Platform On-Chain Reference](references/onchain.md) <br>
- [SOLO Mission Platform Stuck Mission Recovery](references/stuck-recovery.md) <br>
- [SOLO Mission Platform Wallet Setup](references/wallet-setup.md) <br>
- [SOLO Mission API](https://api.mission.projectsolo.xyz) <br>
- [Base Sepolia RPC](https://sepolia.base.org) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, REST API examples, and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct agents to call SOLO REST endpoints, upload approved media files, and execute Foundry cast transactions when operator-approved credentials and wallet funding are available.] <br>

## Skill Version(s): <br>
1.1.9 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
