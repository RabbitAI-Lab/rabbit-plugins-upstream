## Description: <br>
Park trading profits in a non-zero-sum yield vault on Base where USDC deposits receive LOVE shares, withdrawals return USDC, and every fund movement requires explicit operator approval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[batcatchina](https://clawhub.ai/user/batcatchina) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agents and developers use this skill to check Zhenghe Vault balances, review NAV, and prepare deposit or withdrawal calldata for operator-approved Base mainnet transactions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Deposits and withdrawals are real Base mainnet transactions involving USDC. <br>
Mitigation: Require explicit operator approval for every fund movement and show the amount, destination contract, calldata, value, and chainId before signing. <br>
Risk: Incorrect contract addresses, approvals, calldata, or chainId can cause irreversible loss. <br>
Mitigation: Verify contract addresses, chainId 8453, approval amounts, and decoded calldata in the wallet or a block explorer before broadcasting. <br>
Risk: Vault yield and NAV claims are not guaranteed and depend on external on-chain activity. <br>
Mitigation: Independently review current vault state and avoid relying on historical NAV growth as a guarantee of future returns. <br>
Risk: Large withdrawals may be limited by available vault liquidity. <br>
Mitigation: Check maxRedeem and current vault balances before attempting a withdrawal. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/batcatchina/skills/zhenghe-vault) <br>
- [Zhenghe system homepage](https://zhenghe-system.vercel.app) <br>
- [Zhenghe A2A endpoint](https://zhenghe-system.vercel.app/api/a2a) <br>
- [Zhenghe agent card](https://zhenghe-system.vercel.app/.well-known/agent.json) <br>
- [LoveVault contract on Basescan](https://basescan.org/address/0x16A7F8CfAD687A87183fCbd1dF7aF09dce05D357) <br>
- [ZhengHeRouter contract on Basescan](https://basescan.org/address/0x2348ec656e395edAbcE2e198DC44647456d81867) <br>
- [Base USDC contract on Basescan](https://basescan.org/address/0x833589fcd6edb6e08f4c7c32d4f71b54bda02913) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown guidance with curl commands and JSON-RPC request and response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl; optional ZHENGHE_WALLET_ADDRESS environment variable can supply the Base wallet address.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
