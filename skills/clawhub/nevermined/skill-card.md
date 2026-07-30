## Description: <br>
Helps an agent use Nevermined payments to buy or sell access with x402, manage API keys and spending delegations, register plans or agents, check buyer and seller balances, and add payment protection to TypeScript or Python services. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nevermined-io](https://clawhub.ai/user/nevermined-io) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to connect AI agents and services to Nevermined payment flows, including x402 purchases, payment-plan registration, protected endpoints, customer onboarding, and buyer or seller reporting. It is suited for agents that need operational payment guidance, REST calls, SDK snippets, and configuration steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide agents through payment flows that may spend real money in live environments. <br>
Mitigation: Default to sandbox, require explicit approval before switching to live, and use small delegation limits with short durations. <br>
Risk: API keys, delegation IDs, x402 tokens, wallet addresses, transaction hashes, and balance metadata are sensitive financial data. <br>
Mitigation: Store secrets in an appropriate secret store and avoid logging or exposing callback query strings, bearer tokens, receipts, and balance details unnecessarily. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/nevermined-io/skills/nevermined) <br>
- [Nevermined App](https://nevermined.app) <br>
- [Nevermined API Discovery](https://api.sandbox.nevermined.app/api/v1/rest/docs-json) <br>
- [Nevermined API Changelog](https://nevermined.ai/docs/development-guide/api-changelog) <br>
- [Get Your Nevermined API Key](https://nevermined.ai/docs/getting-started/get-your-api-key) <br>
- [Autonomous Agent Operations](references/autonomous-operations.md) <br>
- [Client-Side Integration](references/client-integration.md) <br>
- [Payment Plans](references/payment-plans.md) <br>
- [Seller Operations](references/seller-operations.md) <br>
- [Customer Onboarding](references/customer-onboarding.md) <br>
- [x402 Protocol](references/x402-protocol.md) <br>
- [Express.js Integration](references/express-integration.md) <br>
- [FastAPI Integration](references/fastapi-integration.md) <br>
- [MCP Server Paywall](references/mcp-paywall.md) <br>
- [Google A2A Integration](references/a2a-integration.md) <br>
- [LangChain and LangGraph Integration](references/langchain-integration.md) <br>
- [Strands Agent Integration](references/strands-integration.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with REST examples, SDK snippets, configuration steps, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires NVM_API_KEY for authenticated Nevermined calls; defaults to sandbox unless live usage is explicitly approved.] <br>

## Skill Version(s): <br>
1.0.5 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
