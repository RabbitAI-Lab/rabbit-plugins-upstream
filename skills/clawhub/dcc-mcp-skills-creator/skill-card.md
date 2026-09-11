## Description:

Infrastructure skill that helps agents create, validate, scaffold, and review DCC-MCP skill packages for the dcc-mcp-core ecosystem.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to author, scaffold, validate, and improve DCC-MCP skill packages, including SKILL.md, tools.yaml, scripts, groups, prompts, and taxonomy metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create scaffold files in a user-provided directory.

Mitigation: Run it only in workspaces where creating a new DCC-MCP skill package is intended, and review the target path before execution.

Risk: Generated or proposed skill content could contain incorrect guidance or unsafe workflow assumptions.

Mitigation: Review and scan generated skills before loading or publishing them, and validate installable skill directories with the provided validator or dcc-mcp-cli lint.

Risk: Installing from a mutable branch, tag, or registry alias may not reproduce the reviewed artifact.

Mitigation: Install from a reviewed full Git commit and verify exported content as described by the bundled verified-install procedure.

## Reference(s):

- [DCC-MCP Skill Authoring Workflow](references/AUTHORING_WORKFLOW.md)
- [DCC-MCP Tool Contracts](references/DCC_TOOL_CONTRACTS.md)
- [Gateway-Facing Tag Taxonomy](references/TAXONOMY_COMPATIBILITY.md)
- [Current Tool Contract](references/TOOL_RUNTIME_CONTRACT.md)
- [Install a reviewed Skill revision](references/VERIFIED_INSTALL.md)
- [Source Skill File](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-mcp-skills-creator/SKILL.md)
- [DCC-MCP Skill](https://clawhub.ai/loonghao/skills/dcc-mcp)
- [DCC-MCP Creator Skill](https://clawhub.ai/loonghao/skills/dcc-mcp-creator)
- [Agent Plugin Schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json)
- [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12/schema)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON-compatible tool results, YAML configuration, Python code, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create files under a user-provided skill directory and may return validation reports for existing skill directories.]

## Skill Version(s):

0.19.103 (source: SKILL.md metadata.dcc-mcp.version and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
