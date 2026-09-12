## Description:

Use when an AI agent must operate on Nevermined autonomously to purchase payment plans, enroll payment methods, create delegations, obtain API keys, register payment plans or agents, check buyer or seller status, or add x402 payment protection to TypeScript and Python agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, engineers, and autonomous agent operators use this skill to integrate Nevermined payment rails, buy or sell agent access, manage payment delegations, and protect services with x402 billing flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is security-sensitive because it guides payment operations, API-key handling, payment-signature use, and delegated spending.

Mitigation: Install only after reviewing the exact release, use sandbox until deliberately switching to live, keep delegations short-lived with low spending caps, and send payment tokens only to trusted HTTPS endpoints outside localhost development.

Risk: Mutable upstream instructions could change payment flows after review.

Mitigation: Do not let an agent auto-refresh the skill from a mutable branch without user approval and a fresh review.

Risk: Reusable API keys, delegation IDs, payment method IDs, and callback query strings can leak through logs or traces.

Mitigation: Store secrets in a secret manager, avoid cleartext logs and URL traces, and keep SDK and CLI dependency versions pinned.

## Reference(s):

- [Nevermined Payments on ClawHub](https://clawhub.ai/nevermined-io/skills/nevermined)
- [Nevermined App](https://nevermined.app)
- [Nevermined API Documentation](https://api.sandbox.nevermined.app/api/v1/rest/docs-json)
- [Nevermined API Changelog](https://nevermined.ai/docs/development-guide/api-changelog)
- [Nevermined API Key Guide](https://nevermined.ai/docs/agents-guide/get-api-key)
- [Autonomous Agent Operations](references/autonomous-operations.md)
- [Client-Side Integration](references/client-integration.md)
- [Payment Plans](references/payment-plans.md)
- [Seller Operations](references/seller-operations.md)
- [White-label Customer Onboarding](references/customer-onboarding.md)
- [x402 Protocol](references/x402-protocol.md)
- [Express.js Integration](references/express-integration.md)
- [FastAPI Integration](references/fastapi-integration.md)
- [MCP Server Paywall](references/mcp-paywall.md)
- [LangChain and LangGraph Integration](references/langchain-integration.md)
- [Strands Agent Integration](references/strands-integration.md)
- [Google A2A Integration](references/a2a-integration.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline code, shell commands, JSON request bodies, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include payment API calls, SDK integration snippets, environment variable guidance, and operational runbooks.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 0.5.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
