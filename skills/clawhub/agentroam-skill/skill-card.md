## Description: <br>
Buy travel eSIM data plans, gift cards, and mobile airtime with crypto through AgentRoam, using live product and payment tools with email delivery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[adiny](https://clawhub.ai/user/adiny) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to find and buy eSIM data plans, gift cards, and prepaid mobile top-ups with supported crypto payments. It guides purchase flows through a required validation and approval step before creating a real order. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The create_order tool creates a real purchase order for a crypto payment. <br>
Mitigation: Use validate_order first, show the order summary, and require explicit user approval before creating the order or sending payment. <br>
Risk: Incorrect product, email, currency, network, amount, or wallet-address details can lead to payment or delivery mistakes. <br>
Mitigation: Verify all purchase details with the user before payment, and rely on live AgentRoam tool responses instead of inventing prices or order states. <br>
Risk: Order status tokens may expose purchase status if shared unnecessarily. <br>
Mitigation: Keep order status tokens private and share them only when needed to check an existing order. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/adiny/agentroam-skill) <br>
- [AgentRoam MCP server](https://agentroam.ai/api/mcp) <br>
- [AgentRoam MCP discovery manifest](https://agentroam.ai/.well-known/mcp.json) <br>
- [ClawHub skill listing](https://clawhub.ai/adiny/skills/agentroam-skill) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with inline tool names, URLs, and setup commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes purchase workflow guidance and explicit approval requirements before real orders.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
