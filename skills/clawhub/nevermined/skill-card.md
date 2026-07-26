## Description: <br>
Use when an AI agent must operate on Nevermined autonomously, purchase payment plans via x402, manage card or stablecoin payment delegation, obtain API keys, register payment plans or AI agents, check credits or revenue, or add x402 payment protection to TypeScript and Python agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nevermined-io](https://clawhub.ai/user/nevermined-io) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and autonomous agents use this skill to integrate Nevermined payments, buy or settle access through x402, manage payment delegations, and protect agent endpoints with paid access controls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Nevermined API keys, payment tokens, payment method identifiers, and delegation identifiers can expose credentials or authorize spend if logged or stored insecurely. <br>
Mitigation: Store secrets in a secret manager, avoid logging query strings or full tokens, and require HTTPS for any non-local deployment. <br>
Risk: Using live payment rails can move real money or consume paid credits. <br>
Mitigation: Start in sandbox, require explicit selection of live mode, and use tight delegation budgets with short durations. <br>
Risk: Out-of-date API or SDK assumptions can cause payment flow failures or incorrect integration behavior. <br>
Mitigation: Pin the Nevermined API version, verify endpoints against current Nevermined documentation, and refresh cached skill copies before production use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/nevermined-io/skills/nevermined) <br>
- [Nevermined App](https://nevermined.app) <br>
- [Nevermined Documentation](https://nevermined.ai/docs) <br>
- [Autonomous Agent Purchase Guide](https://nevermined.ai/docs/getting-started/ai-agent-purchase) <br>
- [Get Your API Key](https://nevermined.ai/docs/getting-started/get-your-api-key) <br>
- [Card Enrollment and Delegation](https://nevermined.ai/docs/solutions/card-delegation) <br>
- [API Changelog](https://nevermined.ai/docs/development-guide/api-changelog) <br>
- [Autonomous Agent Operations](references/autonomous-operations.md) <br>
- [Client-Side Integration](references/client-integration.md) <br>
- [Customer Onboarding](references/customer-onboarding.md) <br>
- [Payment Plans](references/payment-plans.md) <br>
- [Seller Operations](references/seller-operations.md) <br>
- [x402 Protocol](references/x402-protocol.md) <br>
- [Express.js Integration](references/express-integration.md) <br>
- [FastAPI Integration](references/fastapi-integration.md) <br>
- [MCP Server Paywall](references/mcp-paywall.md) <br>
- [Google A2A Integration](references/a2a-integration.md) <br>
- [LangChain and LangGraph Integration](references/langchain-integration.md) <br>
- [Strands Agent Integration](references/strands-integration.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline JSON, TypeScript, Python, and shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes REST, SDK, framework integration, environment variable, and operational runbook guidance.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter states 0.5.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
