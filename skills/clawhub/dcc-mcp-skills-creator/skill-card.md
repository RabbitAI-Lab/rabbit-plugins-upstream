## Description:

Creates, edits, and validates DCC-MCP tool skill packages, including their skill instructions and tool declarations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to scaffold, improve, and validate DCC-MCP skill packages for agent adapters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated or modified skill files may contain mistakes or unsafe tool declarations.

Mitigation: Review the generated files and validate the installable skill directory before loading it into an agent or DCC host.

Risk: Installing an unreviewed upstream revision can introduce unexpected code.

Mitigation: If installing from the upstream repository, follow the documented procedure pinned to a previously reviewed commit.

## Reference(s):

- [Skill homepage](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-mcp-skills-creator/SKILL.md)
- [Authoring workflow](references/AUTHORING_WORKFLOW.md)
- [Package validation](references/PACKAGE_VALIDATION.md)
- [Verified installation](references/VERIFIED_INSTALL.md)

## Skill Output:

**Output Type(s):** [Code, Configuration instructions, Shell commands, Files]

**Output Format:** [Markdown guidance and generated skill package files (YAML and Python)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated packages should be reviewed and validated before loading.]

## Skill Version(s):

0.19.108 (source: ClawHub release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
