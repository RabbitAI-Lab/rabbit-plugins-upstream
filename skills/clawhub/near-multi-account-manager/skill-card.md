## Description: <br>
Secure multi-account management for NEAR Protocol with encrypted credential storage, account switching, and balance aggregation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shaiss](https://clawhub.ai/user/shaiss) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, organizations, traders, DeFi users, and advanced NEAR users use this skill to manage multiple NEAR accounts, switch active accounts, check balances, transfer NEAR, and export account metadata without private keys. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores NEAR wallet private keys for managed accounts. <br>
Mitigation: Use only accounts appropriate for this risk profile and set a strong, unique NEAR_SKILL_KEY before adding any account. <br>
Risk: Transfer actions can move real NEAR on mainnet. <br>
Mitigation: Review every transfer request, amount, recipient, and active account before execution; prefer low-value test accounts until behavior is verified. <br>
Risk: The artifact includes unrelated authenticated marketplace scripts and an exposed token. <br>
Mitigation: Remove the unrelated market.near.ai scripts and revoke the exposed token before installing or redistributing the skill. <br>
Risk: Required capabilities are not declared even though the skill performs local file storage and network blockchain operations. <br>
Mitigation: Require explicit capability review for local file access, NEAR RPC access, and transaction submission before deployment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/shaiss/skills/near-multi-account-manager) <br>
- [NEAR Mainnet Explorer](https://explorer.mainnet.near.org) <br>


## Skill Output: <br>
**Output Type(s):** [text, configuration, shell commands, JSON] <br>
**Output Format:** [Agent-facing text and structured JSON-like results from NEAR account operations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read and write local encrypted account storage and may submit NEAR mainnet transactions when transfer actions are invoked.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
