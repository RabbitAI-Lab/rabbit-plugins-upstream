## Description: <br>
Use when users ask to order Luckin Coffee, search Luckin stores/products, query pickup code/order status, cancel a Luckin order, or mention Luckin Coffee ordering intents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luckin](https://clawhub.ai/user/luckin) <br>

### License/Terms of Use: <br>
Creative Commons Attribution-NoDerivatives 4.0 International <br>


## Use Case: <br>
External users can use this skill to search Luckin Coffee stores and products, create pickup orders, retrieve payment QR codes, check order status and pickup codes, and cancel orders. It is intended for normal coffee-ordering workflows where the user authorizes real order activity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create real pickup orders and payment QR-code flows. <br>
Mitigation: Require explicit user confirmation of the store, item, quantity, and pricing before order creation, and treat payment links as sensitive order data. <br>
Risk: The skill can access a Luckin MCP bearer token and may persist it locally if the user agrees. <br>
Mitigation: Prefer platform-managed MCP authentication or the LUCKIN_MCP_TOKEN environment variable, avoid pasting tokens into chat, and only save tokens locally after explicit consent. <br>
Risk: Fallback shell commands can send authenticated requests to the Luckin MCP endpoint. <br>
Mitigation: Review command output before sharing it, do not expose Authorization headers, and avoid running placeholder or redacted tokens. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/luckin/skills/my-coffee) <br>
- [Luckin MCP platform](https://open.lkcoffee.com/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, Markdown] <br>
**Output Format:** [Markdown text with order details, payment QR-code links, and occasional shell command examples for MCP fallback calls] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce real order and payment information when used with a valid Luckin MCP token.] <br>

## Skill Version(s): <br>
0.8.4 (source: SKILL.md metadata, manifest.json, CHANGELOG) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
