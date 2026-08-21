## Description:

OpenClaw 工作流快速入门指南 - 含业务流程处理（TaskFlow）与数字资源入库（ClawHub）的端到端实操步骤，适用于新用户在 30 分钟内完成从内容创作到资源发布的完整链路

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this guide to learn an end-to-end workflow for TaskFlow orchestration and ClawHub resource publishing. It provides practical setup steps, API examples, CLI commands, metadata checks, and release verification guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The guide includes install, login, update, and publish commands that can modify a local CLI environment or publish resources to a registry.

Mitigation: Run commands only when those side effects are intended, and review the target slug, version, metadata, and publish path before execution.

Risk: The guide includes TaskFlow API examples for persistent workflow state and lifecycle changes.

Mitigation: Use the examples with an authorized OpenClaw runtime context and verify flow IDs, revisions, waiting state, and final status before mutating a live workflow.

## Reference(s):

- [Reference README](reference/README.md)
- [OpenClaw documentation](https://docs.openclaw.ai)
- [ClawHub registry](https://clawhub.com)
- [ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/workflow-starter-guide)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guide with TypeScript examples, shell command blocks, checklists, and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes operational examples for TaskFlow APIs and ClawHub CLI actions.]

## Skill Version(s):

1.0.0 (source: server release, skill frontmatter, _meta.json, reference/README.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
