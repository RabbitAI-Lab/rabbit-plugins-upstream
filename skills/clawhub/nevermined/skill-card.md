## Description: <br>
Guides agents and developers through Nevermined payment operations, including x402 plan purchases, card or stablecoin delegation, API key handling, plan and agent registration, credit or revenue checks, and adding payment protection to TypeScript or Python agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nevermined-io](https://clawhub.ai/user/nevermined-io) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and autonomous-agent operators use this skill to buy or settle Nevermined payment plans, manage card or stablecoin delegations, and add x402 payment gates to Express, FastAPI, MCP, Google A2A, LangChain, LangGraph, or Strands agents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Payment credentials, delegation IDs, payment method IDs, or payment tokens may be exposed through logs, callback query strings, shell history, or process arguments. <br>
Mitigation: Keep NVM_API_KEY and delegation IDs in a secret store, avoid logging callback request lines or full payment tokens, and use HTTPS for any non-local agent endpoint. <br>
Risk: Live payment flows can move real funds or consume paid credits. <br>
Mitigation: Start in sandbox, use live only when explicitly required, and test payment flows with low-value plans before production use. <br>
Risk: Overbroad delegations can authorize more spending than intended. <br>
Mitigation: Use short-lived, low-limit delegations and monitor settle receipts, remaining balances, and delegation transactions. <br>


## Reference(s): <br>
- [Autonomous Agent Operations](references/autonomous-operations.md) <br>
- [Client-Side Integration](references/client-integration.md) <br>
- [Payment Plans](references/payment-plans.md) <br>
- [Seller Operations](references/seller-operations.md) <br>
- [White-label Customer Onboarding](references/customer-onboarding.md) <br>
- [x402 Protocol](references/x402-protocol.md) <br>
- [Express.js Integration](references/express-integration.md) <br>
- [FastAPI Integration](references/fastapi-integration.md) <br>
- [MCP Server Paywall](references/mcp-paywall.md) <br>
- [Google A2A Integration](references/a2a-integration.md) <br>
- [LangChain and LangGraph Integration](references/langchain-integration.md) <br>
- [Strands Agent Integration](references/strands-integration.md) <br>
- [Nevermined Documentation](https://nevermined.ai/docs) <br>
- [Get a Nevermined API Key](https://nevermined.ai/docs/agents-guide/get-api-key) <br>
- [Nevermined App](https://nevermined.app) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown guidance with REST examples and TypeScript/Python snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes API calls, environment variables, and payment-flow safeguards; no executable files are produced by the skill itself.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata; artifact frontmatter reports 0.5.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
