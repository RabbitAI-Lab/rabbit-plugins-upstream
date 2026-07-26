## Description: <br>
Register agents on the Zeru ERC-8004 Identity Registry, manage wallets and metadata, and read on-chain state on Base Mainnet or Base Sepolia. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[elitex45](https://clawhub.ai/user/elitex45) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to register Zeru/ERC-8004 agent records, inspect registry fees and agent data, and update owned agent metadata or wallet state on Base Mainnet or Base Sepolia. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write operations use a funded blockchain private key and can submit on-chain transactions. <br>
Mitigation: Use a dedicated wallet with limited funds, keep PRIVATE_KEY scoped to this skill, and prefer Base Sepolia for testing before using Base Mainnet. <br>
Risk: Registration and metadata changes can publish user-provided agent JSON or metadata through Zeru APIs and on-chain registry state. <br>
Mitigation: Review JSON files, service endpoints, ownership fields, and metadata values before registering or updating an agent. <br>
Risk: Commands may contact Zeru API services and Base RPC endpoints. <br>
Mitigation: Run the skill only when those network interactions are expected and review optional RPC_URL or CHAIN_ID overrides before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/elitex45/skills/zeruai) <br>
- [EIP-8004 registration-v1](https://eips.ethereum.org/EIPS/eip-8004) <br>
- [OASF reference](https://github.com/agntcy/oasf/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May initiate API requests, Base RPC reads, and on-chain transactions when the user runs write commands with a funded PRIVATE_KEY.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
