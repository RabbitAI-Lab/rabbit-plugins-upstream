## Description:

Query OpenSea NFT and token data, trade NFTs, swap ERC20 tokens, configure wallet signing, and build or gate AI agent tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[opensea](https://clawhub.ai/user/opensea)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use the skill to query OpenSea marketplace data, manage NFT trades and token swaps, configure signing wallets, and build onchain-gated tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks the release suspicious for transaction approval and swap workflow risks; its inspection was partial.

Mitigation: Review the transaction, swap, and quote-approval details before signing, and treat the scan as incomplete.

Risk: Unpinned package commands may run in an environment containing wallet credentials.

Mitigation: Avoid running unpinned package commands where wallet credentials are available.

Risk: Marketplace trades and swaps can sign approvals or other onchain transactions.

Mitigation: Preview the plan or quote and verify assets, amounts, fees, recipients, chain, and approvals before authorizing a transaction.

## Reference(s):

- [OpenSea developer documentation](https://docs.opensea.io/)
- [OpenSea Skill homepage](https://github.com/ProjectOpenSea/opensea-skill)
- [Marketplace API guide](artifact/opensea-marketplace/references/marketplace-api.md)
- [Wallet policies](artifact/opensea-wallet/references/wallet-policies.md)
- [Wallet setup and hardening](artifact/opensea-wallet/references/wallet-setup.md)
- [Tool access gating](artifact/opensea-tool-sdk/references/predicate-gating.md)
- [x402 payments](artifact/opensea-tool-sdk/references/x402.md)

## Skill Output:

**Output Type(s):** [API data, Markdown guidance, Shell commands, Code, JSON transaction steps, Configuration instructions]

**Output Format:** [JSON and text responses, Markdown guidance, shell commands, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only results or proposed transaction steps; onchain writes require wallet signing.]

## Skill Version(s):

2.33.0 (source: release metadata, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
