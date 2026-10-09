## Description:

Helps agents quote and purchase pay-per-call x402 data for endpoint trust, Base token safety, and wallet or market intelligence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[33ai-wq](https://clawhub.ai/user/33ai-wq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to assess x402 endpoints or Base tokens before paying or trading, and to request paid wallet and market data with a live price quote.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A funded Base USDC wallet key can authorize paid calls to caller-supplied URLs.

Mitigation: Use a dedicated low-balance wallet, keep the default or a lower payment ceiling, quote each call first, verify payTo manually, and do not let unattended agents choose arbitrary payment URLs.

## Reference(s):

- [XH Agents x402 on ClawHub](https://clawhub.ai/33ai-wq/skills/xh-agents-x402)
- [XH Agents API specification](https://xhagents.xyz/openapi.json)
- [XH Agents x402 discovery](https://xhagents.xyz/.well-known/x402)
- [Paid routes reference](references/routes.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Text and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live price quotes, endpoint or token scores, paid data, and payment receipts.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
