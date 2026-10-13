## Description:

Helps agents operate supported creative applications through DCC-MCP and discover the tools and marketplace skills needed for the task.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Creative professionals and developers use this skill to find and operate tools for supported applications, perform requested scene or document tasks, and verify the results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: App control can change projects or launch software.

Mitigation: Obtain user authorization for launching apps and project changes, and verify the resulting state.

Risk: Gateway requests may transmit project data to an unapproved destination.

Mitigation: Use loopback by default; use a remote HTTPS gateway only after explicit destination approval and send only necessary data.

Risk: Installing binaries or marketplace adapters changes the local environment.

Mitigation: Review the install plan and obtain consent before installing or publishing; verify release artifacts before replacement.

## Reference(s):

- [ClawHub DCC-MCP release](https://clawhub.ai/loonghao/skills/dcc-mcp)
- [DCC-MCP skill documentation (linked in metadata)](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-mcp/SKILL.md)
- [Tool execution](references/TOOL_EXECUTION.md)
- [UI workflows](references/UI_WORKFLOWS.md)
- [Marketplace maintenance](references/MARKETPLACE_MAINTENANCE.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Text or Markdown with commands and task-specific results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include verified scene, document, or application status after authorized operations.]

## Skill Version(s):

0.19.108 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
