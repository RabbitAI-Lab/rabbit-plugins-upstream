## Description:

Drivethru Operations helps internal teams query, analyze, and coordinate purchasing, manufacturing, inventory, receiving, shipping, replenishment, and accounts-payable workflows in Odoo through the drivethru_mcp MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zmtucker](https://clawhub.ai/user/zmtucker)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and operations teams use this skill to answer Odoo Discuss questions and scheduled routine prompts about purchase orders, receipts, deliveries, inventory, manufacturing, replenishment, and vendor billing. It supports read-only analysis by default and can guide live ERP write workflows when a human gives explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can invoke live Odoo write tools, including purchasing, stock, replenishment, and vendor-bill actions.

Mitigation: Use a least-privilege Odoo MCP token scoped to the intended company, user role, and operations tools, and require explicit human approval before any write action.

Risk: The MCP token grants ERP access and is sent as a bearer credential.

Mitigation: Provide credentials only through ODOO_MCP_URL and ODOO_MCP_TOKEN environment variables, keep the token out of chat and logs, and rotate it if exposure is suspected.

Risk: A broad MCP call interface may expose more tools than this operations workflow needs.

Mitigation: Confirm the MCP server exposes only approved tools before installation and remove administrator or accounting permissions unless they are required for the release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zmtucker/skills/drivethru-operations)
- [Odoo](https://www.odoo.com)
- [Operations field reference](references/field_reference.md)
- [Operations query patterns](references/query_patterns.md)
- [Drive Thru routines](references/routines.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with JSON tool-call arguments, shell command snippets, and concise operational reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses ODOO_MCP_URL and ODOO_MCP_TOKEN for MCP access; tool results are JSON; write actions require explicit human approval.]

## Skill Version(s):

0.5.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
