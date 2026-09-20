## Description:

Buy and sell NFTs through OpenSea on EVM chains and Solana. Fulfill listings, accept or create offers, cancel orders, make cross-chain purchases, and sweep listings. Requires wallet signing; for read-only queries use opensea-api instead.

This skill is ready for commercial/non-commercial use.

## Publisher:

[opensea](https://clawhub.ai/user/opensea)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to prepare OpenSea marketplace actions for NFT buying, selling, offer management, order cancellation, cross-chain purchases, and listing sweeps. It is intended for wallet-backed marketplace workflows where users review and sign returned transaction data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can support wallet-backed marketplace actions, including trades and approvals.

Mitigation: Use managed wallet providers with spending caps, allowlists, and least-privilege scopes, and require human review before signing.

Risk: Returned transaction data, recipients, chain identifiers, assets, amounts, and approvals may not match user intent.

Mitigation: Review chain, asset, recipient, amount, approval target, and transaction data before signing or broadcasting any step.

Risk: Raw private keys increase exposure outside isolated local testing.

Mitigation: Avoid raw private keys except for local development and prefer managed providers such as Privy, Turnkey, Fireblocks, or Bankr.

Risk: Unpinned npm or npx installs may produce non-reproducible behavior.

Mitigation: Pin npm and npx versions when reproducible installs are required.

## Reference(s):

- [OpenSea Skill Homepage](https://github.com/ProjectOpenSea/opensea-skill)
- [OpenSea Marketplace API](artifact/opensea-marketplace/references/marketplace-api.md)
- [Seaport Protocol Reference](artifact/opensea-marketplace/references/seaport.md)
- [OpenSea Developer Docs](https://docs.opensea.io/)
- [OpenSea CLI](https://github.com/ProjectOpenSea/opensea-cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON/API response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe unsigned or signable transaction data, ordered action steps, API calls, wallet configuration requirements, and safety checks.]

## Skill Version(s):

2.22.0 (source: server release evidence and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
