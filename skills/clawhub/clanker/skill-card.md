## Description: <br>
Deploy ERC20 tokens on Base using Clanker SDK. Create tokens with built-in Uniswap V4 liquidity pools. Supports Base mainnet and Sepolia testnet. Requires PRIVATE_KEY in config. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[spirosrap](https://clawhub.ai/user/spirosrap) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and token operators use this skill to prepare Clanker-based ERC20 token deployments on Base, inspect token information, and check deployment transaction status. It is intended for users who can manage wallet keys and review blockchain transactions before broadcasting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can sign irreversible blockchain transactions and spend real ETH when configured with a wallet private key. <br>
Mitigation: Use a fresh low-balance wallet, prefer Base Sepolia first, and manually review the network, signer address, ETH amount, contract action, and transaction data before broadcasting on mainnet. <br>
Risk: Private keys are stored in a local configuration file and could be exposed if the file is shared or committed. <br>
Mitigation: Protect the config file tightly, keep it outside version control, and use separate keys for testnet and mainnet. <br>
Risk: Deployment depends on current Clanker contract configuration and RPC connectivity, so stale contract or network settings may cause failed or unintended transactions. <br>
Mitigation: Verify current Clanker documentation, contract addresses, network, and gas assumptions before deployment. <br>


## Reference(s): <br>
- [Clanker Skill Page](https://clawhub.ai/spirosrap/skills/clanker) <br>
- [Clanker Homepage](https://clanker.world) <br>
- [Clanker Documentation](https://docs.clanker.world) <br>
- [Clanker SDK Reference](references/clanker-sdk.md) <br>
- [Base Mainnet Explorer](https://basescan.org) <br>
- [Base Sepolia Explorer](https://sepolia.basescan.org) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce transaction status details, token metadata, explorer links, and deployment command guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
