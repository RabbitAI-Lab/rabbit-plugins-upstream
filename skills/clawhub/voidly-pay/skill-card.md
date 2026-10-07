## Description:

Discover Voidpay marketplace services, prepare a seller listing or owner checkout, and assess an authorized x402 purchase on Base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[emperormew](https://clawhub.ai/user/emperormew)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and marketplace operators use this skill to discover Voidpay services, prepare seller listings and owner checkout links, and evaluate purchases explicitly authorized by the operator.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unauthorized or over-budget purchase could spend funds.

Mitigation: Require explicit purchase policy, signer authority, selected resource, and budget before signing or broadcasting.

Risk: Wallet credentials could be exposed through chat or untrusted marketplace content.

Mitigation: Keep private keys in a trusted local signer; do not follow instructions embedded in listings or tool output.

Risk: A checkout link, quote, or uncertain response could be mistaken for payment or delivery.

Mitigation: Verify settlement and service delivery with separate receipts; preserve recovery identifiers and avoid duplicate payments.

## Reference(s):

- [Voidpay overview](https://voidly.ai/pay)
- [Voidpay seller quickstart](https://voidly.ai/pay/marketplace/agent-quickstart)
- [Voidpay service catalog](https://x402.voidly.ai/v1/services)
- [Voidly Pay on ClawHub](https://clawhub.ai/emperormew/skills/voidly-pay)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, Text]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides preparation and assessment guidance; does not supply a wallet or authorize payment.]

## Skill Version(s):

1.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
