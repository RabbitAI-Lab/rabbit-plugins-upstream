## Description:

Guides agents through developing, designing, building, deploying, debugging, migrating, and troubleshooting CloudBase projects across web, WeChat Mini Program, mobile, database, serverless, AI, operations, and specification workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to route CloudBase project work to the right domain guidance, prepare backend resources, implement application code, deploy CloudBase services, and review CloudBase-specific risks before close-out.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents toward cloud deployments, permission changes, and resource creation that may affect billing or live environments.

Mitigation: Confirm the target IDEs, canonical CloudBase environment ID, billing impact, and every deployment or permission change before enabling or executing the skill.

Risk: Generated auth, CORS, JWT, logging, and public endpoint guidance may create insecure application behavior if accepted without review.

Mitigation: Review generated auth guards, CORS settings, JWT handling, logging behavior, and public endpoint rules before deployment.

Risk: High-impact cleanup or shell examples could remove files or change state unexpectedly.

Mitigation: Inspect shell commands, especially cleanup commands such as rm -rf, before running them in a project workspace or cloud environment.

## Reference(s):

- [CloudBase skill page](https://clawhub.ai/binggg/skills/cloudbase)
- [CloudBase Development Guidelines](SKILL.md)
- [Activation Map](references/activation-map.yaml)
- [MCP Setup](references/mcp-setup.md)
- [Tooling Fallback](references/tooling-fallback.md)
- [Deployment Workflow](references/deployment-workflow.md)
- [CloudBase Platform](references/cloudbase-platform/SKILL.md)
- [CloudBase CLI](references/cloudbase-cli/SKILL.md)
- [Web Development](references/web-development/SKILL.md)
- [CloudBase Code Review](references/cloudbase-code-review/SKILL.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with code snippets, shell commands, configuration examples, and review findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be scoped to active CloudBase projects and should identify verification gaps when platform, security, or deployment checks cannot run.]

## Skill Version(s):

1.92.63 (source: server release metadata); artifact frontmatter version 2.28.1

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
