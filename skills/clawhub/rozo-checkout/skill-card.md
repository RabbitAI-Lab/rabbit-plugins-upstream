## Description:

Helps an agent pay supported Coinbase payment links and Bitrefill invoices with crypto, and pay eligible x402 APIs from a prepaid Rozo balance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shawnmuggle](https://clawhub.ai/user/shawnmuggle)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fund OpenRouter credits, pay supported Coinbase payment links or Bitrefill invoices, and make eligible x402 payments with supported crypto.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports default attribution derived from an unrelated API key.

Mitigation: Review the attribution behavior and confirm it is acceptable before installing or using the skill.

Risk: The security scan reports payment support beyond the declared asset scope, including a Zcash-related mismatch, and says some files were only partially analyzed.

Mitigation: Review the documented supported assets and payment flows, and treat the scan as incomplete rather than a full script review.

Risk: The security scan reports repeated instructions to run an unpinned package, creating a supply-chain risk.

Mitigation: Pin the package version and verify the package source before running install or payment commands.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/shawnmuggle/skills/rozo-checkout)
- [OpenRouter credits settings](https://openrouter.ai/settings/credits)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Payment status and receipt information, Guidance]

**Output Format:** [Markdown guidance with shell commands and CLI or JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide payment quotes, deposit instructions, transaction status, and receipts; transfer details and wallet transactions require user confirmation.]

## Skill Version(s):

0.1.25 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
