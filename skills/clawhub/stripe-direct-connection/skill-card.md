## Description: <br>
Stripe Direct Connection lets agents operate Stripe payments, subscriptions, invoices, refunds, disputes, balances, and related billing objects through AgentPMT-hosted remote tool calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, finance operators, and support teams use this skill to let an agent manage Stripe billing workflows such as customer setup, product and price creation, subscriptions, payment links, invoices, refunds, disputes, and balance checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can grant an agent live read/write authority over Stripe customers, billing, invoices, refunds, disputes, subscriptions, and balances. <br>
Mitigation: Use the setup flow for credentials, restrict the connected Stripe key as much as possible, and require explicit human approval before financial writes or broad data reads. <br>
Risk: Refunds, subscription changes, invoice finalization, and dispute submissions can create financial or customer-impacting outcomes. <br>
Mitigation: Require human review and approval for those actions, including the amount, customer, object ID, and business reason before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/agentpmt/skills/stripe-direct-connection) <br>
- [AgentPMT marketplace listing](https://www.agentpmt.com/marketplace/stripe-direct-connection) <br>
- [AgentPMT MCP server](https://api.agentpmt.com/mcp/) <br>
- [AgentPMT REST invoke endpoint](https://api.agentpmt.com/products/purchase) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, API calls] <br>
**Output Format:** [Markdown instructions with JSON request examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Remote AgentPMT calls return JSON from Stripe-related actions; credential handling is routed through the setup flow.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
