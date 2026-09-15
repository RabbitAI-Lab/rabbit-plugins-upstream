## Description:

Helps agents build, deploy, debug, migrate, and troubleshoot Tencent CloudBase projects across web apps, WeChat mini programs, mobile apps, cloud functions, CloudRun, databases, storage, AI model integrations, agents, operations, and specification workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to route CloudBase work to the right domain guidance, prepare cloud resources, implement application code, deploy services, and verify CloudBase-backed projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent toward persistent user-level tooling changes and cloud resource management actions.

Mitigation: Use a pinned, project-scoped setup when possible, review exact install and management commands before execution, and confirm the intended CloudBase environment before cloud changes.

Risk: Generated deployment or deletion commands may affect the wrong local path or CloudBase environment.

Mitigation: Require explicit EnvId resolution, review target paths, and confirm destructive or production write operations before running them.

Risk: Fallback tooling guidance may encourage global plugin or MCP installs.

Mitigation: Prefer target-specific plugin installation and avoid global npx plugin additions or @latest MCP installs unless the user accepts that scope.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/cloudbase)
- [CloudBase scenarios](references/scenarios.md)
- [Deployment workflow](references/deployment-workflow.md)
- [MCP setup](references/mcp-setup.md)
- [Tooling fallback](references/tooling-fallback.md)
- [CloudBase console entry points](references/console-links.md)
- [CloudBase pricing](https://cloud.tencent.com/document/product/876/75213)
- [CloudBase AI console](https://tcb.cloud.tencent.com/dev?envId={envId}#/ai)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with code blocks, commands, configuration snippets, and implementation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to local reference files and CloudBase management or CLI workflows depending on the user's task.]

## Skill Version(s):

1.92.100 (source: server release metadata; artifact frontmatter reports 2.34.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
