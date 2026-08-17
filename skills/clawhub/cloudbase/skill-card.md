## Description:

CloudBase guides agents through development, deployment, debugging, migration, and troubleshooting for CloudBase projects across Web/H5, WeChat Mini Programs, mobile apps, databases, authentication, cloud functions, CloudRun, storage, AI model calls, agent workflows, operations, and specification work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to route CloudBase work to the right local guidance, prepare backend resources, implement app features, deploy CloudBase services, and review CloudBase-specific risks before claiming completion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Examples or guidance could weaken authentication, CORS, public permissions, logging, or secret handling if copied into production without review.

Mitigation: Review auth, CORS, permission, logging, and secret-handling changes before use, and adapt examples to the target environment instead of applying them unchanged.

Risk: The skill may lead an agent toward deployments, provider setup, permission changes, package installs, or shell cleanup commands.

Mitigation: Require explicit confirmation before deployments, provider setup, permission changes, package installs, or rm/rm -rf commands, and inspect generated commands before execution.

Risk: The security verdict marks the release as suspicious because some examples could expose services, leak user data, or run destructive cleanup commands.

Mitigation: Install only for intentional CloudBase work and run a focused review of security-sensitive behavior before allowing the agent to act.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/cloudbase)
- [CloudBase Development Guidelines](SKILL.md)
- [Activation map](references/activation-map.yaml)
- [MCP setup](references/mcp-setup.md)
- [Deployment workflow](references/deployment-workflow.md)
- [Tooling fallback](references/tooling-fallback.md)
- [CloudBase code review](references/cloudbase-code-review/SKILL.md)
- [Web development](references/web-development/SKILL.md)
- [Cloud functions](references/cloud-functions/SKILL.md)
- [PostgreSQL development on CloudBase](references/postgresql-development-cloudbase/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with code snippets, shell commands, and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes work through local reference files and asks for explicit confirmation before sensitive CloudBase actions.]

## Skill Version(s):

1.92.58 (source: ClawHub release metadata; artifact frontmatter reports 2.27.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
