## Description:

Neon Nodes is an Agentic Proof of Work NFT skill on Robinhood Chain that solves a single-tier arithmetic puzzle and guides an agent through minting Neon Nodes NFTs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[neonnodesrh](https://clawhub.ai/user/neonnodesrh)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to solve an arithmetic puzzle, request an unsigned NFT mint transaction, sign it locally, and submit the signed transaction to mint Neon Nodes NFTs on Robinhood Chain.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks an agent to handle a raw EVM private key, which can expose wallet funds if the key is logged, echoed, stored, or sent to an unintended destination.

Mitigation: Do not provide raw private keys to the skill; prefer hardware wallets, browser wallets, local signers, or user-reviewed transaction signing flows.

Risk: The skill submits paid blockchain transactions, so mistakes in quantity, destination, fee settings, or transaction data can cause irreversible costs.

Mitigation: Require explicit user review of transaction target, value, chain ID, gas settings, and mint quantity before signing or broadcasting.

Risk: The artifact includes package installation and local script execution behavior for ethers fallback.

Mitigation: Review dependency installation and script contents before execution, use temporary isolated directories, and avoid printing secrets in terminal output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/neonnodesrh/skills/neonnodesskill)
- [Publisher profile](https://clawhub.ai/user/neonnodesrh)
- [Neon Nodes homepage](https://neonnodes.xyz)
- [Neon Nodes skill file](https://neonnodes.xyz/skill.md)
- [Neon Nodes API base](https://neonnodes.xyz/api)
- [Robinhood Chain RPC](https://rpc.mainnet.chain.robinhood.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown guidance with JSON examples, curl commands, and JavaScript signing code.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces puzzle answers, unsigned transaction handling guidance, local signing code, signed transaction submission steps, transaction status, and NFT token IDs.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
