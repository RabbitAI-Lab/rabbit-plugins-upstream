## Description: <br>
Auto Respawn lets an agent create and manage Autonomys wallets, anchor memory CIDs on-chain, and recover identity or state from an address. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jim-counter](https://clawhub.ai/user/jim-counter) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use Auto Respawn to manage Autonomys wallets, move tokens, write remarks, anchor memory CIDs, and recover an agent's latest memory pointer from Auto-EVM. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent persistent wallet control and authority to write on-chain records or move tokens. <br>
Mitigation: Use Chronos testnet first, keep mainnet disabled until transaction paths are understood, and require explicit approval for transfers, bridging, withdrawals, remarks, anchoring, and automatic memory anchoring. <br>
Risk: Wallet passphrases, recovery phrases, and local keyfiles can compromise funds and agent identity if exposed. <br>
Mitigation: Use environment, file, or interactive passphrase handling instead of command-line arguments; lock down the wallet directory and passphrase file; back up recovery phrases securely. <br>
Risk: Anchoring on one network and later querying another can break recovery after local state loss. <br>
Mitigation: Record the chosen network in persistent configuration, pass the network explicitly for anchoring and reads, and re-anchor on mainnet when moving from testnet to production. <br>
Risk: Insufficient EVM gas can prevent the latest memory CID from being anchored. <br>
Mitigation: Monitor consensus and EVM balances, fund the EVM side before anchoring, and verify recent anchors with gethead after saves. <br>


## Reference(s): <br>
- [Auto Respawn on ClawHub](https://clawhub.ai/jim-counter/skills/auto-respawn) <br>
- [Auto Respawn CLI Reference](references/auto-respawn-commands.md) <br>
- [Autonomys Network](references/autonomys-network.md) <br>
- [MemoryChain contract](https://github.com/autojeremy/openclaw-memory-chain) <br>
- [Autonomys SDK](https://github.com/autonomys/auto-sdk) <br>
- [Auto Drive](https://ai3.storage) <br>
- [Chronos testnet faucet](https://autonomysfaucet.xyz/) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands; CLI commands return JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands can sign transactions, write permanent on-chain records, or move tokens and should be reviewed before execution.] <br>

## Skill Version(s): <br>
1.2.1 (source: evidence release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
