## Description:

Buy and sell NFTs through OpenSea on EVM chains and Solana. Fulfill listings, accept or create offers, cancel orders, make cross-chain purchases, and sweep listings. Requires wallet signing; for read-only queries use opensea-api instead.

This skill is ready for commercial/non-commercial use.

## Publisher:

[opensea](https://clawhub.ai/user/opensea)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to create, fulfill, cancel, and sweep OpenSea NFT listings and offers across supported EVM chains and Solana. It guides wallet signing and transaction review for marketplace actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wallet signing can authorize NFT trades and token or NFT approvals; the security evidence reports wallet and transaction safety concerns.

Mitigation: Use a restricted wallet, inspect the dry-run plan and costs (including price, fees, chain, recipients, approvals, and plan digest), and obtain explicit approval before signing.

Risk: The security evidence notes unpinned installation commands, and its scan was partial.

Mitigation: Review and pin the package and source versions before installation, and independently inspect each transaction before approving it.

## Reference(s):

- [Marketplace API reference](references/marketplace-api.md)
- [OpenSea API key documentation](https://docs.opensea.io/reference/api-keys#instant-api-key-for-agents)
- [Project homepage](https://github.com/ProjectOpenSea/opensea-skill)

## Skill Output:

**Output Type(s):** [API Calls, Transaction plans, Shell commands, Configuration instructions]

**Output Format:** [JSON transaction plans and responses, human-readable summaries, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Marketplace writes may require wallet signatures and explicit user approval.]

## Skill Version(s):

2.31.1 (source: package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
