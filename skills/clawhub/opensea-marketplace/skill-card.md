## Description:

Query NFT and token data, trade NFTs on Seaport, swap ERC20 tokens via a DEX aggregator, configure wallet signing providers, and build or gate AI agent tools on Base through the OpenSea CLI, MCP server, shell scripts, and SDK.

This skill is ready for commercial/non-commercial use.

## Publisher:

[opensea](https://clawhub.ai/user/opensea)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to route OpenSea tasks to the right sub-skill for read-only marketplace data, NFT trades, ERC20 swaps, wallet signing setup, and AI tool registration or gating.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wallet-linked actions can sign live transactions, fulfill orders, execute swaps, move assets, or mutate account state.

Mitigation: Use managed wallet providers with strict spending caps and allowlists, and require human review of every transaction, order, and swap before signing.

Risk: Credentials such as API keys, JWTs, PATs, and wallet-provider secrets may persist in local files or environment variables.

Mitigation: Keep credentials out of logs and backups, store them with least privilege, and revoke or rotate them after task-specific use.

Risk: Raw private keys expose funds if used in shared, hosted, or logged agent environments.

Mitigation: Avoid raw private keys except for local testing; prefer Privy, Turnkey, Fireblocks, Bankr, or another managed signing provider.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/opensea/skills/opensea-marketplace)
- [OpenSea skill homepage](https://github.com/ProjectOpenSea/opensea-skill)
- [OpenSea developer docs](https://docs.opensea.io/)
- [OpenSea CLI](https://github.com/ProjectOpenSea/opensea-cli)
- [Marketplace API reference](opensea-marketplace/references/marketplace-api.md)
- [Seaport reference](opensea-marketplace/references/seaport.md)
- [Wallet setup reference](opensea-wallet/references/wallet-setup.md)
- [Wallet policies reference](opensea-wallet/references/wallet-policies.md)
- [Token swaps reference](opensea-swaps/references/token-swaps.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, API examples, and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce transaction, order, swap, wallet, and credential-handling guidance that should be reviewed before execution.]

## Skill Version(s):

2.19.2 (source: release evidence and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
