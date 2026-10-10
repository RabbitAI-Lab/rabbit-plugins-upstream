## Description:

Helps agents discover and purchase pay-per-call x402 data on Base, including endpoint trust scoring, token safety, wallet intelligence, and document extraction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[33ai-wq](https://clawhub.ai/user/33ai-wq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents can compare live prices and assess x402 endpoints or Base tokens before purchasing data. With an explicitly supplied funded wallet key, they can pay for individual requests and receive results and settlement receipts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A paid call spends USDC from the provided Base wallet.

Mitigation: Use a dedicated low-balance wallet, quote before paying, keep the default or lower price ceiling, and restrict the payment destination with --pay-to when possible.

Risk: Paid requests may disclose submitted documents, internal URLs, credentials, or sensitive prompts to an external service.

Mitigation: Do not submit sensitive material unless external processing is acceptable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/33ai-wq/skills/xh-agents-x402)
- [XH Agents API specification](https://xhagents.xyz/openapi.json)
- [XH Agents x402 discovery](https://xhagents.xyz/.well-known/x402)
- [Route reference](references/routes.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands]

**Output Format:** [Plain-text quotes and receipts, JSON service results, and example shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid results include a decoded payment settlement proof.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
