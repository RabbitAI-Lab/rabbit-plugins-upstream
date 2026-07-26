## Description: <br>
Buy and sell NFTs on OpenSea's Seaport marketplace. Fulfill listings, accept offers, create new orders, cross-chain purchases, and sweep multiple listings. Requires wallet signing; for read-only queries use opensea-api instead. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[opensea](https://clawhub.ai/user/opensea) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare and execute OpenSea marketplace trade workflows, including NFT purchases, offer acceptance, order creation, cross-chain purchases, and listing sweeps. It is intended for workflows where an operator can supply OpenSea API access and review wallet-signing actions before submission. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide real wallet transactions and account mutations using OpenSea API access and wallet-signing authority. <br>
Mitigation: Use a dedicated low-balance wallet, managed signing provider policies and allowlists, and review every transaction before signing. <br>
Risk: API and wallet-auth credentials may be persisted locally for reuse. <br>
Mitigation: Avoid raw private keys, keep credentials in controlled environment variables or managed providers, and delete or rotate cached API/auth credentials when they are no longer needed. <br>
Risk: Marketplace fulfillment data and API responses can contain untrusted order, metadata, token, or transaction fields. <br>
Mitigation: Verify the transaction recipient, value, calldata, order hash, chain, and order expiry before signing, and do not follow instructions embedded in response content. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/opensea/skills/opensea-marketplace) <br>
- [OpenSea skill homepage](https://github.com/ProjectOpenSea/opensea-skill) <br>
- [OpenSea marketplace sub-skill](opensea-marketplace/SKILL.md) <br>
- [Marketplace API reference](opensea-marketplace/references/marketplace-api.md) <br>
- [Seaport reference](opensea-marketplace/references/seaport.md) <br>
- [Wallet setup sub-skill](opensea-wallet/SKILL.md) <br>
- [OpenSea CLI](https://github.com/ProjectOpenSea/opensea-cli) <br>
- [OpenSea developer documentation](https://docs.opensea.io/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, API call examples, and transaction-review instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce transaction calldata or ordered transaction steps that require human review and wallet signing before execution.] <br>

## Skill Version(s): <br>
2.19.0 (source: server release metadata, package.json, CHANGELOG) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
