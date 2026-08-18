## Description:

Deterministic rug-pull and honeypot verdicts (CLEAR/CAUTION/AVOID) for tokens on 10 chains. Pay per scan via x402, about $0.015. No API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pulsenetwork](https://clawhub.ai/user/pulsenetwork)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to request deterministic token-safety scans before buying, trading, recommending, or otherwise evaluating crypto tokens. It returns token verdicts and flags for Solana, EVM chains, Robinhood Chain, and Algorand through paid x402 endpoints with explicit user consent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initiate paid token-safety scans through x402 or a local wallet setup.

Mitigation: Quote the scan price and obtain explicit user approval or a batch budget before any paid call.

Risk: Token identifiers are sent to the third-party provider for scanning.

Mitigation: Use the skill only when the user is comfortable sending token identifiers to PulseNetwork.

Risk: Payment keys or wallet secrets could be mishandled if discussed in chat.

Mitigation: Keep payment keys in the payment tool or environment secret and never request or accept private keys in chat.

Risk: A token-safety verdict could be mistaken for investment advice.

Mitigation: Present CLEAR as on-chain facts only, show CAUTION and AVOID flags clearly, and do not treat any verdict as a buy recommendation or price prediction.

## Reference(s):

- [PulseNetwork Token Safety on ClawHub](https://clawhub.ai/pulsenetwork/skills/pulsenetwork-token-safety)
- [PulseNetwork Service Homepage](https://onchainpulse.theaslangroupllc.com)
- [x402 Machine Catalog](https://onchainpulse.theaslangroupllc.com/.well-known/x402)

## Skill Output:

**Output Type(s):** [API Calls, Analysis, Guidance]

**Output Format:** [Text and Markdown summaries with quoted verdict fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Verdicts use CLEAR, CAUTION, or AVOID labels with red_flags and green_flags when returned by the service.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
