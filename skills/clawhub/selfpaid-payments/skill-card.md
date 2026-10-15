## Description:

Helps agents prepare USDC payments and collateral deposits on Base using Aave or Morpho, with projected yield-based recovery and a developer fee.

This skill is ready for commercial/non-commercial use.

## Publisher:

[altoninelli](https://clawhub.ai/user/altoninelli)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents prepare USDC payments to recipients on Base while depositing additional USDC into Aave or Morpho to seek yield. The skill proposes a separate developer-fee transfer and unsigned calls for review before wallet signing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A hosted service constructs transactions that pay a recipient and a developer fee and deposit USDC collateral.

Mitigation: Before signing, use a local signer or policy layer to decode actual calldata and confirm each recipient, fee, approval, and deposit.

Risk: The local validator does not enforce the user's maximum approved collateral amount.

Mitigation: Set and enforce a local maximum collateral amount before approving or signing the transaction batch.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/altoninelli/skills/selfpaid-payments)
- [SelfPaid payment API](https://selfpaid.cryptofolio.it/api/v1/payment/build)
- [Base mainnet endpoint](https://mainnet.base.org)

## Skill Output:

**Output Type(s):** [Text, JSON transaction proposals, Code, Guidance]

**Output Format:** [Markdown guidance and JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Unsigned Base transactions and EIP-5792 batch calls; signing and execution remain with the user's wallet.]

## Skill Version(s):

2.1.2 (source: release metadata, frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
