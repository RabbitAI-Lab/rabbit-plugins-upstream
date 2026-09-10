## Description:

Guides agents through CloudBase application development, deployment, debugging, migration, and troubleshooting for web, WeChat Mini Program, mobile, serverless, database, storage, AI, and operations workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to select CloudBase-specific workflows, configure or deploy CloudBase resources, implement application features, integrate authentication, databases, storage, AI models, and troubleshoot operations issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-wide plugin or MCP setup may change the user's agent environment beyond the current project.

Mitigation: Prefer a specific IDE target or project-scoped setup where available, and confirm the scope before running install commands.

Risk: Mutable npm package installation can pull unreviewed versions.

Mitigation: Pin reviewed package versions where possible and inspect install commands before execution.

Risk: CloudBase deployment, cleanup, and resource-management commands can overwrite, delete, or expose cloud resources.

Mitigation: Require explicit user confirmation for destructive or production-affecting actions, including cleanup commands such as rm -rf ./env and any cloud resource changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/cloudbase)
- [CloudBase skill definition](SKILL.md)
- [Activation map](references/activation-map.yaml)
- [MCP setup](references/mcp-setup.md)
- [Deployment workflow](references/deployment-workflow.md)
- [Tooling fallback](references/tooling-fallback.md)
- [CloudBase scenarios](references/scenarios.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline code blocks, shell commands, configuration snippets, and implementation notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose CloudBase MCP, CLI, deployment, cleanup, and package-install commands that require user review before execution.]

## Skill Version(s):

1.92.88 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
