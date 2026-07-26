## Description: <br>
Build with ERC-8004 Trustless Agents - on-chain agent identity, reputation, validation, and discovery on EVM chains. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tenequm](https://clawhub.ai/user/tenequm) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and engineers use this skill to register AI agents on-chain, work with ERC-8004 identity and reputation registries, search or discover agents, and integrate the Agent0 TypeScript SDK. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: On-chain registration and feedback examples can submit real transactions with the configured signer. <br>
Mitigation: Use throwaway or testnet keys for development and confirm the chain, signer, balance, and transaction details before sending. <br>
Risk: Wallet private keys and Pinata JWTs are sensitive credentials. <br>
Mitigation: Keep PRIVATE_KEY and PINATA_JWT out of source control, avoid hardcoding them, and use scoped or disposable credentials where possible. <br>
Risk: On-chain and IPFS registration or feedback data can become public and persistent. <br>
Mitigation: Avoid placing secrets, private user data, or sensitive business information in registration files, feedback files, or transaction metadata. <br>
Risk: Semantic search sends keyword queries to an external service. <br>
Mitigation: Avoid sensitive search terms when using semantic discovery. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/erc-8004-development) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/tenequm) <br>
- [Skill Homepage](https://github.com/tenequm/skills/tree/main/skills/erc-8004) <br>
- [ERC-8004 Specification](references/spec.md) <br>
- [ERC-8004 Smart Contracts](references/contracts.md) <br>
- [Agent0 TypeScript SDK](references/sdk-typescript.md) <br>
- [Agent Registration Best Practices](references/registration.md) <br>
- [ERC-8004 Reputation and Feedback System](references/reputation.md) <br>
- [Agent Search and Discovery](references/search-discovery.md) <br>
- [OASF Taxonomy v0.8.0](references/oasf-taxonomy.md) <br>
- [EIP Discussion](https://ethereum-magicians.org/t/erc-8004-trustless-agents/25098) <br>
- [ERC-8004 Contracts](https://github.com/erc-8004/erc-8004-contracts) <br>
- [ERC-8004 Best Practices](https://github.com/erc-8004/best-practices) <br>
- [Agent0 SDK Docs](https://sdk.ag0.xyz) <br>
- [OASF](https://github.com/agntcy/oasf) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with TypeScript, JSON, Solidity, and bash examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference RPC_URL, PRIVATE_KEY, and PINATA_JWT environment variables for ERC-8004 development workflows.] <br>

## Skill Version(s): <br>
0.2.2 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
