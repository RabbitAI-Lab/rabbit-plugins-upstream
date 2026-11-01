## Description:

本地 Skill 联动总线与 MCP 安装器，让兼容的 CAD 技能共享项目状态和识图契约，减少重复解析；也可通过 CLI 使用，并在未安装时回退到各技能自身状态。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

面向 CAD 与算量工作流的开发者和使用者，用于在兼容技能间共享项目状态及识图契约，衔接读图与算量流程。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected skills can update shared local project data.

Mitigation: Keep backups and use a local, unsynced state directory.

Risk: Installation can optionally register an MCP server.

Mitigation: Preview with --dry-run, or set SKIP_MCP_REG=1 to skip registration.

## Reference(s):

- [lis-skill-bus on ClawHub](https://clawhub.ai/lisong2003-lgtm/skills/lis-skill-bus)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON project-state and CAD-contract data, with text or JSON CLI/MCP responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-keyed local state; contract shape depends on the selected CAD workflow.]

## Skill Version(s):

0.1.1 (source: SKILL.md frontmatter, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
