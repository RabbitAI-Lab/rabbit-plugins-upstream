## Description:

Buy and sell NFTs through OpenSea on EVM chains and Solana. Fulfill listings, accept or create offers, cancel orders, make cross-chain purchases, and sweep listings. Requires wallet signing; for read-only queries use opensea-api instead.

This skill is ready for commercial/non-commercial use.

## Publisher:

[opensea](https://clawhub.ai/user/opensea)

### License/Terms of Use:

MIT

## Use Case:

External developers and engineers use this skill to prepare OpenSea marketplace actions for NFT buying, selling, offer creation, order cancellation, cross-chain fulfillment, and listing sweeps. It is intended for workflows where a human or managed wallet policy reviews and signs returned transaction data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initiate wallet-backed marketplace actions such as listings, offers, cancellations, fulfillment, and cross-chain purchases.

Mitigation: Require explicit user confirmation before any state-changing action and review the exact order, quote, transaction target, calldata, value, and chain before signing.

Risk: A compromised or overfunded agent wallet could expose funds during trades or approvals.

Mitigation: Use a managed wallet provider with spending caps and allowlists, keep only limited funds in the agent wallet, and avoid production raw private keys.

Risk: API keys, wallet credentials, cached auth data, JWTs, PATs, and provider secrets are sensitive.

Mitigation: Store credentials only through approved secret handling, avoid logging secrets, and rotate or revoke credentials when no longer needed.

## Reference(s):

- [Marketplace API Reference](opensea-marketplace/references/marketplace-api.md)
- [Seaport Reference](opensea-marketplace/references/seaport.md)
- [OpenSea Developer Docs](https://docs.opensea.io/)
- [OpenSea CLI](https://github.com/ProjectOpenSea/opensea-cli)
- [Skill Homepage](https://github.com/ProjectOpenSea/opensea-skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON/API payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include OpenSea API request guidance and transaction/action details that require separate wallet review, signing, and submission.]

## Skill Version(s):

2.21.1 (source: package.json and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
