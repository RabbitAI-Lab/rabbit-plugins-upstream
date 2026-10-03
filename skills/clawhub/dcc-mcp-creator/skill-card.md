## Description:

Helps developers build or modernize DCC-MCP adapters and standalone studio MCP services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and studio engineers use this skill to design, implement, and validate DCC host adapters or private standalone MCP services using shared runtime contracts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated adapter or service code could expose unsafe behavior when deployed beyond local development.

Mitigation: Review generated code before network exposure or access to production credentials; require operator-managed authentication, TLS, and network controls for intranet deployments.

Risk: Project file edits or local validation commands could change or disrupt the target project.

Mitigation: Review proposed edits and commands, then validate changes in the owner's project before deployment.

## Reference(s):

- [DCC-MCP Creator skill documentation](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-mcp-creator/SKILL.md)
- [Adapter and service workflow](artifact/references/ADAPTER_WORKFLOW.md)
- [Internal service workflow](artifact/references/INTERNAL_SERVICE_WORKFLOW.md)
- [Testing and release guidance](artifact/references/TESTING_AND_RELEASE.md)

## Skill Output:

**Output Type(s):** [Code, Configuration instructions, Shell commands, Guidance]

**Output Format:** [Markdown with code and command examples; project file edits when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Host-specific implementation and validation guidance]

## Skill Version(s):

0.19.107 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
