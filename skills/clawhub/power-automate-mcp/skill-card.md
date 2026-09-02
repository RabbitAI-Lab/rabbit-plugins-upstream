## Description:

Foundation skill for Power Automate via FlowStudio MCP: auth setup, reusable Python and Node.js MCP helpers, tool discovery, and oversized-response handling for agents connecting to Power Automate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ninihen1](https://clawhub.ai/user/ninihen1)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this foundation skill to connect an agent to FlowStudio MCP for Power Automate, discover relevant tool schemas, call flows and environment tools, and parse large or nested MCP responses. It supports setup and shared plumbing for build, debug, monitoring, and governance workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables an agent to use a FlowStudio MCP token to inspect and potentially operate Power Automate assets.

Mitigation: Install only for intended Power Automate work, use the least-privileged account that fits the task, and avoid admin-wide modes unless required.

Risk: Flow updates, triggers, and state changes can affect tenant automation when incorrect environment or flow identifiers are used.

Mitigation: Verify environment and flow IDs before any update, trigger, or state-change operation.

Risk: Large spilled MCP responses may contain confidential tenant data.

Mitigation: Treat spill files as confidential and extract only the fields needed for the task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ninihen1/skills/power-automate-mcp)
- [FlowStudio MCP](https://mcp.flowstudio.app)
- [MCP Bootstrap](references/MCP-BOOTSTRAP.md)
- [Tool Response Catalog](references/tool-reference.md)
- [Action Types Reference](references/action-types.md)
- [Connection References](references/connection-references.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python, JavaScript, PowerShell, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes MCP request patterns, response parsing guidance, and references for handling oversized tool results.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
