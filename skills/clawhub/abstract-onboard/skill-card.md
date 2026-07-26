## Description: <br>
Deploy smart contracts and bridge assets to Abstract (ZK Stack L2). Use when an agent needs to deploy contracts on Abstract, bridge ETH/tokens to Abstract, trade/swap tokens, place predictions on Myriad Markets, check balances, transfer assets, or interact with Abstract mainnet. Covers zksolc compilation, Hardhat deployment, Relay bridging, DEX trading (Kona, Aborean), Myriad prediction markets, and key contract addresses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[masoncags-tech](https://clawhub.ai/user/masoncags-tech) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to operate on Abstract by creating Abstract Global Wallets, deploying zkSync-compatible contracts, bridging assets, swapping tokens, placing Myriad prediction-market trades, checking balances, transferring assets, and monitoring chain activity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a private key to sign live mainnet transactions and move real funds. <br>
Mitigation: Use a dedicated low-balance wallet and review every transaction target, amount, spender, allowance, and quote before running scripts. <br>
Risk: Some swaps, bridges, approvals, and prediction-market trades may execute with weak safety gates. <br>
Mitigation: Confirm slippage limits, deadlines, allowances, bridge routes, and destination addresses before submitting transactions. <br>
Risk: Abstract Global Wallet address derivation can change when dependency versions change. <br>
Mitigation: Pin wallet-related dependencies and verify the computed AGW address before sending funds. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/masoncags-tech/skills/abstract-onboard) <br>
- [Abstract contract addresses](references/addresses.md) <br>
- [Abstract Global Wallet guide](references/agw.md) <br>
- [Abstract DEX reference](references/dex.md) <br>
- [Hardhat config for Abstract](references/hardhat.config.js) <br>
- [Myriad prediction markets on Abstract](references/myriad.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>
- [Abstract docs](https://docs.abs.xyz) <br>
- [Abstract Global Wallet docs](https://docs.abs.xyz/abstract-global-wallet/overview) <br>
- [Abstract AGW SDK](https://github.com/Abstract-Foundation/agw-sdk) <br>
- [Abstract explorer](https://abscan.org) <br>
- [Relay bridge for Abstract](https://relay.link/bridge/abstract) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JavaScript code examples, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or run scripts that use wallet private keys and submit transactions on Abstract mainnet.] <br>

## Skill Version(s): <br>
1.6.0 (source: server release and SKILL.md frontmatter; artifact/package.json lists 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
