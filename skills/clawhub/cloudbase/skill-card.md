## Description:

cloudbase helps agents develop, deploy, debug, migrate, and troubleshoot Tencent CloudBase projects across Web, WeChat Mini Programs, mobile apps, databases, cloud functions, CloudRun, storage, AI model calls, and agent workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to guide CloudBase application work, including resource preparation, authentication, database access, serverless deployment, AI integration, troubleshooting, and review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent CloudBase plugin or MCP setup can give the agent ongoing user-level access inside an AI IDE.

Mitigation: Install only after reviewing the requested IDE target and scope; prefer a single explicit target instead of broad automatic setup.

Risk: Mutable npm or npx commands can install different package contents over time.

Mitigation: Use pinned package or MCP versions where possible and review installation output before continuing.

Risk: CloudBase operations may mutate cloud resources, deployments, domains, or local files.

Mitigation: Require explicit confirmation before resource changes, deployments, domain changes, or local deletion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/cloudbase)
- [Publisher profile](https://clawhub.ai/user/binggg)
- [CloudBase console](https://tcb.cloud.tencent.com/dev)
- [CloudBase security rules documentation](https://docs.cloudbase.net/database/security-rules)
- [artifact/SKILL.md](artifact/SKILL.md)
- [artifact/references/mcp-setup.md](artifact/references/mcp-setup.md)
- [artifact/references/tooling-fallback.md](artifact/references/tooling-fallback.md)
- [artifact/references/deployment-workflow.md](artifact/references/deployment-workflow.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with code blocks and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CloudBase resource plans, CLI or MCP setup steps, application code, configuration snippets, and review findings.]

## Skill Version(s):

1.92.102 (source: server release metadata; artifact frontmatter version: 2.34.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
