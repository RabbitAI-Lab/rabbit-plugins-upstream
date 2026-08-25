## Description:

Build with ERC-8004 Trustless Agents for on-chain agent identity, reputation, validation, and discovery on EVM chains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to implement ERC-8004 and Agent0 workflows, including agent registration, wallet-aware identity, reputation feedback, validation, and discovery across EVM chains.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Signing ERC-8004 transactions with valuable or incorrectly configured wallet keys can expose funds or register data on the wrong chain.

Mitigation: Use testnet or throwaway keys for development, verify chain IDs before signing, and avoid storing valuable wallet keys in environment variables.

Risk: Registration metadata, feedback records, IPFS or on-chain data, and semantic search keywords may become public or be processed by external services.

Mitigation: Treat those inputs as public, minimize sensitive data, and review metadata before publishing or searching.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/erc-8004-development)
- [Skill homepage](https://github.com/tenequm/skills/tree/main/skills/erc-8004)
- [ERC-8004 specification](artifact/references/spec.md)
- [ERC-8004 smart contracts](artifact/references/contracts.md)
- [Agent0 TypeScript SDK](artifact/references/sdk-typescript.md)
- [Agent registration best practices](artifact/references/registration.md)
- [Reputation and feedback system](artifact/references/reputation.md)
- [Agent search and discovery](artifact/references/search-discovery.md)
- [OASF taxonomy](artifact/references/oasf-taxonomy.md)
- [EIP discussion](https://ethereum-magicians.org/t/erc-8004-trustless-agents/25098)
- [Agent0 SDK docs](https://sdk.ag0.xyz)
- [ERC-8004 contracts repository](https://github.com/erc-8004/erc-8004-contracts)
- [ERC-8004 best practices](https://github.com/erc-8004/best-practices)
- [Agent0 TypeScript SDK repository](https://github.com/agent0lab/agent0-ts)
- [OASF repository](https://github.com/agntcy/oasf)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with TypeScript, JSON, GraphQL, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference optional environment variables RPC_URL, PRIVATE_KEY, and PINATA_JWT for blockchain and IPFS workflows.]

## Skill Version(s):

0.2.3 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
