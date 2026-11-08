## Description:

Query NFT and token data, trade NFTs on Seaport, swap ERC20 tokens via DEX aggregator, configure wallet signing providers, and build/register/gate AI agent tools on Base. Covers the full OpenSea developer surface across CLI, MCP server, shell scripts, and SDK.

This skill is ready for commercial/non-commercial use.

## Publisher:

[opensea](https://clawhub.ai/user/opensea)

### License/Terms of Use:

MIT

## Use Case:

Developers and AI agents use this integration to query OpenSea NFT and token data, execute marketplace trades and token swaps, configure wallet signing, and build or manage agent tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wallet setup includes a live trade.

Mitigation: Before connecting a funded wallet, replace setup trades with a wallet-information check and use a dedicated low-balance wallet.

Risk: The recommended spending-policy examples are unreliable.

Mitigation: Correct and test the policy templates, and keep administrative credentials off the agent host.

Risk: Signing an unexpected transaction can execute an unintended trade.

Mitigation: Authorize each intended trade's assets, chain, amount, and limits, and validate returned transactions before signing.

## Reference(s):

- [Project homepage](https://github.com/ProjectOpenSea/opensea-skill)
- [OpenSea developer documentation](https://docs.opensea.io/)
- [Marketplace API guide](opensea-marketplace/references/marketplace-api.md)
- [Seaport guide](opensea-marketplace/references/seaport.md)
- [Wallet setup guide](opensea-wallet/references/wallet-setup.md)
- [Wallet policy guide](opensea-wallet/references/wallet-policies.md)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Shell commands, Code, Configuration]

**Output Format:** [Markdown guidance, shell commands, code examples, configuration instructions, and JSON API or transaction data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returned fields depend on the selected API, CLI command, or wallet action.]

## Skill Version(s):

2.28.0 (source: package.json, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
