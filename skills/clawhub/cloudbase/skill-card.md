## Description:

Guides agents through CloudBase development, deployment, debugging, migration, and troubleshooting across Web, WeChat Mini Program, mobile, serverless, storage, database, AI, and operations workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build and operate applications on Tencent CloudBase, including authentication, databases, cloud functions, CloudRun, storage, AI model access, agent workflows, deployment, and code review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill covers broad CloudBase automation, including permissions, public exposure, billing-sensitive AI resources, and deployment workflows.

Mitigation: Use least-privilege CloudBase or Tencent accounts and require explicit confirmation before permission, public exposure, billing, or deployment changes.

Risk: The skill recommends user-wide mutable CloudBase tooling and MCP or hook configuration in some setup paths.

Mitigation: Prefer project-scoped or single-target setup, pin exact package or plugin versions where possible, and review MCP and hook files before restarting the IDE.

Risk: Guidance or generated code may affect authentication, database access, security rules, cloud functions, or CloudRun behavior.

Mitigation: Review proposed changes, run the included CloudBase code review guidance, and verify static and runtime checks before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/cloudbase)
- [ClawHub publisher profile](https://clawhub.ai/user/binggg)
- [CloudBase main skill](artifact/SKILL.md)
- [Activation map](artifact/references/activation-map.yaml)
- [CloudBase scenarios](artifact/references/scenarios.md)
- [MCP setup](artifact/references/mcp-setup.md)
- [Deployment workflow](artifact/references/deployment-workflow.md)
- [Tooling fallback](artifact/references/tooling-fallback.md)
- [CloudBase platform guidance](artifact/references/cloudbase-platform/SKILL.md)
- [CloudBase code review guidance](artifact/references/cloudbase-code-review/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code, command, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose CloudBase resource, permission, deployment, and tooling changes for human review before execution.]

## Skill Version(s):

2.33.2 (source: artifact/SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
