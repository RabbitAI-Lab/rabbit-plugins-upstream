## Description:

MENTAT helps agents quote token swaps, inspect the open order book, verify tokens, and prepare OTC escrow deals, with human approval required before signing or sending any step.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agora0x](https://clawhub.ai/user/agora0x)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use MENTAT to request token-swap quotes, inspect OTC orders and deals, check token addresses, and prepare unsigned escrow transactions. A human must review and explicitly approve each step before a wallet signs or sends it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A mistaken or unreviewed trade step could result in an unwanted financial transaction.

Mitigation: Use a wallet with spending limits and an approval step; verify token contract addresses, amounts, fees, and expiry, then obtain the human's explicit approval before signing or sending.

Risk: MENTAT and its routing services receive order details and wallet addresses, and private deal links remain public on-chain.

Mitigation: Share only necessary information and treat deal details and links as public; do not rely on deal links for confidentiality.

Risk: Remote service and contract claims could not be independently verified.

Mitigation: Independently check contract addresses and settlement details against trusted sources before approving a transaction.

## Reference(s):

- [MENTAT](https://mentat.market)
- [MENTAT ClawHub release](https://clawhub.ai/agora0x/skills/mentat)
- [MENTAT official contract and token address list](https://api.mentat.market/.well-known/contracts.json)

## Skill Output:

**Output Type(s):** [JSON, Text, Guidance]

**Output Format:** [Structured JSON results and concise human-readable guidance; the skill documentation also provides Markdown with curl examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can include quotes, order and deal details, token trust checks, settlement proofs, and unsigned transaction data. Signing and sending are not performed by the skill and require explicit human approval.]

## Skill Version(s):

1.8.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
