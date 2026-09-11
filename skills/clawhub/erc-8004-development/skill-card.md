## Description:

Build ERC-8004 Trustless Agents with guidance for on-chain agent identity, reputation, validation, discovery, Agent0 SDK usage, and EVM smart contract integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to register and discover ERC-8004 agents, wire Agent0 SDK flows, reason about on-chain identity and reputation, and prepare registration or feedback files for EVM deployments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Examples may sign state-changing EVM transactions with PRIVATE_KEY.

Mitigation: Use testnet or throwaway keys first, confirm chain ID, signer, transaction details, and balance before signing, and use scoped or hardware-backed signers for mainnet.

Risk: Registration files, feedback files, IPFS content, blockchain events, subgraph queries, and semantic search requests may be observable by third parties.

Mitigation: Avoid secrets and personal data in public metadata, registration files, and feedback files; review content before publishing or pinning.

Risk: SDK, RPC, IPFS, subgraph, and contract integrations depend on external services and package versions.

Mitigation: Pin and review SDK versions for serious use, verify endpoint configuration, and inspect contract addresses before relying on examples.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/erc-8004-development)
- [Skill Homepage](https://github.com/tenequm/skills/tree/main/skills/erc-8004)
- [ERC-8004 Specification](references/spec.md)
- [ERC-8004 Smart Contracts](references/contracts.md)
- [Agent Registration Best Practices](references/registration.md)
- [ERC-8004 Reputation and Feedback System](references/reputation.md)
- [Agent0 TypeScript SDK](references/sdk-typescript.md)
- [Agent Search and Discovery](references/search-discovery.md)
- [OASF Taxonomy v0.8.0](references/oasf-taxonomy.md)
- [EIP Discussion](https://ethereum-magicians.org/t/erc-8004-trustless-agents/25098)
- [ERC-8004 Contracts Repository](https://github.com/erc-8004/erc-8004-contracts)
- [ERC-8004 Best Practices](https://github.com/erc-8004/best-practices)
- [Agent0 SDK Docs](https://sdk.ag0.xyz)
- [Agent0 TypeScript SDK Repository](https://github.com/agent0lab/agent0-ts)
- [Agent0 Python SDK Repository](https://github.com/agent0lab/agent0-py)
- [Agent0 Subgraph Repository](https://github.com/agent0lab/subgraph)
- [Open Agentic Schema Framework](https://github.com/agntcy/oasf)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with TypeScript, JSON, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference RPC_URL, PRIVATE_KEY, and PINATA_JWT for EVM, signing, and IPFS examples.]

## Skill Version(s):

0.2.4 (source: evidence release.version and SKILL.md metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
