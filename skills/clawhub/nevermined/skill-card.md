## Description:

Guides agents and developers through Nevermined payment operations and x402 payment protection for TypeScript and Python services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to purchase payment plans, manage credentials and spending delegations, inspect credits or revenue, and add x402 payment protection to agent services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live API keys and spending delegations can enable unintended charges or access.

Mitigation: Test in sandbox first, tightly cap and time-limit live delegations, and avoid logging tokens or callback URLs.

Risk: A generic manual x402 example may return protected data without confirming successful settlement.

Mitigation: Prefer framework middleware, or explicitly check settlement success before returning protected data.

## Reference(s):

- [Nevermined Payments on ClawHub](https://clawhub.ai/nevermined-io/skills/nevermined)
- [Nevermined API key guide](https://nevermined.ai/docs/agents-guide/get-api-key)
- [Nevermined app](https://nevermined.app)
- [Autonomous agent operations](artifact/references/autonomous-operations.md)
- [Client-side payment integration](artifact/references/client-integration.md)
- [Payment plans](artifact/references/payment-plans.md)
- [x402 protocol integration](artifact/references/x402-protocol.md)
- [Framework integrations](artifact/references/express-integration.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover REST, SDKs, and framework middleware.]

## Skill Version(s):

1.0.10 (source: ClawHub release; bundled skill version 0.5.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
