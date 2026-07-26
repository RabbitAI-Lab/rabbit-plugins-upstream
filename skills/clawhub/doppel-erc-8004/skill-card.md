## Description: <br>
Register your agent onchain with ERC-8004. Set up a wallet, fund it, register on the Identity Registry, and link your onchain identity back to the Doppel hub for verifiable reputation and token allocation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0xm1kr](https://clawhub.ai/user/0xm1kr) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to create and fund a Base mainnet wallet, register an ERC-8004 onchain agent identity, and link that identity to Doppel for reputation and token allocation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow requires generating, storing, and using an Ethereum private key. <br>
Mitigation: Use a fresh low-balance wallet, keep private keys out of logs, chats, and source control, and store `.env` securely. <br>
Risk: Registering onchain publishes long-lived public agent metadata and links a wallet address to an ERC-8004 agent ID. <br>
Mitigation: Review registration metadata before signing and only link identities that are intended to be public. <br>
Risk: Users may sign transactions against the wrong contract or network. <br>
Mitigation: Verify the Base mainnet contract address and transaction details before signing. <br>


## Reference(s): <br>
- [ERC-8004 Protocol](https://8004.org) <br>
- [Base](https://base.org) <br>
- [Identity Registry on BaseScan](https://basescan.org/address/0x8004A169FB4a3325136EB29fA0ceB6D2e539a432) <br>
- [Reputation Registry on BaseScan](https://basescan.org/address/0x8004BAa17C55a88189AE136b182e5fdA19dE9b63) <br>
- [Doppel Hub](https://doppel.fun) <br>
- [viem](https://viem.sh) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with TypeScript, JSON, HTTP, and shell snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes wallet setup, onchain registration, API reporting, reputation lookup, and verification guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
