## Description: <br>
GhostBot ACLM helps agents guide users through Sepolia Uniswap v4 concentrated liquidity management, including status checks, positions, oracle signals, pool stats, and wallet-signed testnet liquidity actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aqiljaafree](https://clawhub.ai/user/aqiljaafree) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and DeFi operators use this skill to inspect and manage Sepolia Uniswap v4 ACLM positions from chat. It can run viem scripts to read contract state and submit testnet transactions for liquidity and oracle-signal workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can submit wallet-signed transactions through add-liquidity and post-signal scripts. <br>
Mitigation: Use only a throwaway Sepolia wallet and confirm the RPC network, wallet address, contract addresses, token amounts, approvals, tick range, autoRebalance setting, and oracle signal details before execution. <br>
Risk: Private key environment variables are required for wallet-backed script execution. <br>
Mitigation: Never use a mainnet or valuable private key; scope DEPLOYER_PRIVATE_KEY to a test wallet and rotate it if exposed. <br>
Risk: Automated liquidity, approval, and oracle-signal actions may behave unexpectedly if pointed at the wrong network or contracts. <br>
Mitigation: Verify Sepolia chain ID 11155111, Etherscan contract addresses, and transaction links before treating script output as successful. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aqiljaafree/skills/ghostbot-aclm) <br>
- [OpenClawACLMHook on Sepolia Etherscan](https://sepolia.etherscan.io/address/0xbD2802B7215530894d5696ab8450115f56b1fAC0) <br>
- [OpenClawOracle on Sepolia Etherscan](https://sepolia.etherscan.io/address/0x300Fa0Af86201A410bEBD511Ca7FB81548a0f027) <br>
- [Architecture reference](artifact/references/architecture.md) <br>
- [Contracts reference](artifact/references/contracts.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, code, guidance] <br>
**Output Format:** [Markdown responses with shell commands, configuration snippets, status summaries, and transaction links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require RPC_URL and DEPLOYER_PRIVATE_KEY environment variables for viem-based Sepolia reads and wallet-signed transactions.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
