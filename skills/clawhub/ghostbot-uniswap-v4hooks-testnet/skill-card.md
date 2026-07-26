## Description: <br>
GhostBot ACLM helps agents manage Sepolia Uniswap v4 concentrated liquidity by checking pool and oracle status, adding testnet liquidity, viewing positions, and preparing oracle signal actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aqiljaafree](https://clawhub.ai/user/aqiljaafree) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External DeFi users and developers use this skill to inspect and manage Sepolia Uniswap v4 liquidity positions, review dynamic-fee and rebalance signals, and run guided testnet pool-management actions from chat. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can sign Sepolia blockchain transactions for actions such as token minting, approvals, adding liquidity, and oracle signal posting. <br>
Mitigation: Confirm every on-chain action before running scripts and use only an isolated Sepolia setup. <br>
Risk: The package includes a public fallback private key that could be used without the user's knowledge. <br>
Mitigation: Remove the fallback private key, require DEPLOYER_PRIVATE_KEY from a secure environment, and avoid funding or trusting the packaged deployer account. <br>
Risk: Roles or assets tied to the exposed account may already be compromised. <br>
Mitigation: Rotate any roles or assets associated with the exposed account before relying on the deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aqiljaafree/skills/ghostbot-uniswap-v4hooks-testnet) <br>
- [Architecture reference](artifact/references/architecture.md) <br>
- [Deployed contracts reference](artifact/references/contracts.md) <br>
- [OpenClawACLMHook on Sepolia Etherscan](https://sepolia.etherscan.io/address/0xbD2802B7215530894d5696ab8450115f56b1fAC0) <br>
- [OpenClawOracle on Sepolia Etherscan](https://sepolia.etherscan.io/address/0x300Fa0Af86201A410bEBD511Ca7FB81548a0f027) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown text with inline shell commands, status summaries, and Sepolia transaction links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include proposed on-chain actions that should be reviewed before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
