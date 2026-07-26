## Description: <br>
Connects an agent to an Odoo ERP through the drivethru_mcp MCP server to discover and call tools for eBay operations, accounts payable, document pricing review, production scheduling, replenishment purchasing, and permission-scoped internal knowledge. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zmtucker](https://clawhub.ai/user/zmtucker) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and operations agents use this skill to read from and write to Odoo for order, inventory, accounts payable, purchasing, document review, production scheduling, and internal knowledge workflows. It is especially suited to agents answering users from inside Odoo Discuss while operating against live Odoo data with the user's confirmation for writes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can operate on live Odoo business data, including purchase order prices, vendor bills, document filing, production schedules, replenishment purchase orders, and eBay order creation. <br>
Mitigation: Install only for agents that should operate on live Odoo data, scope the Odoo MCP token to intended companies, users, and tools, and require explicit user confirmation before write actions. <br>
Risk: The ODOO_MCP_TOKEN authorizes access to the Odoo MCP server. <br>
Mitigation: Keep the token in the agent environment, treat it as a secret, and do not paste it into chat or skill output. <br>
Risk: Operators may not expect document review, purchasing, or scheduling requests to move records or change Odoo state. <br>
Mitigation: Make operators aware that matching Purchasing documents can update PO prices, post chatter messages, file documents into Matched or Questions, and move purchase documents through confirmation workflows. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zmtucker/skills/drivethru-odoo) <br>
- [Odoo](https://www.odoo.com) <br>
- [Odoo agent_api endpoint surface](references/agent_api_endpoints.md) <br>
- [Document-driven PO pricing review](references/po_pricing_review.md) <br>
- [Production scheduling data model](references/production_scheduling.md) <br>
- [Replenishment to vendor purchasing](references/replenishment_purchasing.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Markdown] <br>
**Output Format:** [Markdown instructions with JSON tool-call examples and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Helper scripts and Odoo MCP calls may return JSON objects from live Odoo workflows.] <br>

## Skill Version(s): <br>
0.6.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
