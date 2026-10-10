## Description:

Guides agents in querying OpenSea NFT and token data, trading NFTs, swapping tokens, configuring wallet signing, and building gated agent tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[opensea](https://clawhub.ai/user/opensea)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to find OpenSea data, prepare or execute NFT trades and token swaps, configure wallet signing, and build or register agent tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wallet-signed trades and swaps can be irreversible, and the skill does not enforce a confirmation gate.

Mitigation: Review each trade, swap, deletion, revoke, or registration before execution; use a dedicated low-balance wallet with allowlists and per-transaction caps.

Risk: API keys and signing credentials grant access to OpenSea actions and wallet transactions.

Mitigation: Use managed wallet-provider policies and avoid exposing raw private keys to the agent.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/opensea/skills/opensea-marketplace)
- [Publisher-listed project homepage](https://github.com/ProjectOpenSea/opensea-skill)
- [OpenSea developer documentation](https://docs.opensea.io/)
- [Marketplace and Seaport reference](opensea-marketplace/references/seaport.md)
- [Token swaps reference](opensea-swaps/references/token-swaps.md)
- [Wallet policy guidance](opensea-wallet/references/wallet-policies.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with command, API, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some actions require API keys and wallet signing credentials.]

## Skill Version(s):

2.26.2 (source: ClawHub release, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
