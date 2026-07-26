## Description: <br>
Performs ERC-721 NFT operations on BNB Chain, including metadata lookup, ownership checks, wallet balances, collection information, transfers, and approvals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clawzai](https://clawhub.ai/user/clawzai) <br>

### License/Terms of Use: <br>
ISC <br>


## Use Case: <br>
Developers and NFT operators use this skill to inspect ERC-721 collections and tokens on BNB Chain and prepare or execute transfer and approval transactions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can sign real NFT transfers and approvals with a raw private key. <br>
Mitigation: Use a dedicated low-value wallet, prefer environment-based secrets over command-line keys, and confirm each transaction before use. <br>
Risk: Collection-wide approve-all can grant broad operator control until it is revoked. <br>
Mitigation: Verify the operator address, use approve-all only when necessary, and revoke approval after the intended transaction flow is complete. <br>
Risk: Incorrect contract, recipient, spender, or operator addresses can affect real assets. <br>
Mitigation: Independently verify all addresses and test transfer or approval flows on testnet before using a valuable wallet. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/clawzai/skills/bnb-nft) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Write operations require a private key and may submit real BNB Chain NFT transactions.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
