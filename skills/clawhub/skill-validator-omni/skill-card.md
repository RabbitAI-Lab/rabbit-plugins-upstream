## Description:

Validates skills, plugins, and repositories against seven agent-skill authoring and installability standards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adelpro](https://clawhub.ai/user/adelpro)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to audit skills, plugins, or repositories for compliance with agent-skill standards before publishing, installing, or using them as CI gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the published npx command fetches and executes the npm package.

Mitigation: Use the bundled local script when you need to inspect exactly what will run before execution.

Risk: Pointing the validator at the wrong project can produce misleading compliance results.

Mitigation: Pass an explicit skill or repository path for the intended validation target.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/adelpro/skills/skill-validator-omni)
- [Frontmatter template](artifact/references/frontmatter-template.md)
- [Agent Plugins 1.0.0 plugin schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json)
- [Agent Skills discovery schema](https://schemas.agentskills.io/discovery/0.2.0/schema.json)
- [Agent Plugins 1.0.0 MCP schema](https://agent-plugins.org/schemas/1.0.0/mcp.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, JSON validation output, CLI commands, and file-edit guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI use may return exit code 0 for pass, 1 for failed checks, or 2 for usage errors.]

## Skill Version(s):

2.5.1 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
