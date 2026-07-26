## Description: <br>
Deploy smart contracts and bridge assets to Abstract (ZK Stack L2). Use when an agent needs to deploy contracts on Abstract, bridge ETH/tokens to Abstract, trade/swap tokens, check balances, transfer assets, or interact with Abstract mainnet. Covers zksolc compilation, Hardhat deployment, Relay bridging, DEX trading, and key contract addresses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[masoncags-tech](https://clawhub.ai/user/masoncags-tech) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to operate on Abstract mainnet and testnet, including wallet setup, balance checks, bridging, token transfers, token swaps, contract deployment, and contract calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent raw private-key authority to move real mainnet funds and call arbitrary contracts. <br>
Mitigation: Use a dedicated low-balance wallet, avoid long-lived raw private keys, and require manual review before any write operation. <br>
Risk: Bridge, swap, transfer, deployment, and arbitrary contract-call workflows can spend assets or interact with the wrong contract if chain, address, ABI, token, amount, approval, or router values are wrong. <br>
Mitigation: Prefer testnet first and manually verify every chain, address, router, ABI, token, amount, approval, and transaction before execution. <br>
Risk: Mainnet examples and defaults may create real financial exposure when copied into an agent workflow. <br>
Mitigation: Start with read-only balance and contract checks, then use small test amounts before allowing larger transactions. <br>


## Reference(s): <br>
- [Abstract Contract Addresses](references/addresses.md) <br>
- [Abstract Global Wallet Guide](references/agw.md) <br>
- [Hardhat Config for Abstract](references/hardhat.config.js) <br>
- [Abstract Troubleshooting Guide](references/troubleshooting.md) <br>
- [Abstract Docs](https://docs.abs.xyz) <br>
- [Abstract Global Wallet Docs](https://docs.abs.xyz/abstract-global-wallet/overview) <br>
- [Abstract Global Wallet SDK](https://github.com/Abstract-Foundation/agw-sdk) <br>
- [Relay Bridge for Abstract](https://relay.link/bridge/abstract) <br>
- [Abscan Explorer](https://abscan.org) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JavaScript scripts, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce transaction hashes, wallet addresses, balances, explorer links, and deployment addresses when scripts are executed.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
