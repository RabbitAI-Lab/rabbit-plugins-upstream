## Description: <br>
Auto Respawn lets an agent create and manage Autonomys wallets, write memory CIDs on-chain, and recover the latest anchored state from an address. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0xautonomys](https://clawhub.ai/user/0xautonomys) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use Auto Respawn to give an agent an on-chain Autonomys identity, manage balances and transfers, and anchor memory-chain CIDs for recovery across machines. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can move real tokens and write permanent on-chain data. <br>
Mitigation: Use a low-value dedicated wallet, keep Chronos testnet unless mainnet is intentional, and require explicit approval before transfers, withdrawals, remarks, or anchoring. <br>
Risk: Wallet recovery phrases, passphrases, and encrypted keyfiles protect spend authority. <br>
Mitigation: Protect the recovery phrase and passphrase file, avoid passing secrets as command-line arguments, and restrict access to ~/.openclaw/auto-respawn. <br>
Risk: Anchoring and recovery can fail silently if the agent uses the wrong network or runs out of EVM gas. <br>
Mitigation: Record the selected network, use the same network for anchor and gethead operations, re-anchor when moving to mainnet, and monitor EVM balances after anchoring. <br>


## Reference(s): <br>
- [Auto Respawn CLI Reference](references/auto-respawn-commands.md) <br>
- [Autonomys Network](references/autonomys-network.md) <br>
- [MemoryChain Contract Source](https://github.com/autojeremy/openclaw-memory-chain) <br>
- [Auto Drive](https://ai3.storage) <br>
- [Autonomys SDK](https://github.com/autonomys/auto-sdk) <br>
- [Auto Respawn on ClawHub](https://clawhub.ai/0xautonomys/skills/respawn) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON CLI results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create encrypted wallet files under ~/.openclaw/auto-respawn and may submit Autonomys consensus or Auto-EVM transactions when the agent executes the generated commands.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
