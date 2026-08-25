## Description:

Buy and sell NFTs on OpenSea's Seaport marketplace. Fulfill listings, accept offers, create new orders, cross-chain purchases, and sweep multiple listings. Requires wallet signing; for read-only queries use opensea-api instead.

This skill is ready for commercial/non-commercial use.

## Publisher:

[opensea](https://clawhub.ai/user/opensea)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to prepare and execute OpenSea marketplace actions, including NFT purchases, offer acceptance, new Seaport orders, cross-chain purchases, and listing sweeps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can support real wallet and marketplace actions, including listings, offers, purchases, approvals, transfers, and cross-chain transactions.

Mitigation: Use a dedicated low-balance wallet, scoped managed wallet-provider policies, narrow API and wallet permissions, and human review before signing any transaction.

Risk: Sensitive wallet or API credentials could be exposed in a shared agent environment.

Mitigation: Store credentials only in environment variables, avoid raw private keys and broad admin credentials, and prefer managed wallet providers for shared or production use.

Risk: Marketplace fulfillment data can be stale, multi-step, or sourced from untrusted API response fields.

Mitigation: Verify the transaction recipient, value, calldata, order expiry, and any ERC20 approval before signing; re-query expired orders and execute cross-chain transaction steps in order.

## Reference(s):

- [Marketplace API Reference](artifact/opensea-marketplace/references/marketplace-api.md)
- [Seaport Reference](artifact/opensea-marketplace/references/seaport.md)
- [OpenSea Developer Docs](https://docs.opensea.io/)
- [OpenSea CLI](https://github.com/ProjectOpenSea/opensea-cli)
- [OpenSea Skill Homepage](https://github.com/ProjectOpenSea/opensea-skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, API paths, JSON snippets, and transaction guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce transaction data guidance for wallet signing workflows; users should review generated transaction details before signing.]

## Skill Version(s):

2.20.0 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
