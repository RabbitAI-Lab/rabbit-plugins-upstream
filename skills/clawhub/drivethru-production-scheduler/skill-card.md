## Description:

Schedules Odoo MRP production batches by ranking open shop-floor work, surfacing art and receipt blockers, and refining runnable batches into machine and time slots through the drivethru_mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zmtucker](https://clawhub.ai/user/zmtucker)

### License/Terms of Use:

MIT-0

## Use Case:

Manufacturing planners and shop-floor operators use this skill to rank Odoo production batches, publish the run order, identify art or receipt blockers, and place ready batches onto eligible machines when timing is reliable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent broad live Odoo MCP access that reads and changes operational records beyond a narrow scheduling boundary.

Mitigation: Install only with an Odoo MCP token scoped to scheduling-specific read/write tools and records; prefer a local allowlist for production tools and keep generic model reads read-only and limited to manufacturing records.

Risk: Confirmed writes can reorder production batches and change machine or time assignments on the shop floor.

Mitigation: Require users to review the exact proposed run order, machine, and slot changes before writes; preserve manual pins unless a human explicitly asks to override them.

Risk: The ODOO_MCP_TOKEN grants access to the Odoo MCP endpoint if exposed.

Mitigation: Provide the token only through the runtime environment, treat it as a secret, never paste it into chat, and rotate it if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zmtucker/skills/drivethru-production-scheduler)
- [zmtucker publisher profile](https://clawhub.ai/user/zmtucker)
- [Odoo](https://www.odoo.com)
- [Scheduling algorithm](references/scheduling_algorithm.md)
- [Receipt readiness](references/receipt_readiness.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API calls, Configuration, Guidance]

**Output Format:** [Markdown responses with inline shell commands and JSON tool-call payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call live Odoo MCP tools and should confirm scheduling writes before changing run order, machines, or time slots.]

## Skill Version(s):

0.4.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
