## Description:

Creates, validates, scaffolds, and reviews DCC-MCP skill packages for the dcc-mcp-core ecosystem.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, validate, scaffold, and review DCC-MCP skill packages, including SKILL.md, tools.yaml, scripts, prompts, and reference docs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scaffolding can create files in a caller-provided directory.

Mitigation: Point it only at an intended workspace and review the generated skill before loading or publishing it.

Risk: Generated or improved skill guidance can be incorrect or incomplete.

Mitigation: Run skill validation and review schemas, annotations, scripts, and reference docs before deployment.

Risk: CLI install, update, or feedback actions may change the local agent or DCC-MCP environment.

Mitigation: Run those actions only when explicitly requested and confirm the target package or operation first.

## Reference(s):

- [DCC-MCP Skill Authoring Workflow](references/AUTHORING_WORKFLOW.md)
- [DCC-MCP Tool Contracts](references/DCC_TOOL_CONTRACTS.md)
- [DCC-MCP Skills Creator homepage](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-mcp-skills-creator/SKILL.md)
- [ClawHub skill page](https://clawhub.ai/loonghao/skills/dcc-mcp-skills-creator)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, scaffold files, JSON-like validation reports, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scaffold output writes a skill directory only at the caller-provided parent path; validation output reports errors and warnings for the requested skill directory.]

## Skill Version(s):

0.19.98 (source: metadata.dcc-mcp.version, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
