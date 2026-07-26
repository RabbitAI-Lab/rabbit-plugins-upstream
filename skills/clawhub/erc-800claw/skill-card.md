## Description: <br>
The OpenClaw entry point for ERC-8004 agent identity and reputation. Register agents on-chain, query identities, give and receive feedback ratings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[primer-dev](https://clawhub.ai/user/primer-dev) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to register ERC-8004 agent identities, query on-chain identity and ownership data, and submit or review reputation feedback. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet-key-backed registration or feedback can create irreversible blockchain transactions, especially on mainnet. <br>
Mitigation: Prefer Sepolia or another testnet first, use a dedicated low-value wallet, and require explicit approval before any mainnet transaction. <br>
Risk: The skill requires PRIVATE_KEY-based actions for registration and feedback. <br>
Mitigation: Store keys only in environment variables, never expose them in logs or chat, and rotate any key that may have been disclosed. <br>
Risk: Package installation relies on external npm or PyPI packages. <br>
Mitigation: Verify the package source and version before installation or execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/primer-dev/skills/erc-800claw) <br>
- [ERC-8004 protocol](https://8004.org) <br>
- [EIP-8004](https://eips.ethereum.org/EIPS/eip-8004) <br>
- [erc-800claw npm package](https://npmjs.com/package/erc-800claw) <br>
- [erc-800claw PyPI package](https://pypi.org/project/erc-800claw) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown guidance with CLI commands, code snippets, and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May involve Ethereum network selection, RPC configuration, and PRIVATE_KEY-backed registration or feedback actions.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata; artifact/_meta.json lists 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
