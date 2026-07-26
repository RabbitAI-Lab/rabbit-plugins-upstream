## Description: <br>
Store, verify, and manage AI data on the Ethereum blockchain (Base network) using the ERCData standard. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0xreisearch](https://clawhub.ai/user/0xreisearch) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent builders use ERCData to store data fingerprints, verify integrity, create audit trails, manage access for private entries, and interact with the ERCData contract on Base mainnet. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Commands can prepare or send real Base mainnet transactions that may spend gas or alter on-chain ERCData state. <br>
Mitigation: Use a dedicated low-balance wallet, verify the intended action before execution, and manually review write, access-control, and snapshot commands. <br>
Risk: Wallet private keys may be exposed if passed directly on the command line or handled as ordinary text. <br>
Mitigation: Use protected environment or secret handling for ERCDATA_KEY and avoid passing --key in command history. <br>
Risk: Raw transaction calldata remains visible on-chain even for private entries. <br>
Mitigation: Store hashes or client-side encrypted payloads instead of raw sensitive data. <br>
Risk: Incorrect contract or RPC configuration can direct actions to an unintended endpoint. <br>
Mitigation: Verify the contract address and Base mainnet RPC endpoint before reads, writes, verification, or access changes. <br>


## Reference(s): <br>
- [ERCData API Reference](references/api.md) <br>
- [ERCData ClawHub Release](https://clawhub.ai/0xreisearch/skills/ercdata) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, JSON] <br>
**Output Format:** [Markdown with inline bash commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May prepare or submit Base mainnet transactions when wallet credentials, contract address, and RPC endpoint are configured.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
