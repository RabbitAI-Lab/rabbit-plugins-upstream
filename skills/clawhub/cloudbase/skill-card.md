## Description:

Guides agents through developing, designing, building, deploying, debugging, migrating, and troubleshooting CloudBase projects across web, WeChat Mini Programs, mobile apps, databases, cloud functions, CloudRun, storage, AI models, AI agents, operations, and specification workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to route CloudBase work to the right local reference, prepare backend resources, implement CloudBase-backed applications, deploy services, and review CloudBase-specific code paths.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents to make persistent user-level AI IDE tooling changes.

Mitigation: Require explicit user confirmation before MCP or plugin setup and specify a single IDE target.

Risk: Automatic build or deployment guidance may be under-scoped for the user's environment.

Mitigation: Review deployment steps before execution and require confirmation before deploying or changing CloudBase resources.

Risk: Package setup or environment rebuild commands may affect local files or installed tooling.

Mitigation: Pin package versions and validate paths before any environment rebuild or rm -rf step.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/cloudbase)
- [CloudBase development guidelines](artifact/SKILL.md)
- [Activation map](artifact/references/activation-map.yaml)
- [Deployment workflow](artifact/references/deployment-workflow.md)
- [MCP setup](artifact/references/mcp-setup.md)
- [Tooling fallback](artifact/references/tooling-fallback.md)
- [CloudBase console](https://tcb.cloud.tencent.com/dev)
- [CloudBase pricing](https://cloud.tencent.com/document/product/876/75213)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with code, shell command, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to read local scenario-specific references before acting.]

## Skill Version(s):

1.92.90 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
