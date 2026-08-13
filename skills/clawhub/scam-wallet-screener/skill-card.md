## Description:

Screens Ethereum and other EVM wallet addresses against the ScamSniffer community blocklist of known phishing, wallet drainer, and scam addresses, with no API key required.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ssidharhubble](https://clawhub.ai/user/ssidharhubble)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security analysts, and crypto users use this skill to do a quick pre-check of EVM addresses before sending funds, approving transactions, claiming airdrops, minting NFTs, or reviewing batches of counterparties. It is a fast blocklist screen and should be combined with contract review, transaction simulation, and other due diligence before real-money actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A clean result can be mistaken for proof that an address or contract is safe.

Mitigation: State that absence from the ScamSniffer list is only one signal, then recommend contract verification, transaction simulation, and independent review before signing or transferring value.

Risk: The skill contacts GitHub to download a public blocklist and caches the data locally.

Mitigation: Disclose the network fetch and local cache behavior before use; use the refresh option when the latest available feed is needed.

Risk: The data source covers Ethereum-style EVM addresses and does not cover non-EVM chains.

Mitigation: Apply the result only to EVM-style addresses and use chain-appropriate tooling for Solana, Bitcoin, and other non-EVM ecosystems.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ssidharhubble/skills/scam-wallet-screener)
- [ScamSniffer scam database](https://github.com/scamsniffer/scam-database)
- [Artifact README](artifact/README.md)
- [Artifact SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text report or JSON object, usually accompanied by concise command-line usage guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each address is reported as FLAGGED or not found in blocklist; the local blocklist cache is refreshed every 6 hours unless bypassed.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
