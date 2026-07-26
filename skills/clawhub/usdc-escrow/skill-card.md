## Description: <br>
Trustless USDC escrow for agent-to-agent payments on Base. Create, release, dispute escrows via simple commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zeroaddresss](https://clawhub.ai/user/zeroaddresss) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external agents use this skill to create, inspect, release, dispute, resolve, and reclaim USDC escrows for agent-to-agent payments on Base. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Financial actions such as create, release, dispute, resolve, and claim-expired can affect escrow state and funds. <br>
Mitigation: Require explicit human approval and verify escrow IDs, recipients, amounts, deadlines, network, and contract details before running state-changing commands. <br>
Risk: The skill depends on api.payclawback.xyz by default and may use a different real-value backend if ESCROW_API_URL is changed. <br>
Mitigation: Use only trusted API endpoints and confirm whether the configured backend targets Base Sepolia testnet or any real-value environment before execution. <br>
Risk: The security verdict is suspicious because the trust model and financial action scope are not clearly disclosed. <br>
Mitigation: Review the skill before installation and disclose backend, arbiter, network, and contract assumptions to users before operation. <br>


## Reference(s): <br>
- [USDC Escrow API Documentation](references/api-docs.md) <br>
- [Verified Base Sepolia escrow contract](https://sepolia.basescan.org/address/0x2a27844f3775c3a446d32c06f4ebc3a02bb52e04) <br>
- [USDC Escrow on ClawHub](https://clawhub.ai/zeroaddresss/skills/usdc-escrow) <br>
- [zeroaddresss publisher profile](https://clawhub.ai/user/zeroaddresss) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands require curl and jq; ESCROW_API_URL can override the default escrow API backend.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
