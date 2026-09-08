## Description:

Connects an agent to an Odoo ERP through the drivethru_mcp MCP server to read and update eBay, accounts payable, purchasing, documents, production scheduling, replenishment, and internal knowledge workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zmtucker](https://clawhub.ai/user/zmtucker)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and operations agents use this skill to answer Odoo-related questions and carry out approved ERP workflows, including product lookup, inventory checks, order creation, vendor bill preparation, PO pricing review, production scheduling, replenishment purchasing, and permission-scoped knowledge retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change live ERP data, including order creation, PO price updates, draft vendor bill creation, document moves, production scheduling, and replenishment PO confirmation.

Mitigation: Scope the Odoo MCP token and Odoo permissions to the intended workflows, and require clear user approval before live write actions.

Risk: The skill depends on ODOO_MCP_TOKEN and ODOO_MCP_URL for authenticated access to the Odoo MCP server.

Mitigation: Provide credentials through environment variables or platform secret management and do not paste the token into chat.

Risk: Pricing review and replenishment workflows can produce incorrect financial or purchasing updates if source documents, stock status, or vendor checkout results are ambiguous.

Mitigation: Use the documented Matched/Questions and out-of-stock pause paths, record issues on the relevant Odoo document or PO, and avoid confirming a PO while an issue remains open.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/zmtucker/skills/drivethru-odoo)
- [Odoo](https://www.odoo.com)
- [Odoo agent API endpoint surface](references/agent_api_endpoints.md)
- [Document-driven PO pricing review](references/po_pricing_review.md)
- [Production scheduling data model](references/production_scheduling.md)
- [Replenishment to vendor purchasing](references/replenishment_purchasing.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration, JSON]

**Output Format:** [Markdown guidance with JSON tool-call examples and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute authenticated Odoo MCP or CLI workflows when the required Odoo endpoint, token, and Python runtime are configured.]

## Skill Version(s):

0.9.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
