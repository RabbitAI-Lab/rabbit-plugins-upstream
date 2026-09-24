## Description:

Guides agents through CloudBase project development, deployment, debugging, migration, and troubleshooting across Web, WeChat Mini Program, mobile, databases, cloud functions, CloudRun, storage, AI, agents, operations, and spec workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to select the right CloudBase reference workflow, prepare CloudBase resources, implement application code, deploy services, and review CloudBase-specific safety and quality checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through CloudBase deployments and control-plane operations, including high-impact deletion, force or bypass flags, CAM grants, plan changes, and destructive database migrations.

Mitigation: Use least-privilege credentials and require explicit user confirmation before destructive, permission-changing, force, bypass, plan-changing, or migration operations.

Risk: The security evidence flags unsafe production authentication examples involving TypeScript JWT persistence.

Mitigation: Do not copy those examples into production without proper server-side token verification.

## Reference(s):

- [CloudBase skill listing](https://clawhub.ai/binggg/skills/cloudbase)
- [Main CloudBase skill definition](artifact/SKILL.md)
- [Activation map](artifact/references/activation-map.yaml)
- [CloudBase MCP setup](artifact/references/mcp-setup.md)
- [CloudBase tooling fallback](artifact/references/tooling-fallback.md)
- [CloudBase deployment workflow](artifact/references/deployment-workflow.md)
- [CloudBase code review rules](artifact/references/cloudbase-code-review/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline code, command examples, configuration snippets, and review checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct an agent to read bundled reference files before taking action and to require explicit confirmation for sensitive CloudBase operations.]

## Skill Version(s):

1.92.113 (source: server-resolved release metadata); artifact frontmatter reports 2.34.6

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
