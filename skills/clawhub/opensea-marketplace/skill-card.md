## Description:

Routes agents to OpenSea workflows for NFT and token queries, NFT trading, token swaps, wallet signing, and building gated AI tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[opensea](https://clawhub.ai/user/opensea)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other OpenSea users can query NFT and token data, trade NFTs, execute token swaps, configure wallet signing, and build or register gated AI tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wallet signing and swap execution can proceed without an enforced transaction-specific confirmation boundary.

Mitigation: Require explicit user review of token addresses, amounts, recipients, fees, and transaction data before signing or executing trades and swaps.

Risk: Agent access to API keys or wallet credentials can expose accounts and funds.

Mitigation: Use managed wallet providers with spending caps and allowlists; avoid raw private keys outside local development and pin tool versions where possible.

## Reference(s):

- [OpenSea skill on ClawHub](https://clawhub.ai/opensea/skills/opensea-marketplace)
- [OpenSea skill project homepage](https://github.com/ProjectOpenSea/opensea-skill)
- [OpenSea developer documentation](https://docs.opensea.io/)
- [Marketplace API reference](opensea-marketplace/references/marketplace-api.md)
- [Wallet policy reference](opensea-wallet/references/wallet-policies.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API requests and transaction preparation steps.]

## Skill Version(s):

2.23.1 (source: ClawHub release and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
