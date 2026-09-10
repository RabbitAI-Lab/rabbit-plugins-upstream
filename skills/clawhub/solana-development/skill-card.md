## Description:

Build, test, deploy, and audit Solana programs with Anchor or native Rust, plus ZK Compression (Light Protocol). Use for Solana contracts, token operations, compute optimization, deployment, program audits, or compressed tokens and PDAs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to build, test, deploy, optimize, and audit Solana programs with Anchor or native Rust. It also supports token operations, client integration, and ZK Compression workflows using Light Protocol.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands may execute code without enough review.

Mitigation: Inspect installer scripts and prefer pinned, verified installation steps before running any curl-to-bash command.

Risk: Examples involving wallets, keypairs, transfers, burns, closes, and deployments can affect real assets or expose secrets.

Mitigation: Use devnet, local validators, disposable wallets, and non-production keypairs until commands have been reviewed and adapted for the target environment.

Risk: Deployment guidance can trigger irreversible or high-impact blockchain changes.

Mitigation: Require explicit human approval, verified builds, small-scope tests, and authority review before any mainnet deployment or upgrade.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/solana-development)
- [Publisher profile](https://clawhub.ai/user/tenequm)
- [Source homepage](https://github.com/tenequm/skills/tree/main/skills/solana-development)
- [Anchor Framework Reference](references/anchor.md)
- [Native Rust Reference](references/native-rust.md)
- [Security Checklists](references/security-checklists.md)
- [Vulnerability Patterns](references/vulnerability-patterns.md)
- [Production Deployment](references/production-deployment.md)
- [ZK Compression Docs](https://www.zkcompression.com/)
- [Light Protocol](https://github.com/Lightprotocol/light-protocol)
- [Helius SDK](https://github.com/helius-labs/helius-sdk)
- [Photon Indexer](https://github.com/helius-labs/photon)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline code blocks and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Solana CLI, Anchor, Rust, TypeScript, testing, deployment, and audit guidance.]

## Skill Version(s):

0.7.3 (source: SKILL.md metadata and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
