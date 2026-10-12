## Description:

Provides paid Hyperliquid funding-carry verdicts, hedgeable opportunity scans, and daily digests through x402.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thearkoftech](https://clawhub.ai/user/thearkoftech)

### License/Terms of Use:

MIT-0

## Use Case:

Traders and developers use this skill to request paid funding-carry classifications, hedgeable opportunity scans, and digests when evaluating Hyperliquid markets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid requests ask an agent to sign real on-chain USDC payments.

Mitigation: Set strict wallet spending limits and manually confirm the recipient, mint, network, facilitator, amount, endpoint, and expiry before each signature.

Risk: The optional Vault-lite deposit exposes capital to operator and financial risks.

Mitigation: Avoid deposits unless the operator and financial risks have been independently evaluated.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/thearkoftech/skills/carry-intel)
- [Public track record linked by the skill](https://github.com/TheArkofTech/hl-carry-public)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text or Markdown summaries of market data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid calls require a separately authorized USDC transaction; a free sample is available.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
