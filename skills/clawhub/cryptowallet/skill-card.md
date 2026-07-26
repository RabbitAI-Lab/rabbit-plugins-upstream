## Description: <br>
CryptoWallet provides agent-facing commands to create or import EVM and Solana wallets, check balances, send tokens, and interact with smart contracts using encrypted local key storage. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gnufoo](https://clawhub.ai/user/gnufoo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and Web3 operators use this skill to manage multi-chain wallet workflows, including wallet creation, balance checks, token transfers, and smart contract interactions across EVM networks and Solana. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can store private keys and broadcast irreversible blockchain transactions. <br>
Mitigation: Use testnets or small balances first, and manually verify every recipient address, network, token contract, amount, ABI, and contract function before running write commands. <br>
Risk: Private keys, wallet passwords, or transaction parameters entered directly in shell commands can be exposed through shell history, logs, or screenshots. <br>
Mitigation: Avoid placing real private keys or passwords directly in command lines; prefer safer local secret entry patterns and keep command output private. <br>
Risk: Public or untrusted RPC endpoints and unpinned dependencies can affect reliability, privacy, and repeatability. <br>
Mitigation: Use trusted or self-controlled RPC endpoints for important operations and pin reviewed dependency versions before production use. <br>
Risk: The security scan reports that some documentation overstates the skill's support and that strong confirmation safeguards are limited. <br>
Mitigation: Review the artifact behavior before installation, treat unsupported wallet features as unavailable, and add an explicit human confirmation step before any transaction-signing workflow. <br>


## Reference(s): <br>
- [Network Configuration](references/networks.json) <br>
- [Security Best Practices](references/security.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/gnufoo/skills/cryptowallet) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may create encrypted local wallet files and may broadcast blockchain transactions when write operations are run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
