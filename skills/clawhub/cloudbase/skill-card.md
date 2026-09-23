## Description:

Helps agents develop, design, build, deploy, debug, migrate, and troubleshoot Tencent CloudBase projects across Web, WeChat Mini Programs, mobile apps, databases, cloud functions, CloudRun, storage, AI models, AI agents, operations, and specification workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to route CloudBase tasks to the right reference workflow and produce code, commands, configuration, deployment steps, troubleshooting guidance, and review checks for CloudBase-backed applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: One agent-deployment reference was flagged for hidden AI-directed mandates and repeated raw deletion commands.

Mitigation: Review the referenced deployment guidance before use and block automatic cleanup commands such as rm -rf unless the working directory and disposable ./env target have been verified.

Risk: The skill can guide agents through CloudBase project and cloud-resource management.

Mitigation: Install and use it only for intended CloudBase work, confirm the target environment ID before changes, and review global plugin installation or Python agent deployment steps before running them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/cloudbase)
- [CloudBase Development Guidelines](artifact/SKILL.md)
- [CloudBase scenario map](artifact/references/scenarios.md)
- [CloudBase MCP setup](artifact/references/mcp-setup.md)
- [CloudBase deployment workflow](artifact/references/deployment-workflow.md)
- [CloudBase code review](artifact/references/cloudbase-code-review/SKILL.md)
- [CloudBase agent SDK router](artifact/references/cloudbase-agent/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with inline code, command snippets, configuration examples, and file edits when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to read bundled reference files, use CloudBase MCP or CLI workflows, and run verification before completion.]

## Skill Version(s):

1.92.112 (source: ClawHub release evidence, created 2026-09-23; artifact frontmatter reports 2.34.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
