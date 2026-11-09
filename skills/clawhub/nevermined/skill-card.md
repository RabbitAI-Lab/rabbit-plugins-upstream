## Description:

Guides agents and developers in managing Nevermined payments, purchasing and registering plans, checking credits and revenue, and adding x402 payment protection to TypeScript and Python services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and agents use this skill to manage Nevermined buyer and seller workflows or integrate x402 payments into services built with supported TypeScript and Python frameworks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic purchase examples can authorize spending without confirming that the seller, plan, and price match the approved purchase.

Mitigation: Keep use in sandbox until purchase checks are added. Before issuing a payment token, verify the seller, plan, and price; restrict delegations to the intended plan, set small budgets and short expiries, control total delegated spending, and protect API keys and callback logs.

## Reference(s):

- [Autonomous operations](references/autonomous-operations.md)
- [Payment plans](references/payment-plans.md)
- [x402 protocol](references/x402-protocol.md)
- [Nevermined documentation](https://nevermined.ai/docs)
- [Agent purchase guide](https://nevermined.ai/docs/getting-started/ai-agent-purchase)
- [Card delegation guide](https://nevermined.ai/docs/solutions/card-delegation)
- [Nevermined App](https://nevermined.app)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline REST examples, TypeScript and Python code, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples can authorize payments or delegated spending; verify purchase details and use sandbox for testing.]

## Skill Version(s):

1.0.13 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
