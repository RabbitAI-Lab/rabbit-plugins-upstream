## Description:

Debug failing Power Automate cloud flows with FlowStudio MCP by inspecting run errors, action-level inputs and outputs, flow definitions, and common failure patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ninihen1](https://clawhub.ai/user/ninihen1)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation engineers use this skill to diagnose and repair failing Power Automate cloud flows by locating failed runs, inspecting action-level inputs and outputs, walking back bad data, applying fixes, and verifying with resubmitted or triggered runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to update live Power Automate flows.

Mitigation: Confirm the exact environment and flow, review proposed changes before execution, and prefer non-production testing or an approved maintenance window.

Risk: Resubmitting or triggering runs can repeat side effects such as emails, writes, or downstream records.

Mitigation: Check expected side effects before reruns and use prior-run resubmission or custom trigger payloads only when the user has approved the test.

Risk: Using the skill gives the agent FlowStudio MCP authority over the targeted Power Automate environment.

Mitigation: Install only when that authority is acceptable, scope credentials to the intended environment, and avoid exposing secrets in diagnostic bookends or copied payloads.

## Reference(s):

- [Common Power Automate Errors](references/common-errors.md)
- [FlowStudio MCP Debug Workflow](references/debug-workflow.md)
- [FlowStudio MCP](https://mcp.flowstudio.app)
- [Expression Error in Child Flow Example](https://github.com/ninihen1/power-automate-mcp-skills/blob/main/examples/fix-expression-error.md)
- [Data Entry, Not a Flow Bug Example](https://github.com/ninihen1/power-automate-mcp-skills/blob/main/examples/data-not-flow.md)
- [Null Value Crashes Child Flow Example](https://github.com/ninihen1/power-automate-mcp-skills/blob/main/examples/null-child-flow.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown guidance with Python and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires access to a FlowStudio MCP server and a valid JWT for the target Power Automate environment.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
