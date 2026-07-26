## Description: <br>
Internal operations agent for the purchasing-to-manufacturing-to-shipping side of Odoo ERP over the `drivethru_mcp` MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zmtucker](https://clawhub.ai/user/zmtucker) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Operations employees use this skill to query and analyze purchase orders, receipts, shipments, inventory moves, replenishment, and manufacturing records in Odoo. It also supports scheduled Drive Thru routine reports and guarded purchasing, stock, pricing, and vendor-bill workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authenticated Odoo MCP access can make live ERP changes, including purchase order, stock, pricing, and vendor-bill updates. <br>
Mitigation: Connect only to a tightly scoped Odoo MCP server, limit the token to intended Odoo roles, and require human approval before any write action. <br>
Risk: Incorrect operations queries can produce misleading counts, totals, or lists for purchasing, inventory, and manufacturing decisions. <br>
Mitigation: Use the self-describing field dictionary, report counts from `total_matched` or server-side aggregates, and include the query method next to reported numbers. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zmtucker/skills/drivethru-operations) <br>
- [Odoo](https://www.odoo.com) <br>
- [Operations field reference](references/field_reference.md) <br>
- [Operations query patterns](references/query_patterns.md) <br>
- [Drive Thru routine guide](references/routines.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with JSON tool results and inline shell commands when invoking the MCP helper] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires `ODOO_MCP_URL`, `ODOO_MCP_TOKEN`, `python3`, and the `mcp>=1.9.0` Python package.] <br>

## Skill Version(s): <br>
0.3.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
