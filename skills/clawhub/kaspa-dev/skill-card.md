## Description: <br>
Kaspa Dev helps developers build Kaspa transactions, wallet integrations, dApps, block explorers, node operations, KRC20 token workflows, and SDK integrations across Rust, Go, JavaScript/TypeScript, Python, WASM, and Motoko. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[codecustard](https://clawhub.ai/user/codecustard) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to create and review Kaspa blockchain code, transaction flows, wallet integrations, node setup steps, SDK usage patterns, and KRC20 token examples. It is suited for external and internal development workflows where blockchain sample code must be adapted and checked before use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Blockchain examples can affect real funds, private keys, or mnemonic phrases if copied directly into mainnet workflows. <br>
Mitigation: Use testnet or devnet first, never log or share real secrets, and manually verify any mainnet broadcast. <br>
Risk: Passing private keys as command-line arguments can expose secrets through shell history or process listings. <br>
Mitigation: Avoid command-line private key arguments and prefer reviewed secret-handling flows before signing transactions. <br>
Risk: Node and firewall commands can change a server's network exposure or operating state. <br>
Mitigation: Review node, Docker, and firewall commands before applying them to a server. <br>


## Reference(s): <br>
- [Kaspa Development Skill](artifact/SKILL.md) <br>
- [Kaspa Developer Platform API Reference](artifact/references/api-reference.md) <br>
- [Kaspa WASM SDK](artifact/references/kaspa-wasm-sdk.md) <br>
- [Kaspa Rust SDK](artifact/references/kaspa-rust-sdk.md) <br>
- [Kaspa Go SDK](artifact/references/kaspa-go-sdk.md) <br>
- [Kaspa Python SDK](artifact/references/kaspa-python-sdk.md) <br>
- [KRC20 Token Standard](artifact/references/krc20-tokens.md) <br>
- [Wallet Integration Guide](artifact/references/wallet-integration.md) <br>
- [Kaspa Node Operations](artifact/references/node-operations.md) <br>
- [Kaspa Documentation](https://docs.kas.fyi/) <br>
- [Kaspa Developer Platform](https://kas.fyi/) <br>
- [Kaspa API Endpoint](https://api.kaspa.org) <br>
- [Kaspa Motoko Package](https://mops.one/kaspa) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with code snippets, shell commands, JSON examples, and configuration steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include blockchain transaction examples and sample scripts; users should test on testnet or devnet before mainnet use.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
