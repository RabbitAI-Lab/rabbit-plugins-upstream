## Description:

Provides pay-per-call x402 access to endpoint trust scoring, Base token safety checks, and wallet and market intelligence without an API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[33ai-wq](https://clawhub.ai/user/33ai-wq)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to quote and pay for x402 endpoint trust checks, Base token screening, and on-chain data before making decisions or spending funds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A payer private key can expose wallet funds if compromised.

Mitigation: Use only a dedicated low-balance wallet, never a production wallet or broadly accessible private key.

Risk: Payment may be signed for an unintended endpoint or recipient.

Mitigation: Quote first, then manually verify the URL, payTo address, network, asset, and price ceiling before paying; do not pay arbitrary untrusted URLs.

Risk: Data submitted to paid routes may disclose sensitive material.

Mitigation: Avoid sending sensitive documents or account information to these routes.

## Reference(s):

- [ClawHub release](https://clawhub.ai/33ai-wq/skills/xh-agents-x402)
- [XH Agents API specification](https://xhagents.xyz/openapi.json)
- [Paid routes](references/routes.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [JSON responses and plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Quotes include price and payment details; paid responses can include a settlement receipt.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
