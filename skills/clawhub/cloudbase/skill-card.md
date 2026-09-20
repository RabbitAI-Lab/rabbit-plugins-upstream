## Description:

cloudbase helps agents develop, deploy, debug, migrate, and troubleshoot CloudBase projects across web, WeChat Mini Program, mobile, databases, cloud functions, CloudRun, storage, AI model, agent, and operations workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to guide CloudBase application work, including resource preparation, authentication, database access, backend services, deployment, AI integration, and troubleshooting. It is scoped to CloudBase projects and tells agents not to apply it to non-CloudBase or self-hosted backend work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead agents into high-impact cloud, deployment, SQL/RLS, authentication-provider, and delete workflows against real CloudBase resources.

Mitigation: Require the exact EnvId, review affected resources, and obtain explicit confirmation before those operations.

Risk: Force, bypass-check, broad access-policy, or destructive rebuild actions can cause unintended production impact.

Mitigation: Avoid BypassCheck, IsForce, broad RLS policies, and rm -rf rebuilds unless the user intentionally accepts the impact.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/cloudbase)
- [Main skill definition](artifact/SKILL.md)
- [MCP setup](artifact/references/mcp-setup.md)
- [Tooling fallback](artifact/references/tooling-fallback.md)
- [CloudBase CLI reference](artifact/references/cloudbase-cli/SKILL.md)
- [Deployment workflow](artifact/references/deployment-workflow.md)
- [Domestic CloudBase MCP endpoint](https://tcb-api.cloud.tencent.com/mcp/v1)
- [International CloudBase MCP endpoint](https://tcb-api.tencentcloud.com/mcp/v1)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code snippets, shell commands, and configuration fragments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to inspect local reference files, run CloudBase tooling, prepare resources, deploy services, and report verification gaps.]

## Skill Version(s):

1.92.108 (source: server release metadata; artifact frontmatter reports 2.34.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
