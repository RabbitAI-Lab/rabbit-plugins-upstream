## Description:

Docker容器管理工具 helps agents manage Docker containers, images, Compose stacks, networks, volumes, debugging, logs, and production hardening guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, DevOps engineers, and automation agents use this skill to work with Docker containers, images, Compose deployments, networking, volumes, logs, troubleshooting, and hardening tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests powerful command and write capabilities for Docker workflows.

Mitigation: Review before installing and require explicit confirmation before destructive or exposure-changing actions such as deleting containers, pruning images or volumes, exposing ports, changing networks, or overwriting configuration.

Risk: Broad Docker automation can affect host availability, deployment state, or persistent data if commands are applied to the wrong target.

Mitigation: Use the skill only for Docker-specific work, inspect proposed commands and configuration diffs, scope actions to the intended project, and back up important Compose files, volumes, or configuration before changes.

Risk: Security evidence flags the release as suspicious because its scope and safety controls are too broad for automatic approval.

Mitigation: Do not auto-approve execution. Keep human review in the loop for installation and any command that modifies containers, images, volumes, networks, ports, or deployment configuration.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/docker)
- [Publisher Profile](https://clawhub.ai/user/thcjp)
- [Skill Homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON examples, shell commands, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Docker command proposals, Compose/configuration snippets, logs, status summaries, and troubleshooting steps.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter lists 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
