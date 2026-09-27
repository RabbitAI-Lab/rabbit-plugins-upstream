## Description:

Guides agents through OpenSea NFT and token queries, marketplace trades, token swaps, wallet setup, and building onchain-gated AI tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[opensea](https://clawhub.ai/user/opensea)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other OpenSea users can guide an agent to query NFT and token data, prepare or execute NFT trades and token swaps, configure wallet signing, and build gated AI tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wallet-signed token swaps and NFT trades can spend funds; the swap helper has no built-in transaction confirmation step.

Mitigation: Before signing, independently verify the chain, asset identifiers, recipient, amount, fees, approvals, and calldata; use managed signing with transaction caps, allowlists, and limited wallet balances.

Risk: API credentials or broad wallet-signing authority can expose accounts and enable account-changing actions.

Mitigation: Use narrowly scoped, non-admin credentials and managed wallet providers instead of raw private keys; review drop publishes and account relationship changes before execution.

## Reference(s):

- [OpenSea skill on ClawHub](https://clawhub.ai/opensea/skills/opensea-marketplace)
- [OpenSea skill homepage](https://github.com/ProjectOpenSea/opensea-skill)
- [OpenSea developer documentation](https://docs.opensea.io/)
- [Marketplace API reference](opensea-marketplace/references/marketplace-api.md)
- [Token swaps reference](opensea-swaps/references/token-swaps.md)
- [Wallet policies reference](opensea-wallet/references/wallet-policies.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with commands and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide API queries, wallet-signed transactions, and tool registration.]

## Skill Version(s):

2.24.0 (source: ClawHub release and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
