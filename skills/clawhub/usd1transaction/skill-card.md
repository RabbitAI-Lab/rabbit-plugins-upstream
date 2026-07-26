## Description: <br>
Allows an agent to transfer USD1, described as USDC on Wormhole, between wallets using Wormhole Liquidity Facility on testnet by default. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[asgherali](https://clawhub.ai/user/asgherali) <br>

### License/Terms of Use: <br>
ISC <br>


## Use Case: <br>
Developers and agents use this skill to check wallet inputs and submit a USD1 transfer request through Wormhole testnet, receiving transaction status and a transaction hash when successful. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill accepts a raw wallet private key and can broadcast a transfer without a separate confirmation step. <br>
Mitigation: Use only throwaway testnet wallets, manually verify recipient, amount, chain, and token before execution, and prefer delegated wallet signing for production use. <br>
Risk: A mistaken or malicious recipient address, amount, chain, or token selection can cause an unintended blockchain transfer. <br>
Mitigation: Require explicit human review of transfer details before providing credentials or allowing the agent to submit the transfer. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/asgherali/skills/usd1transaction) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Text, Configuration] <br>
**Output Format:** [JSON-like status object with transaction hash, status, and message fields] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires amount, recipient address, and sender private key inputs; chain defaults to Solana.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
