## Description: <br>
Schedules Odoo MRP production batches by ranking live work queues, checking receipt readiness, choosing eligible machines and time slots, and proposing or writing schedule changes through the drivethru_mcp MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zmtucker](https://clawhub.ai/user/zmtucker) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Manufacturing planners and Odoo operators use this skill to build and adjust shop-floor production schedules for MRP batches, including rush-order re-ranking and receipt-readiness checks before schedule changes are confirmed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent live MCP access to business scheduling data and scheduling write tools without a tight enforced tool boundary. <br>
Mitigation: Scope the Odoo MCP token to the intended scheduling tools, review available MCP tools with an operator, and require explicit confirmation before every write. <br>
Risk: Schedule changes can affect live production timing if batch, machine, or time-slot choices are applied without review. <br>
Mitigation: State the exact batch, machine, and slot before writing, use atomic bulk scheduling where appropriate, and read back tool results after changes. <br>
Risk: Informal human feedback about receipt-readiness exceptions could become persistent scheduling policy without approval. <br>
Mitigation: Treat feedback as case-specific unless it is captured in approved shop configuration or operator documentation. <br>


## Reference(s): <br>
- [Drivethru Production Scheduler on ClawHub](https://clawhub.ai/zmtucker/skills/drivethru-production-scheduler) <br>
- [Odoo](https://www.odoo.com) <br>
- [Scheduling Algorithm](references/scheduling_algorithm.md) <br>
- [Receipt Readiness](references/receipt_readiness.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, API calls, Guidance] <br>
**Output Format:** [Markdown or conversational text with shell command examples and JSON MCP tool-call payloads.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 plus ODOO_MCP_URL and ODOO_MCP_TOKEN; scheduling writes should be confirmed before execution.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
