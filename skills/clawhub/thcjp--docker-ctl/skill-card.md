## Description:

Docker控制管理工具 helps agents inspect and manage containers, logs, and images through Podman for lightweight operations workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to inspect container state, review logs, work with images, and support monitoring, alerting, and deployment management in agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Container management actions can modify or disrupt container state.

Mitigation: Use only in environments where the agent is authorized to run Podman, and require explicit approval before starts, stops, removals, builds, file writes, or deployment changes.

Risk: The skill mixes read-only inspection with broader container management and image-building behavior.

Mitigation: Prefer read-only inspection tasks unless a specific operational change has been reviewed and approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/docker-ctl)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured text with occasional JSON or shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Podman inspection and management actions; review commands before execution.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter lists 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
