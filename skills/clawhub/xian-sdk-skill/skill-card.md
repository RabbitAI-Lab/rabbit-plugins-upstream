## Description: <br>
Build applications on the Xian blockchain using the xian-py Python SDK, including wallets, transactions, smart contracts, state queries, token transfers, and sync or async patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[endogen](https://clawhub.ai/user/endogen) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to build Xian blockchain applications with the xian-py Python SDK. It provides examples and guidance for wallet management, transaction submission, smart contract deployment and validation, blockchain queries, encryption, error handling, and sync or async integration patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Transaction, approval, swap, send_tx, and submit_contract examples can become real on-chain actions when connected to a live wallet or production node. <br>
Mitigation: Use test wallets and testnets first, verify addresses and amounts, and require explicit confirmation before broadcasting transactions. <br>
Risk: Wallet private keys and mnemonic phrases appear in the workflow domain and must be treated as highly sensitive secrets. <br>
Mitigation: Never paste production private keys or mnemonics into prompts, logs, or generated files; use secret storage and redaction for live credentials. <br>
Risk: Smart contract examples may deploy or upgrade code with persistent blockchain effects. <br>
Mitigation: Review and validate contracts against the intended Xian standard, simulate where possible, and deploy first to a non-production environment. <br>


## Reference(s): <br>
- [Contract Patterns](references/contract-patterns.md) <br>
- [xian-py GitHub](https://github.com/xian-network/xian-py) <br>
- [Xian Standard Contracts](https://github.com/xian-network/xian-standard-contracts) <br>
- [Xian Project Site](https://xian.org) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with Python and bash code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces developer guidance and example commands; it does not execute blockchain transactions by itself.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
