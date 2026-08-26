## Description:

Drivethru Odoo lets an agent work with an Odoo ERP through the drivethru_mcp MCP server for inventory, eBay orders, accounts payable, purchasing document review, replenishment, production scheduling, and permission-scoped internal knowledge lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zmtucker](https://clawhub.ai/user/zmtucker)

### License/Terms of Use:

MIT-0

## Use Case:

Operations agents inside an Odoo-backed business use this skill to read ERP records, answer workflow questions, and carry out order, accounts payable, purchasing, replenishment, production, and knowledge-base tasks. The skill is intended for configured agents with Odoo MCP access and clear approval before live write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate on live Odoo business data and perform write actions such as creating orders or bills, updating prices, moving documents, posting messages, assigning activities, confirming purchase orders, and scheduling production.

Mitigation: Install only for agents intended to operate in the Odoo environment and require clear user approval before live write actions.

Risk: The Odoo MCP token is a live business credential.

Mitigation: Keep ODOO_MCP_TOKEN in the agent environment, do not paste it into chat, and verify the MCP server exposes only approved tools.

Risk: The skill depends on the configured Odoo MCP server, required environment variables, and the approved live tool surface.

Mitigation: Before operational use, verify ODOO_MCP_URL, ODOO_MCP_TOKEN, python3, and the attached MCP tools with a low-impact smoke test.

## Reference(s):

- [Odoo Drive Thru MCP integration](SKILL.md)
- [Odoo agent_api endpoint surface](references/agent_api_endpoints.md)
- [Document-driven PO pricing review](references/po_pricing_review.md)
- [Production scheduling data model](references/production_scheduling.md)
- [Replenishment to vendor purchasing](references/replenishment_purchasing.md)
- [Odoo](https://www.odoo.com)
- [ClawHub skill page](https://clawhub.ai/zmtucker/skills/drivethru-odoo)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Plain text or Markdown responses with JSON MCP/tool payloads and shell commands when native tools are unavailable.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ODOO_MCP_URL, ODOO_MCP_TOKEN, python3, and MCP access to the configured Odoo server.]

## Skill Version(s):

0.9.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
