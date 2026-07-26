## Description: <br>
Allows an agent to transfer USD1, described as USDC on Wormhole, between wallets through Wormhole Liquidity Facility on testnet and return transaction status details. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[asgherali](https://clawhub.ai/user/asgherali) <br>

### License/Terms of Use: <br>
ISC <br>


## Use Case: <br>
Developers and external users can use this skill to let an agent initiate a USD1 testnet transfer between wallets and report the transaction hash, status, and message. It is best suited for disposable testnet wallet workflows because it requires a sender private key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill accepts a wallet private key that can authorize transfers. <br>
Mitigation: Use only disposable testnet wallets and do not provide reused or mainnet private keys. <br>
Risk: The skill can send tokens immediately without a built-in confirmation step. <br>
Mitigation: Verify the token, amount, chain, and recipient outside the skill before invocation; prefer a signer flow with explicit user approval for production use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/asgherali/skills/usd1) <br>


## Skill Output: <br>
**Output Type(s):** [Text, API Calls] <br>
**Output Format:** [JSON object with transactionHash, status, and message fields] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs a Wormhole testnet transfer flow from amount, recipient address, optional chain, and private key inputs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
