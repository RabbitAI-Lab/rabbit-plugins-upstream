## Description:

Use when an AI agent must operate on Nevermined autonomously — purchase a payment plan via the x402 protocol (crypto or card), enroll a card and create a spending delegation, obtain a Nevermined API key, register a payment plan or AI agent, or check its credits (as a buyer) or revenue (as a seller) — and when adding x402 payment protection to a TypeScript or Python agent (Express, FastAPI, MCP, Google A2A, Strands, LangChain / LangGraph). Covers the @nevermined-io/payments and payments-py SDKs and the Nevermined REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to manage Nevermined payment plans, purchases, delegations, and account status, or to add x402 payment handling to TypeScript and Python agent services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment flows may spend from a delegation without clear merchant or price validation.

Mitigation: Review the merchant, plan, and price before proceeding, and use a narrowly limited delegation.

Risk: Customer-account provisioning and third-party data handling may exceed the intended scope.

Mitigation: Confirm customer provisioning fits your needs and review third-party data handling before sending sensitive user content.

Risk: The security scan was partial and did not inspect all referenced material.

Mitigation: Review the relevant references before installation; the partial scan cannot rule out additional issues.

## Reference(s):

- [Nevermined skill documentation](https://nevermined.ai/docs/development-guide/build-using-nvm-skill)
- [Autonomous operations](artifact/references/autonomous-operations.md)
- [Payment plans](artifact/references/payment-plans.md)
- [x402 protocol](artifact/references/x402-protocol.md)
- [Client integration](artifact/references/client-integration.md)
- [Express integration](artifact/references/express-integration.md)
- [FastAPI integration](artifact/references/fastapi-integration.md)
- [MCP paywall](artifact/references/mcp-paywall.md)
- [Google A2A integration](artifact/references/a2a-integration.md)
- [LangChain integration](artifact/references/langchain-integration.md)
- [Strands integration](artifact/references/strands-integration.md)
- [Seller operations](artifact/references/seller-operations.md)
- [Customer onboarding](artifact/references/customer-onboarding.md)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Shell commands, Code, Configuration]

**Output Format:** [Markdown with JSON, shell, and TypeScript or Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples may include payment and account operations.]

## Skill Version(s):

1.0.15 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
