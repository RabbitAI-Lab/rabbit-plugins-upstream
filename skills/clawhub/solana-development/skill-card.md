## Description:

Build, test, deploy, and audit Solana programs with Anchor or native Rust, and build with ZK Compression (Light Protocol). Use when developing Solana smart contracts, implementing token operations, optimizing compute, deploying to networks, auditing programs for vulnerabilities, or creating compressed tokens/PDAs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to build, test, deploy, optimize, and review Solana programs with Anchor or native Rust, including token operations and ZK Compression workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review rated the skill suspicious because some security and deployment guidance may be inconsistent or may under-warn about destructive Solana actions.

Mitigation: Treat the skill as a broad Solana development reference, and verify security-critical examples against current Anchor, Solana, and Light Protocol documentation before copying them.

Risk: Deploy, upgrade, close, mainnet RPC, or API-key-bearing commands can affect real Solana programs, accounts, or credentials.

Mitigation: Require explicit confirmation before running these commands, prefer devnet or local validation first, and avoid embedding API keys in shared command output.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/solana-development)
- [ClawHub Metadata Homepage](https://github.com/tenequm/skills/tree/main/skills/solana-development)
- [Anchor Framework Reference](references/anchor.md)
- [Native Rust Solana Programs Reference](references/native-rust.md)
- [Solana Program Deployment Reference](references/deployment.md)
- [Production Deployment Guide for Solana Programs](references/production-deployment.md)
- [Solana Program Security & Validation](references/security-fundamentals.md)
- [Security Checklists](references/security-checklists.md)
- [Common Vulnerability Patterns](references/vulnerability-patterns.md)
- [Compute Unit Optimization Guide](references/compute-optimization.md)
- [Compressed PDAs](references/compressed-pdas.md)
- [Compressed Tokens](references/compressed-tokens.md)
- [ZK Compression Docs](https://www.zkcompression.com/)
- [Light Protocol](https://github.com/Lightprotocol/light-protocol)
- [Helius SDK](https://github.com/helius-labs/helius-sdk)
- [Photon Indexer](https://github.com/helius-labs/photon)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Solana, Anchor, Rust, TypeScript, RPC, deployment, testing, and audit guidance.]

## Skill Version(s):

0.7.2 (source: server release and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
