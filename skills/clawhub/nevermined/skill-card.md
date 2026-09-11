## Description:

Use when an AI agent must operate on Nevermined autonomously, purchase a payment plan via x402, enroll a card and create spending delegation, obtain an API key, register payment plans or AI agents, check buyer credits or seller revenue, or add x402 payment protection to TypeScript and Python agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, builders, and autonomous agents use this skill to integrate Nevermined payment rails, buy or settle x402 access, manage delegations and API keys, and protect agent endpoints with paid access control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents can spend real money or manage customer accounts when configured for live Nevermined operations.

Mitigation: Use sandbox first, require explicit human approval for live mode and nontrivial spending limits, and bind delegations to expected plans where possible.

Risk: Unverified 402 payment requirements can direct an agent to pay an unexpected seller, plan, origin, or price.

Mitigation: Validate every 402 payment requirement against an allowlist before creating or sending a payment token.

Risk: API keys, delegation IDs, payment method IDs, and x402 tokens can leak through logs, callback URLs, or command output.

Mitigation: Redact secrets, avoid logging callback request lines, keep credentials in a secret store, and use HTTPS for non-local endpoints.

Risk: Payment enforcement can fail open for protected or side-effecting tools.

Mitigation: Pin SDK and CLI versions, verify settlement paths during integration, and reject protected requests when payment validation or settlement is unavailable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/nevermined-io/skills/nevermined)
- [Nevermined App](https://nevermined.app)
- [Nevermined Documentation](https://nevermined.ai/docs)
- [Get a Nevermined API Key](https://nevermined.ai/docs/agents-guide/get-api-key)
- [Autonomous Agent Purchase Guide](https://nevermined.ai/docs/getting-started/ai-agent-purchase)
- [Card Enrollment and Delegation](https://nevermined.ai/docs/solutions/card-delegation)
- [API Changelog](https://nevermined.ai/docs/development-guide/api-changelog)
- [Autonomous Agent Operations](references/autonomous-operations.md)
- [Client-Side Integration](references/client-integration.md)
- [Payment Plans](references/payment-plans.md)
- [x402 Protocol](references/x402-protocol.md)
- [MCP Server Paywall](references/mcp-paywall.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with code examples, shell commands, API request bodies, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires NVM_API_KEY for Nevermined SDK, REST API, and CLI flows.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
