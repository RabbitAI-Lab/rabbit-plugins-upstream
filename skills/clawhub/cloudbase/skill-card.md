## Description:

Use this skill to guide agents through CloudBase project development, design, deployment, debugging, migration, and troubleshooting across Web, WeChat Mini Programs, mobile apps, databases, cloud functions, CloudRun, storage, AI models, agents, and operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to plan, build, verify, and deploy CloudBase-backed applications and services. It routes agents to targeted CloudBase guidance for authentication, databases, cloud functions, CloudRun, storage, AI model use, operations troubleshooting, UI work, and specification workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents toward broad persistent tooling setup and live CloudBase resource changes.

Mitigation: Prefer project-scoped setup, inspect tool scope before use, and require explicit confirmation before user-wide plugin installs or live resource changes.

Risk: The skill may lead to paid, destructive, or security-sensitive operations such as SQL/RLS changes, deployments, API key creation, or rebuild commands.

Mitigation: Require explicit user confirmation before paid or destructive cloud operations, SQL/RLS changes, deployments, credential creation, and any rm -rf rebuild command.

Risk: The security verdict is suspicious because the skill requests broad authority despite mostly matching its CloudBase development purpose.

Mitigation: Review and scan the skill before deployment, pin reviewed package versions where possible, and use target-specific CloudBase guidance instead of blanket automation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/cloudbase)
- [SKILL.md](artifact/SKILL.md)
- [Activation map](artifact/references/activation-map.yaml)
- [MCP setup](artifact/references/mcp-setup.md)
- [Tooling fallback](artifact/references/tooling-fallback.md)
- [Deployment workflow](artifact/references/deployment-workflow.md)
- [Web development](artifact/references/web-development/SKILL.md)
- [CloudBase code review](artifact/references/cloudbase-code-review/SKILL.md)
- [PostgreSQL development](artifact/references/postgresql-development-cloudbase/SKILL.md)
- [Cloud functions](artifact/references/cloud-functions/SKILL.md)
- [CloudRun development](artifact/references/cloudrun-development/SKILL.md)
- [AI model web](artifact/references/ai-model-web/SKILL.md)
- [CloudBase AI console](https://tcb.cloud.tencent.com/dev?envId={envId}#/ai)
- [Moonshot OpenAI-compatible endpoint](https://api.moonshot.cn/v1)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline code blocks and actionable instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose CloudBase API, MCP, CLI, deployment, and verification steps; user confirmation should gate paid, destructive, or broad-scope operations.]

## Skill Version(s):

1.92.90 (source: server release; artifact frontmatter reports 2.33.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
