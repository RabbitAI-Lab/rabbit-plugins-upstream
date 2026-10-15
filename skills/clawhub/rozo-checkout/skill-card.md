## Description:

Helps agents pay Coinbase payment links and Bitrefill invoices with supported crypto assets, or pay x402 APIs from a prepaid Rozo balance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shawnmuggle](https://clawhub.ai/user/shawnmuggle)

### License/Terms of Use:

MIT

## Use Case:

Developers and other users can have an agent prepare and track crypto payments for Coinbase links or Bitrefill invoices, or pay x402 endpoints using a prepaid balance. Users review the payment details before transferring funds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crypto transfers and prepaid x402 payments spend real funds and may be difficult to reverse.

Mitigation: Prefer the keyless flow, review amounts and destinations before confirming, and treat x402 requests as real spending even with the default cap.

Risk: Automated sending can expose signing keys or transfer funds from a connected wallet.

Mitigation: Use --send only with a dedicated low-balance hot wallet or encrypted keystore, and review each confirmation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/shawnmuggle/skills/rozo-checkout)
- [Quick start](docs/QUICKSTART.md)
- [Safety design](docs/safety.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Text with shell commands and JSON payment status or deposit details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Payment quotes, confirmations, deposit instructions and status are subject to expiry and chain-specific limits.]

## Skill Version(s):

0.1.19 (source: ClawHub release; internal skill metadata lists 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
