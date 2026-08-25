## Description:

CloudBase guides agents through building, deploying, debugging, migrating, troubleshooting, and reviewing CloudBase applications across web, WeChat Mini Program, mobile, cloud functions, CloudRun, storage, databases, authentication, AI, and operations workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to plan and implement CloudBase projects, route work to the right CloudBase reference, prepare cloud resources, generate application code and configuration, deploy, troubleshoot, and review changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide persistent CloudBase tooling setup across developer environments.

Mitigation: Review installation steps before use and prefer target-limited plugin installation instead of broad global setup.

Risk: CloudBase commands or generated guidance may affect deployments, permissions, deletion, or public routes.

Mitigation: Confirm the exact CloudBase environment and require explicit approval before executing deploy, delete, permission, or public-route changes.

Risk: Copy-paste authentication or public endpoint examples can weaken access controls if used unchanged.

Mitigation: Add real token validation, least-privilege permissions, and endpoint access review before reusing those examples.

## Reference(s):

- [CloudBase skill release](https://clawhub.ai/binggg/skills/cloudbase)
- [CloudBase Development Guidelines](SKILL.md)
- [Activation Map](references/activation-map.yaml)
- [CloudBase MCP Setup](references/mcp-setup.md)
- [Tooling Fallback](references/tooling-fallback.md)
- [Deployment Workflow](references/deployment-workflow.md)
- [CloudBase CLI](references/cloudbase-cli/SKILL.md)
- [CloudBase Code Review](references/cloudbase-code-review/SKILL.md)
- [Web Development](references/web-development/SKILL.md)
- [Cloud Functions](references/cloud-functions/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code snippets, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose CloudBase API or tooling actions that require environment-specific review before deployment, deletion, permission, or public-route changes.]

## Skill Version(s):

1.92.70 (source: server release metadata; artifact frontmatter lists 2.32.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
