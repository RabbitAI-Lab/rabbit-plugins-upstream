## Description: <br>
Build, test, deploy, and audit Solana programs with Anchor or native Rust, and build with ZK Compression (Light Protocol). Use when developing Solana smart contracts, implementing token operations, optimizing compute, deploying to networks, auditing programs for vulnerabilities, or creating compressed tokens/PDAs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tenequm](https://clawhub.ai/user/tenequm) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and engineers use this skill to build Solana programs, clients, tests, deployment flows, security reviews, and ZK Compression workflows. It is intended for agents that need practical guidance, code examples, shell commands, and review checklists for Solana development. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Example code or commands may be copied into production Solana programs without sufficient review. <br>
Mitigation: Require human review of generated snippets and validate account ownership, signer checks, arithmetic, PDA seeds, CPI targets, and token handling before use. <br>
Risk: Deployment, upgrade authority, close, buffer write, or mainnet-fund commands can affect real on-chain assets or program control. <br>
Mitigation: Require explicit confirmation before executing real-chain actions and prefer localnet, devnet, or forked-mainnet testing before any mainnet operation. <br>
Risk: ZK Compression and Photon examples depend on external infrastructure and may have compute, proof, indexing, and state-update trade-offs. <br>
Mitigation: Confirm provider configuration, proof generation, compute budget, and indexing behavior in a test environment before production use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tenequm/skills/solana-development) <br>
- [Clawdis homepage](https://github.com/tenequm/skills/tree/main/skills/solana-development) <br>
- [Anchor Framework Reference](references/anchor.md) <br>
- [Native Rust Solana Programs Reference](references/native-rust.md) <br>
- [Solana Program Security and Validation](references/security-fundamentals.md) <br>
- [Security Checklists](references/security-checklists.md) <br>
- [Common Vulnerability Patterns](references/vulnerability-patterns.md) <br>
- [Solana Program Deployment Reference](references/deployment.md) <br>
- [Production Deployment Guide for Solana Programs](references/production-deployment.md) <br>
- [Compute Unit Optimization Guide](references/compute-optimization.md) <br>
- [Compressed Account Model](references/compressed-accounts.md) <br>
- [Compressed PDAs](references/compressed-pdas.md) <br>
- [Compressed Tokens](references/compressed-tokens.md) <br>
- [Client Integration](references/client-integration.md) <br>
- [ZK Compression Docs](https://www.zkcompression.com/) <br>
- [Light Protocol](https://github.com/Lightprotocol/light-protocol) <br>
- [Helius SDK](https://github.com/helius-labs/helius-sdk) <br>
- [Photon Indexer](https://github.com/helius-labs/photon) <br>
- [Program Examples](https://github.com/Lightprotocol/program-examples) <br>
- [Anchor documentation](https://www.anchor-lang.com/docs) <br>
- [Resources](references/resources.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline code blocks and command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Solana, Anchor, Rust, TypeScript, CLI, deployment, testing, audit, and ZK Compression guidance.] <br>

## Skill Version(s): <br>
0.7.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
