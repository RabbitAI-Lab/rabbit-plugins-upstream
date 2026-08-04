## Description: <br>
Stripe payments, subscriptions, invoicing, refunds, disputes, and balance with full read/write access for customers through AgentPMT-hosted remote tool calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external agents use this skill to connect AgentPMT workflows to Stripe for billing, subscriptions, invoicing, payment links, refunds, disputes, customer records, and account balance retrieval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives agents broad Stripe read/write authority for financial operations. <br>
Mitigation: Use only with trusted agents and prefer test-mode or least-privilege Stripe credentials. <br>
Risk: Refunds, cancellations, invoice finalization, subscription item deletion, and dispute submissions can have financial or customer-impacting effects. <br>
Mitigation: Require a human approval step outside the skill before these actions are executed. <br>
Risk: Prompts or feedback could expose secrets or unnecessary customer and payment details. <br>
Mitigation: Do not place account secrets, wallet keys, payment headers, or unnecessary customer/payment details into prompts, logs, or feedback. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/agentpmt/skills/stripe-direct-connection) <br>
- [AgentPMT marketplace page](https://www.agentpmt.com/marketplace/stripe-direct-connection) <br>
- [AgentPMT main MCP server](https://api.agentpmt.com/mcp/) <br>
- [AgentPMT REST invoke endpoint](https://api.agentpmt.com/products/purchase) <br>
- [AgentPMT external x402 action endpoint](https://www.agentpmt.com/api/external) <br>
- [Action schema](artifact/schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, API calls, JSON] <br>
**Output Format:** [Markdown instructions with JSON request bodies and remote tool call schemas] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces agent-facing instructions for 28 Stripe actions, including read and write operations for billing, customer, invoice, refund, dispute, subscription, and balance workflows.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
